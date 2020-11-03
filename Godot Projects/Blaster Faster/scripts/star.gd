# script star

extends Sprite

export var velocity = Vector2()

func _ready():
	set_process(true)
	pass

func _process(delta):
	translate(velocity * delta)
	
	if get_pos().y >= utils.view_size.y:
		set_pos(Vector2(0, -180))
	pass
