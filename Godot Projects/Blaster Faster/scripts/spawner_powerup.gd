# script spawner_powerup

extends Node

# settings
onready var screen_size = utils._get_view_size()
var extents

onready var powerups = [preload("res://scenes/powerup_armor.tscn"),
						preload("res://scenes/powerup_laser.tscn")
]

onready var container = get_node("container")

func _ready():
	yield(utils.create_timer(rand_range(10, 15), self), "timeout")
	spawn()
	pass

func spawn():
	while true:
		randomize()
		
		var p = utils.choose(powerups).instance()
		extents = utils.get_extents(p.get_node("sprite"), true)
		var pos = Vector2(rand_range(extents.x, screen_size.x - extents.x), -extents.y)
		p.set_pos(pos)
		container.call_deferred("add_child", p)
		yield(utils.create_timer(rand_range(10, 15), self), "timeout")
	pass
