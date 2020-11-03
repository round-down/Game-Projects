extends Area2D

signal explode
signal shield_destroyed

export var rot_speed = 3
export var thrust = 500
export var max_vel = 400
export var friction = 0.1

onready var exhaust_back = get_node("exhaust back")
onready var exhaust_front = get_node("exhaust front")
onready var exhaust_rot_left = get_node("exhaust rot left")
onready var exhaust_rot_right = get_node("exhaust rot right")

onready var extents = get_node("ship").get_texture().get_size() / 2
onready var bullet_container = get_node("bullet container")

onready var gun_timer = get_node("gun timer")

var screensize = Vector2(Globals.get("display/width"), Globals.get("display/height"))
var rot = 0
var pos = screensize / 2
var vel = Vector2()
var acc = Vector2()
var shield_level = global.shield_max
var shield_up = true
var auto_shoot = false
var current_gun = null
var gun_list = ["res://scenes/shoot_single.tscn", "res://scenes/shoot_dual.tscn", "res://scenes/shoot_machine.tscn", \
				"res://scenes/shoot_cannon.tscn", "res://scenes/shoot_laser.tscn"]

onready var vControl = get_node("/root/main/hud/HorControl")
onready var hControl = get_node("/root/main/hud/VertControl")
onready var shoot = get_node("/root/main/hud/shoot")

onready var anim = get_node("anim")

func _ready():
	randomize()
	set_pos(pos)
	set_process(true)
	shoot.connect("toggled", self, "auto_shoot_toggled")
	
func auto_shoot_toggled(pressed):
	if pressed == true:
		auto_shoot = true
	else:
		auto_shoot = false

func _process(delta):
	if shield_up:
		shield_level = min(shield_level + global.shield_regen * delta, 100)
		if shield_level <= 0 and shield_up:
			shield_up = false
			shield_level = 0
			get_node("shield").hide()
			emit_signal("shield_destroyed", true)
	if (Input.is_action_pressed("ui_select") or auto_shoot == true) and gun_timer.get_time_left() == 0:
		anim.play("shoot")
		current_gun.shoot()
	if Input.is_action_pressed("ui_left") or vControl.val > 0.01:
		rot += rot_speed * abs(vControl.val) * delta
		exhaust_rot_right.show()
	else:
		exhaust_rot_right.hide()
	if Input.is_action_pressed("ui_right") or vControl.val < -0.01:
		rot -= rot_speed * abs(vControl.val) * delta
		exhaust_rot_left.show()
	else:
		exhaust_rot_left.hide()
	if Input.is_action_pressed("ui_up") or hControl.val > 0.01:
		acc = Vector2(thrust * hControl.val, 0).rotated(rot)
		exhaust_front.hide()
		exhaust_back.show()
	elif Input.is_action_pressed("ui_down") or hControl.val < -0.01:
		acc = Vector2(-thrust * -hControl.val, 0).rotated(rot)
		exhaust_back.hide()
		exhaust_front.show()
	else:
		acc = Vector2(0,0)
		exhaust_back.hide()
		exhaust_front.hide()
		
	acc += vel * -friction
	vel += acc * delta
	pos += vel * delta
	if pos.x - extents.width > screensize.x:
		pos.x = -extents.width
	if pos.x + extents.width < 0:
		pos.x = screensize.x + extents.width
	if pos.y - extents.height > screensize.y:
		pos.y = -extents.height
	if pos.y + extents.height < 0:
		pos.y = screensize.y + extents.height
	set_pos(pos)
	
	set_rot(rot - PI/2 )
	
func change_guns():
	gun_timer.stop()
	var a
	if current_gun:
		current_gun.queue_free()
		sounds.play("next_wave")
		shield_up = true
		shield_level = global.shield_max
	if global.level == 1:
		a = load("res://scenes/shoot_single.tscn")
	elif global.level == 2:
		a = load("res://scenes/shoot_dual.tscn")
	elif global.level == 3:
		a = load("res://scenes/shoot_machine.tscn")
	elif global.level == 4:
		a = load("res://scenes/shoot_cannon.tscn")
	elif global.level == 5:
		a = load("res://scenes/shoot_laser.tscn")
	
	# temporary
	elif global.level >= 6:
		var r = (randi() % 5)
		a = load(gun_list[r])
	var b = a.instance()
	add_child(b)
	current_gun = b
	
func empty_bullet_container():
	for i in range(bullet_container.get_child_count()):
		var c = bullet_container.get_child(i)
		if c.get_name() == "laser":
			c.queue_free()

func _on_player_body_enter( body ):
	if is_hidden():
		return
	if body.get_groups().has("asteroids"):
		if shield_up == true:
			body.explode(vel, true)
			damage(global.ast_damage[body.size])
		else:
			emit_signal("explode")
			
func _on_player_area_enter( area ):
	if area.get_groups().has("enemies"):
		if not is_hidden():
			area.damage(global.run_into_enemy_damage, true)
			damage(global.run_into_enemy_damage/2)
	
func disable():
	hide()
	set_process(false)
	
func damage(amount):
	if shield_up:
		shield_level -= amount
	else:
		disable()
		emit_signal("explode")


