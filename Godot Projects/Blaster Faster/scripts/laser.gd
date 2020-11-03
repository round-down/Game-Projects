# script laser

extends Area2D

onready var scn_flare = preload("res://scenes/flare.tscn")

export var velocity = Vector2()

func _ready():
	set_process(true)
	
	yield(get_node("vis_notifier"), "exit_screen")
	queue_free()
	pass

func _process(delta):
	translate(velocity * delta)
	pass

func create_flare():
	var flare = scn_flare.instance()
	flare.set_pos(get_pos())
	utils.main_node.call_deferred("add_child", flare)
	pass