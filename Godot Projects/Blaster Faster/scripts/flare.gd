# script flare

extends Sprite

func _ready():
	yield(get_node("anim"), "finished")
	queue_free()
	pass
