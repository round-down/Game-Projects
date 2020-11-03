extends Node

var asteroid = preload("res://scenes/asteroid.tscn")
var explosion = preload("res://scenes/explosion.tscn")
var enemy = preload("res://scenes/enemy.tscn")
onready var spawns = get_node("spawn locations")
onready var asteroid_container = get_node("asteroid container")

onready var hud = get_node("hud")
onready var player = get_node("player")

onready var restart_timer = get_node("restart timer")
onready var enemy_timer = get_node("enemy timer")

func _ready():
	music.play()
	set_process(true)
	player.connect("explode", self, "explode_player")
	begin_next_level()
	
func begin_next_level():
	global.level += 1
	global.create_timer(1.3, true)
	player.empty_bullet_container()
	player.change_guns()
	hud.shield_destroyed(false)
	if global.level >= 2:
		enemy_timer.stop()
		enemy_timer.set_wait_time(rand_range(20, 105))
		enemy_timer.start()
	hud.show_message("Wave %d" % global.level)
	for i in range(global.level):
		spawn_asteroid("big", spawns.get_child(i).get_pos(), Vector2())
	

func spawn_asteroid(size, pos, vel):
	var a = asteroid.instance()
	asteroid_container.add_child(a)
	a.connect("explode", self, "explode_asteroid")
	a.init(size, pos, vel)
	
func _process(delta):
	hud.update(player)
	if asteroid_container.get_child_count() == 0:
		begin_next_level()

func explode_asteroid(size, pos, vel, hit_vel, boolean):
	var new_size = global.break_pattern[size]
	if new_size:
		for offset in [-1, 1]:
			var new_pos = pos + hit_vel.tangent().clamped(25) * offset
			var new_vel = vel + hit_vel.tangent() * offset
			spawn_asteroid(new_size, new_pos, new_vel)
	var expl = explosion.instance()
	add_child(expl)
	expl.set_pos(pos)
	expl.play()
	if boolean == false:
		return
	else:
		sounds.play("expl")
	
func explode_player():
	player.disable()
	var expl = explosion.instance()
	add_child(expl)
	expl.set_pos(player.pos)
	expl.set_scale(Vector2(1.5,1.5))
	expl.set_animation("sonic")
	expl.play()
	sounds.play("sonic")
	hud.show_message("Game Over")
	restart_timer.start()

func _on_restart_timer_timeout():
	global.new_game()
	
func explode_enemy(pos, boolean):
	var expl = explosion.instance()
	add_child(expl)
	expl.set_pos(pos)
	expl.set_animation("sonic")
	expl.play()
	if boolean == true:
		sounds.play("sonic")

func _on_enemy_timer_timeout():
	var e = enemy.instance()
	add_child(e)
	e.target = player
	if e.gun_to_use == 1:
		e.health = global.enemy_health/3.5
	e.connect("explode", self, "explode_enemy")
	enemy_timer.set_wait_time(rand_range(20, 40))
	enemy_timer.start()
