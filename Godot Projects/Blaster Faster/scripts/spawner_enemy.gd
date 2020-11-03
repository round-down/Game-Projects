# script spawner_enemy

extends Node

# settings
onready var screen_size = utils._get_view_size()
var extents

onready var enemies = [preload("res://scenes/enemy_kamakaze.tscn"),
					   preload("res://scenes/enemy_clever.tscn")
]

onready var container = get_node("container")

func _ready():
	yield(utils.create_timer(5, self), "timeout")
	spawn()
	pass

func spawn():
	while true:
		randomize()
		
		var e = utils.choose(enemies).instance()
		extents = utils.get_extents(e.get_node("sprite"), true)
		var pos = Vector2(rand_range(extents.x, screen_size.x - extents.x), -extents.y)
		e.set_pos(pos)
		container.call_deferred("add_child", e)
		yield(utils.create_timer(rand_range(0.5, 1.25), self), "timeout")
	pass
