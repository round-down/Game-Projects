extends "res://scripts/global_shoot.gd"

onready var left = get_node("left")
onready var right = get_node("right")
onready var anim = get_node("anim")

var list1 = [0.04, 0.1, 0.05, 0.5, 0.3, 0.06, 0.4]
var list2 = [-0.3, -0.1, -0.08, -0.05, -0.2, -0.02, -0.4]

func _ready():
	randomize()
	gun_timer.set_wait_time(0.1)

func shoot():
	var r = (randi() % 6)
	gun_timer.start()
	anim.play("shoot_machine")
	var b = bullet.instance()
	player.bullet_container.add_child(b)
	b.start_at(player.get_rot() + list1[r], left.get_global_pos())
	var b2 = bullet.instance()
	player.bullet_container.add_child(b2)
	b2.start_at(player.get_rot() + list2[r], right.get_global_pos())
	sounds.play("shoot")
