extends "res://scripts/global_shoot.gd"

onready var middle = get_node("middle")

func _ready():
	gun_timer.set_wait_time(0.5)

func shoot():
	gun_timer.start()
	var b = bullet.instance()
	player.bullet_container.add_child(b)
	b.start_at(player.get_rot(), middle.get_global_pos())
	sounds.play("shoot")
	

