extends "res://scripts/global_shoot.gd"

onready var laser = preload("res://scenes/laser.tscn")
onready var middle = get_node("middle")

var on = false
var l = null

func shoot():
	if on:
		if l:
			l.start_at(player.get_rot(), middle.get_global_pos())
		elif l == null:
			on = false
	if not on:
		l = laser.instance()
		player.bullet_container.add_child(l)
		l.start_at(player.get_rot(), middle.get_global_pos())
		on = true
		
