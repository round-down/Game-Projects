extends Particles2D


func _ready():
	if global.hide_bg == false:
		set_emitting(true)
	elif global.hide_bg == true:
		set_emitting(false)
	pass