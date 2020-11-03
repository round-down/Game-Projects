extends Particles2D

onready var timer = get_node("timer")

func _ready():
	set_emitting(true)
	timer.start()
	yield(timer,"timeout")
	queue_free()
	pass
