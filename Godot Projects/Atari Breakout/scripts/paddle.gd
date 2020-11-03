extends KinematicBody2D

onready var middle = get_node("middle")
onready var anim = get_node("anim")
var extents

func _ready():
	global.set_extents(self)
	set_process(true)
	
func _process(delta):
	# tracking mouse
	if get_global_mouse_pos().y < global.screensize.y - 130:
		var motion = (get_global_mouse_pos().x - get_pos().x) * 0.3
		translate(Vector2(motion, 0))
		
		# clamping to view
		var pos = get_pos()
		pos.x = clamp(pos.x, extents.x, global.screensize.x - extents.x)
		set_pos(pos)