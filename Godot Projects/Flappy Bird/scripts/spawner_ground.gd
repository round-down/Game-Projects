# script ground_spawner

extends Node2D

const scn_ground = preload("res://scenes/ground.tscn")
const GROUND_WIDTH = 168

func _ready():
	for i in range(int(stage_manager.AMOUNT_TO_FILL_VIEW / GROUND_WIDTH) + 2):
		spawn_and_move()
	pass

func spawn_and_move():
	var new_ground = scn_ground.instance()
	new_ground.set_pos(get_pos())
	new_ground.connect("exit_tree", self, "spawn_and_move")
	get_node("container").call_deferred("add_child", new_ground)
	set_pos( get_pos() + Vector2(GROUND_WIDTH, 0) )
	pass
