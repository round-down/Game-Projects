# script: input

extends Node

var keyboard setget , _get_keyboard
var mouse    setget , _get_mouse

var keyboard_idle = Keyboard.new()
var mouse_idle    = Mouse.new()

var keyboard_fixed = Keyboard.new()
var mouse_fixed    = Mouse.new()

var is_idle_frame = true

onready var root_node = get_tree().get_root()

func _ready():
	set_process(true)
	set_fixed_process(true)
	set_process_input(true)
	pass

func _notification(what):
	if what == NOTIFICATION_PROCESS:
		is_idle_frame = true
	elif what == NOTIFICATION_FIXED_PROCESS:
		is_idle_frame = false
	pass

func _process(delta):
	keyboard_idle.update()
	mouse_idle.update(delta)
	pass

func _fixed_process(delta):
	keyboard_fixed.update()
	mouse_fixed.update(delta)
	pass

func _input(ev):
	# mouse wheel are just detected in _input callback
	# so they'll get simulated from here
	if ev.type != InputEvent.MOUSE_BUTTON or !ev.is_pressed() or ev.is_echo():
		return
	
	if (ev.button_index == BUTTON_WHEEL_UP):
		_press_mouse_btn("wheel_up")
	elif (ev.button_index == BUTTON_WHEEL_DOWN):
		_press_mouse_btn("wheel_down")
	elif (ev.button_index == BUTTON_WHEEL_LEFT):
		_press_mouse_btn("wheel_left")
	elif (ev.button_index == BUTTON_WHEEL_RIGHT):
		_press_mouse_btn("wheel_right")
	pass

func _get_keyboard():
	if is_idle_frame:
		return keyboard_idle
	else:
		return keyboard_fixed
	pass

func _get_mouse():
	if is_idle_frame:
		return mouse_idle
	else:
		return mouse_fixed
	pass

# ---------------------------------------------------------------------
# Keyboard
# ---------------------------------------------------------------------

class Keyboard:
	var keys = {
		"a": Key.new(KEY_A),
		"b": Key.new(KEY_B),
		"c": Key.new(KEY_C),
		"d": Key.new(KEY_D),
		"e": Key.new(KEY_E),
		"f": Key.new(KEY_F),
		"g": Key.new(KEY_G),
		"h": Key.new(KEY_H),
		"i": Key.new(KEY_I),
		"j": Key.new(KEY_J),
		"k": Key.new(KEY_K),
		"l": Key.new(KEY_L),
		"m": Key.new(KEY_M),
		"n": Key.new(KEY_N),
		"o": Key.new(KEY_O),
		"p": Key.new(KEY_P),
		"q": Key.new(KEY_Q),
		"r": Key.new(KEY_R),
		"s": Key.new(KEY_S),
		"t": Key.new(KEY_T),
		"u": Key.new(KEY_U),
		"v": Key.new(KEY_V),
		"w": Key.new(KEY_W),
		"x": Key.new(KEY_X),
		"y": Key.new(KEY_Y),
		"z": Key.new(KEY_Z),
		"0": Key.new(KEY_0),
		"1": Key.new(KEY_1),
		"2": Key.new(KEY_2),
		"3": Key.new(KEY_3),
		"4": Key.new(KEY_4),
		"5": Key.new(KEY_5),
		"6": Key.new(KEY_6),
		"7": Key.new(KEY_7),
		"8": Key.new(KEY_8),
		"9": Key.new(KEY_9),
		"left"     : Key.new(KEY_LEFT     ),
		"right"    : Key.new(KEY_RIGHT    ),
		"up"       : Key.new(KEY_UP       ),
		"down"     : Key.new(KEY_DOWN     ),
		"space"    : Key.new(KEY_SPACE    ),
		"tab"      : Key.new(KEY_TAB      ),
		"backtab"  : Key.new(KEY_BACKTAB  ),
		"backspace": Key.new(KEY_BACKSPACE),
		"return"   : Key.new(KEY_RETURN   ),
		"enter"    : Key.new(KEY_ENTER    ),
		"insert"   : Key.new(KEY_INSERT   ),
		"delete"   : Key.new(KEY_DELETE   ),
		"shift"    : Key.new(KEY_SHIFT    ),
		"control"  : Key.new(KEY_CONTROL  ),
		"meta"     : Key.new(KEY_META     ),
		"alt"      : Key.new(KEY_ALT      )
	}
	
	func _init():
		pass
	
	func update(ev = null):
		for key in keys:
			keys[key].update()
		pass
	
	func is_key_pressed(key):
		return keys[key].is_pressed()
		pass
	
	func is_key_released(key):
		return keys[key].is_released()
		pass
	
	func is_key_down(key):
		return keys[key].is_down()
		pass
	
	func is_key_up(key):
		return keys[key].is_up()
		pass
	
	# ---------------------------------------------------------------------
	# Key
	# ---------------------------------------------------------------------
	
	class Key:
		var scancode
		var is_pressed  = false
		var was_pressed = false
		
		var simulate_press = false
		
		signal pressed
		signal released
		
		func _init(scancode):
			self.scancode = scancode
			pass
		
		func update():
			was_pressed = is_pressed
			is_pressed  = Input.is_key_pressed(scancode)
			
			if simulate_press : is_pressed = true
			
			if is_pressed() : emit_signal("pressed" )
			if is_released(): emit_signal("released")
			pass
		
		func is_pressed():
			return (not was_pressed and is_pressed)
			pass
		
		func is_released():
			return (was_pressed and not is_pressed)
			pass
		
		func is_down():
			return (was_pressed and is_pressed)
			pass
		
		func is_up():
			return (not was_pressed and not is_pressed)
			pass
		
		func press():
			simulate_press = true
			pass
		
		func release():
			simulate_press = false
			pass
		
		# end class Key
	
	# end class Keyboard

