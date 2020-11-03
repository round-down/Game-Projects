#script 101.gd
extends Sprite

onready var parti = preload("res://Scenes/parti.tscn")
onready var explode = preload("res://Scenes/explode.tscn")
onready var anim = find_node("anim")
onready var timer = get_node("timer")
onready var main = get_node("/root/main")
onready var explo_container = get_node("/root/main/explosion container")
onready var parti_container = get_node("/root/main/parti container")
onready var score_lbl = get_node("/root/main/hud/score")
onready var mob_container = get_node("/root/main/mob container")
onready var powerup_bar = get_node("/root/main/hud/powerup")

var screensize = Vector2(Globals.get("display/width"), Globals.get("display/height"))
var extents = get_texture().get_size() / 4
var vel
var pos = Vector2()
var spin
var time
var enlarged
var spawn_size
var x_enlarged = false
var exlrg_chance
var x_counter = 0
var ignore_walls = false
var amount_spawn_on_explode

func _unhandled_input(event):
	# If player "pops" a Robo, explode and spawn more.
	if event.type == InputEvent.SCREEN_TOUCH:
		if event.pressed:
			if get_scale() == Vector2(1,1):
				if (get_pos().x - 39) <= event.x and event.x <=  (get_pos().x + 39):
					if (get_pos().y - 39) <= event.y and event.y <=  (get_pos().y + 39):
						spawn_robos( event.x, event.y )
						powerup_bar.set_val(mob_container.get_child_count())
	pass

func _process(delta):
	if not exlrg_chance in [4,5] and timer.get_time_left() <= 10:
			exlrg_chance = 4
	if timer.get_time_left() <= global.mob_timer and ignore_walls == false:
		ignore_walls = true
		if enlarged == false:
			anim.play("enlrg")
			enlarged = true
			yield(anim,"finished")
		if x_enlarged == false:
			anim.play("exlrg")
			yield(anim,"finished")
		set_scale(Vector2(1,1))
		anim.play("blink_red")
		
	
	if get_scale() == Vector2(0.1,0.1):
		extents = get_texture().get_size() / 40
	elif get_scale() == Vector2(0.5,0.5):
		extents = get_texture().get_size() / 4
	elif get_scale() == Vector2(1,1):
		extents = get_texture().get_size() - Vector2(39,39)
	set_rot(get_rot() + spin * delta)
	set_pos(get_pos() + vel * delta)
	
	if get_pos().x >= screensize.x - extents.width:
		spawn_parti( Vector2(screensize.x + 5, get_pos().y) )
		animate()
		vel.x *= -1
		set_pos(Vector2(screensize.x - extents.width, get_pos().y))
		_hit_sound()
		
	elif get_pos().x <= 0 + extents.width:
		spawn_parti( Vector2(-5, get_pos().y) )
		animate()
		vel.x *= -1
		set_pos(Vector2(extents.width, get_pos().y))
		_hit_sound()
		
	if get_pos().y >= screensize.y - extents.height:
		spawn_parti( Vector2(get_pos().x,screensize.y + 5) )
		animate()
		vel.y *= -1
		set_pos(Vector2(get_pos().x,screensize.y - extents.height))
		_hit_sound()
		
	elif get_pos().y <= 0 + extents.height:
		spawn_parti( Vector2(get_pos().x,0 - 5) )
		animate()
		vel.y *= -1
		set_pos(Vector2(get_pos().x,extents.height))
		_hit_sound()
	pass

func _ready():
	randomize()
	set_process(true)
	set_process_unhandled_input(true)
	if get_parent().get_name() == "main menu":
		set_process_unhandled_input(false)
	spawn_size = randi() % 2
	amount_spawn_on_explode = randi() % 4
	if spawn_size == 0:
		enlarged = false
		set_scale(Vector2(0.1,0.1))
	else:
		enlarged = true
		set_scale(Vector2(0.5,0.5))
	exlrg_chance = randi() % 9
	spin = rand_range(-PI,PI)
	vel = Vector2(rand_range(100,200), 0).rotated(rand_range(0,2*PI))
	
	time = randi() % 61
	if time < 10:
		time = 10
	timer.set_wait_time(time)
	timer.start()
	yield(timer, "timeout")
	var explo = explode.instance()
	explo.set_pos(get_pos())
	explo_container.add_child(explo)
	snd_player.play("explode")
	queue_free()
	print("Success")
	powerup_bar.set_val(mob_container.get_child_count())
	pass

func _hit_sound():
	if abs(vel.x) <= 100:
		snd_player.play("Hit_1")
	else:
		snd_player.play("Hit_2")
	pass

func spawn_robos( x, y ):
	explode()
	for i in range(amount_spawn_on_explode + 1):
		main.call( "spawn", x, y )

func explode():
	global.score += int(timer.get_time_left())
	score_lbl.set_text(str(global.score))
	snd_player.play("explode")
	var explo = explode.instance()
	explo_container.add_child(explo)
	explo.set_global_pos(get_global_pos())
	queue_free()

func spawn_parti( pos ):
	var p = parti.instance()
	parti_container.add_child(p)
	p.set_global_pos( pos )
	pass
	
func animate():
	if ignore_walls == false:
		if enlarged == false:
			anim.play("enlrg")# goes to large
			enlarged = true
			vel -= vel * 0.05
		elif enlarged == true:
			if exlrg_chance in [4,5] and x_enlarged == false and x_counter == 0:
				anim.play("exlrg")# goes to extra large
				x_enlarged = true
				vel -= vel * 0.1
			elif x_enlarged == true:
				anim.play("normal_size")# goes back to normal
				x_enlarged = false
				vel += vel * 0.1
				x_counter += 1
			else:
				anim.play("sq")# goes to small
				enlarged = false
				vel += vel * 0.1
				x_counter = 0
			
	vel.x = clamp(vel.x, -400, 400)
	vel.y = clamp(vel.y, -400, 400)
	pass
		