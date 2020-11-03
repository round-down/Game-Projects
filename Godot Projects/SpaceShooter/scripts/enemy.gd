extends Area2D

signal explode
signal pulse_timeout # enables pulsed shots

var bullet = preload("res://scenes/enemy bullet.tscn")

onready var paths = get_node("enemy paths")
onready var bullet_container = get_node("bullet container")
onready var gun_timer = get_node("gun timer")
onready var anim = get_node("anim")

var path
var follow
var remote
var speed = 250
var accuracy = 0.1
var target = null
var health = global.enemy_health
var pulse_timer
var gun_to_use = (randi() % 2)


func _ready():
	pulse_timer = Timer.new()
	add_child(pulse_timer)
	pulse_timer.connect("timeout", self, "emit_pulse_timeout")
	add_to_group("enemies")
	set_process(true)
	randomize()
	path = paths.get_children()[randi() % paths.get_child_count()]
	follow = PathFollow2D.new()
	follow.set_name("PathFollow2D")
	path.add_child(follow)
	follow.set_loop(false)
	remote = Node2D.new()
	follow.add_child(remote)
	gun_timer.set_wait_time(1.5)  # vary by level
	gun_timer.start()

func _process(delta):
	follow.set_offset(follow.get_offset() + speed * delta)
	set_pos(remote.get_global_pos())
	if follow.get_unit_offset() > 1:
		queue_free()

func damage(amount, boolean):
	anim.play("hit")
	health -= amount
	if health <= 0:
		global.score += global.enemy_points
		queue_free()
		emit_signal("explode", get_global_pos(), boolean)

func shoot1():
	var dir = get_global_pos() - target.get_global_pos()
	var b = bullet.instance()
	bullet_container.add_child(b)
	b.start_at(dir.angle() + rand_range(-accuracy, accuracy), get_global_pos())
	sounds.play("eshoot")
	
func shoot3():
	var dir = get_global_pos() - target.get_global_pos()
	for a in [-0.1, 0, 0.1]:
		var b = bullet.instance()
		bullet_container.add_child(b)
		b.start_at(dir.angle() + a + rand_range(-accuracy, accuracy), get_global_pos())
		sounds.play("eshoot")

func shoot_pulse(n, delay):
	for i in range(n):
		if gun_to_use == 0:
			shoot1()
		else:
			shoot3()
		pulse_delay(delay)
		yield(self, "pulse_timeout")

func _on_gun_timer_timeout():
	if target.is_visible():
		shoot_pulse(3, 0.1)

func pulse_delay(delay):
	pulse_timer.set_wait_time(delay)
	pulse_timer.set_timer_process_mode(0)
	pulse_timer.start()
	
func emit_pulse_timeout():
	emit_signal("pulse_timeout")

func rotate():
	anim.play("rotate")