# ---------------------------------------------------------------------
# Mouse
# ---------------------------------------------------------------------

class Mouse extends Node:
	var pos = Vector2()
	var previous_pos = Vector2()
	var relative_pos = Vector2()
	var velocity     = Vector2()
	var buttons      = {
		"left"        : MouseButton.new(BUTTON_LEFT       ),
		"right"       : MouseButton.new(BUTTON_RIGHT      ),
		"middle"      : MouseButton.new(BUTTON_MIDDLE     ),
		"wheel_up"    : MouseButton.new(BUTTON_WHEEL_UP   ),
		"wheel_down"  : MouseButton.new(BUTTON_WHEEL_DOWN ),
		"wheel_left"  : MouseButton.new(BUTTON_WHEEL_LEFT ),
		"wheel_right" : MouseButton.new(BUTTON_WHEEL_RIGHT),
	}
	
	func update(delta):
		for button in buttons:
			buttons[button].update()
		
		previous_pos = pos
		pos          = input.root_node.get_mouse_pos()
		relative_pos = pos - previous_pos
		velocity     = relative_pos / delta
		pass
	
	func is_btn_pressed(button):
		return buttons[button].is_pressed()
		pass
	
	func is_btn_released(button):
		return buttons[button].is_released()
		pass
	
	func is_btn_down(button):
		return buttons[button].is_down()
		pass
	
	func is_btn_up(button):
		return buttons[button].is_up()
		pass
	
	# ---------------------------------------------------------------------
	# MouseButton
	# ---------------------------------------------------------------------
	
	class MouseButton:
		var index
		var is_pressed  = false
		var was_pressed = false
		
		var simulate_press = false
		
		signal pressed
		signal released
		
		func _init(index):
			self.index = index
			pass
		
		func update():
			was_pressed = is_pressed
			is_pressed  = Input.is_mouse_button_pressed(index)
			
			if simulate_press : is_pressed = true
			
			if is_pressed() : emit_signal("pressed" )
			if is_released(): emit_signal("released")
			pass
		
		func is_pressed():
			return (not was_pressed and is_pressed)
			pass
		
		func is_released():
			return (was_pressed and not is_pressed)
			pass
		
		func is_down():
			return (was_pressed and is_pressed)
			pass
		
		func is_up():
			return (not was_pressed and not is_pressed)
			pass
		
		func press():
			simulate_press = true
			pass
		
		func release():
			simulate_press = false
			pass
		
		# end class MouseButton
	
	# end class Mouse

