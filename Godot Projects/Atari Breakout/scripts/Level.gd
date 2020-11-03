extends Node

onready var main = get_node("/root/main")

func _ready():
	set_process(true)
	
func _process(delta):
	if get_child_count() == 0:
		main.change_level()
		queue_free()
