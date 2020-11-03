extends "res://scripts/global_shoot.gd"

onready var anim = get_node("anim")
onready var left = get_node("left")
onready var right = get_node("right")

func _ready():
	gun_timer.set_wait_time(0.2)

func shoot():
	gun_timer.start()
	anim.play("shoot_dual")
	var b = bullet.instance()
	player.bullet_container.add_child(b)
	b.start_at(player.get_rot() - 0.01, left.get_global_pos())
	var b2 = bullet.instance()
	player.bullet_container.add_child(b2)
	b2.start_at(player.get_rot() + 0.01, right.get_global_pos())
	sounds.play("shoot")
	
