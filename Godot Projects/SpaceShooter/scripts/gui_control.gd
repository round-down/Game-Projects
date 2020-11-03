extends TextureFrame

var val = 0

var touch_index = -1
var minXY
var maxXY
var isVertical

var joystick
var valOut

func _ready():
	set_process_input(true)
	joystick = get_node("Joystick")
	isVertical = (get_name().left(1) == "V")
	
	if isVertical: # Check if Vertical Joystick
		minXY = Vector2(floor((float(get_size().x))/2.0), 0)
		maxXY = Vector2(floor((float(get_size().x))/2.0), get_size().y - 1)
		valOut = get_node("valV")
	else: # isVertical returns False and therefore it is the Horizonal Joystick
		minXY = Vector2(0,floor((float(get_size().y))/2.0))
		maxXY = Vector2(get_size().x - 1, floor((float(get_size().y))/2.0))
		valOut = get_node("valH")
		
func _input(ev):
	if is_visible() and ((ev.type == InputEvent.SCREEN_TOUCH) or (ev.type == InputEvent.SCREEN_DRAG)):
		if ev.type == InputEvent.SCREEN_TOUCH:
			if ev.pressed:
				# define some variables to keep track of position and size of texture
				var pos = get_pos()
				var size = get_size()
				# check if touch was inside control
				if (ev.pos.x >= pos.x) and (ev.pos.x <= pos.x + size.x) and \
				   (ev.pos.y >= pos.y) and (ev.pos.y <= pos.y + size.y):
					# save touch index to track "DRAG" events
					touch_index = ev.index
					ev.pos.x = clamp(ev.pos.x - pos.x, minXY.x, maxXY.x)
					ev.pos.y = clamp(ev.pos.y - pos.y, minXY.y, maxXY.y)
					set_val(ev)
			else: # released
				if touch_index == ev.index:
					touch_index = -1
					reset_val(ev)
					
		if ev.type == InputEvent.SCREEN_DRAG:
			var pos = get_pos()
			var size = get_size()
			if (ev.index == touch_index): # allow drag outside control
				ev.pos.x = clamp(ev.pos.x - pos.x, minXY.x, maxXY.x)
				ev.pos.y = clamp(ev.pos.y - pos.y, minXY.y, maxXY.y)
				set_val(ev)
				
# reset joystick to center on touch release
func reset_val(ev):
	ev.pos.x = (maxXY.x - minXY.x + 1)/2 + minXY.x
	ev.pos.y = (maxXY.y - minXY.y + 1)/2 + minXY.y
	set_val(ev)

# set value based on control-relative event coordinates(also suitable for mouse coords)
func set_val(ev):
	if isVertical:
		val = clamp((ev.pos.y - (get_size().y/2.0)) / (get_size().y/-2.0), -1, 1)
	else:
		val = clamp((ev.pos.x - (get_size().x/2.0)) / (get_size().x/-2.0), -1, 1)
	# move joystick control
	joystick.set_pos(Vector2(ev.pos.x - (joystick.get_size().x/2), ev.pos.y - (joystick.get_size().y/2)))
	valOut.set_text(str(val))









