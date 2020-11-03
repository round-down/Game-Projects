extends "res://scripts/global_shoot.gd"

onready var cannon = preload("res://scenes/cannon.tscn")
onready var anim = get_node("anim")
onready var middle = get_node("middle")

func _ready():
	gun_timer.set_wait_time(3.2)
	
func shoot():
	gun_timer.start()
	anim.play("shoot_cannon")
	var c = cannon.instance()
	player.bullet_container.add_child(c)
	c.start_at(player.get_rot() - PI, middle.get_global_pos())
	sounds.play("shoot")

