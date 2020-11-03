# script: tweener

extends Node

var tweens = []

func _ready():
	set_process(true)
	pass

func _process(delta):
	for tween in tweens:
		tween.update(delta)
	pass

func create():
	var tween = Tween.new()
	tweens.push_back(tween)
	return tween
	pass

func destroy(tween):
	var index = tweens.find(tween)
	if index != -1: tweens.remove(index)
	pass

# ---------------------------------------------------------------------
# Tween
# ---------------------------------------------------------------------

class Tween:
	var name      = "noname"
	var from      = .0
	var to        = .0
	var change    = .0 setget , _get_change
	var amplitud  = .0
	var period    = .0
	var overshoot = .0
	var time      = .0
	var duration  = .0
	var ease_func = "linear"
	var value     = .0
	var target    = null
	var property  = null
	var function  = null
	
	var state setget _set_state, _get_state
	
	const STATE_PLAYING = 0
	const STATE_PAUSED  = 1
	const STATE_DONE    = 2
	
	signal done
	
	func _init():
		self.state = STATE_PAUSED
		pass
	
	func update(delta):
		state.update(delta)
		pass
	
	func play():
		self.state = STATE_PLAYING
		pass
	
	func pause():
		self.state = STATE_PAUSED
		pass
	
	func reset():
		time = 0
		pass
	
	func is_playing():
		return self.state == STATE_PLAYING
		pass
	
	func is_paused():
		return self.state == STATE_PAUSED
		pass
	
	func is_done():
		return self.state == STATE_DONE
		pass
	
	func _set_state(new_state):
		if new_state == STATE_PLAYING:
			state = PlayingState.new(self)
		if new_state == STATE_PAUSED:
			state = PausedState.new(self)
		if new_state == STATE_DONE:
			state = DoneState.new(self)
		pass
	
	func _get_state():
		if state extends PlayingState:
			return STATE_PLAYING
		if state extends PausedState:
			return STATE_PAUSED
		if state extends DoneState:
			return STATE_DONE
		pass
	
	func _get_change():
		return to - from
		pass
	
	# ---------------------------------------------------------------------
	# State
	# ---------------------------------------------------------------------
	
	class State:
		var tween
		
		func _init(tween):
			self.tween = tween
			pass
		
		func update(delta):
			pass
		
	# end class State
	
	# ---------------------------------------------------------------------
	# PlayingState
	# ---------------------------------------------------------------------
	
	class PlayingState extends State:
		
		func _init(tween).(tween):
			pass
		
		func update(delta):
			tween.time += delta
			tween.time  = min(tween.time, tween.duration)
			
			tween.value = tweener.do_easing(tween.ease_func, tween.time, tween.from, tween.change, tween.duration, tween.amplitud, tween.period, tween.overshoot)
			
			if tween.target:
				if tween.property: tween.target.set (tween.property, tween.value)
				if tween.function: tween.target.call(tween.function, tween.value)
			
			if tween.time == tween.duration:
				tween.state = tween.STATE_DONE
			pass
		
	# end class PlayingState
	
	# ---------------------------------------------------------------------
	# PausedState
	# ---------------------------------------------------------------------
	
	class PausedState extends State:
		
		func _init(tween).(tween):
			pass
		
	# end class PausedState
	
	# ---------------------------------------------------------------------
	# DoneState
	# ---------------------------------------------------------------------
	
	class DoneState extends State:
		
		func _init(tween).(tween):
			yield(tweener.get_tree(), "idle_frame")
			tween.emit_signal("done")
			pass
		
	# end class DoneState
	
# end class Tween


# ---------------------------------------------------------------------
# Do easing
# ---------------------------------------------------------------------

func do_easing(ease_func, time, from, change, duration, amplitud, period, overshoot):
	if typeof(change) == TYPE_REAL:
		if ease_func.begins_with("back")   : return call(str(ease_func), time, from, change, duration, overshoot)
		if ease_func.begins_with("elastic"): return call(str(ease_func), time, from, change, duration, amplitud, period)
		return call(str(ease_func), time, from, change, duration)
	if typeof(change) == TYPE_VECTOR2:
		var vector = Vector2()
		vector.x = do_easing(ease_func, time, from.x, change.x, duration, amplitud, period, overshoot)
		vector.y = do_easing(ease_func, time, from.y, change.y, duration, amplitud, period, overshoot)
		return vector
	if typeof(change) == TYPE_COLOR:
		var color = Color()
		color.r = do_easing(ease_func, time, from.r, change.r, duration, amplitud, period, overshoot)
		color.g = do_easing(ease_func, time, from.g, change.g, duration, amplitud, period, overshoot)
		color.b = do_easing(ease_func, time, from.b, change.b, duration, amplitud, period, overshoot)
		color.a = do_easing(ease_func, time, from.a, change.a, duration, amplitud, period, overshoot)
		return color
	pass

# ---------------------------------------------------------------------
# Ease Functions
# ---------------------------------------------------------------------

# ---------------
# LINEAR
# ---------------
func linear(time, from, change, duration):
	return change * time / duration + from
	pass

# ---------------
# QUAD
# ---------------
func quad_in(time, from, change, duration):
	var percent = time / duration
	return change * pow(percent, 2) + from
	pass

func quad_out(time, from, change, duration):
	var percent = time / duration
	return -change * percent * (percent - 2) + from
	pass

func quad_inout(time, from, change, duration):
	var percent = time / duration * 2.0
	if percent < 1:
		return change / 2.0 * pow(percent, 2) + from
	else:
		return -change / 2.0 * ((percent - 1) * (percent - 3) - 1) + from
	pass

# ---------------
# CUBIC
# ---------------
func cubic_in(time, from, change, duration):
	var percent = time / duration
	return change * pow(percent, 3) + from
	pass

func cubic_out(time, from, change, duration):
	var percent = time / duration - 1
	return change * (pow(percent, 3) + 1) + from
	pass

func cubic_inout(time, from, change, duration):
	var percent = time / duration * 2
	if percent < 1:
		return change / 2.0 * percent * percent * percent + from
	else:
		percent = percent - 2
		return change / 2.0 * (percent * percent * percent + 2) + from
	pass

# ---------------
# QUART
# ---------------
func quart_in(time, from, change, duration):
	var percent = time / duration
	return change * pow(percent, 4) + from
	pass

func quart_out(time, from, change, duration):
	var percent = time / duration - 1
	return -change * (pow(percent, 4) - 1) + from
	pass

func quart_inout(time, from, change, duration):
	var percent = time / duration * 2
	if percent < 1:
		return change / 2.0 * pow(percent, 4) + from
	else:
		percent = percent - 2
		return -change / 2.0 * (pow(percent, 4) - 2) + from
	pass

# ---------------
# QUINT
# ---------------
func quint_in(time, from, change, duration):
	var percent = time / duration
	return change * pow(percent, 5) + from
	pass

func quint_out(time, from, change, duration):
	var percent = time / duration - 1
	return change * (pow(percent, 5) + 1) + from
	pass

func quint_inout(time, from, change, duration):
	var percent = time / duration * 2
	if percent < 1:
		return change / 2.0 * pow(percent, 5) + from
	else:
		percent = percent - 2
		return change / 2.0 * (pow(percent, 5) + 2) + from
	pass

# ---------------
# SINE
# ---------------
func sine_in(time, from, change, duration):
	return -change * cos(time / duration * (PI / 2.0)) + change + from
	pass

func sine_out(time, from, change, duration):
	return change * sin(time / duration * (PI / 2.0)) + from
	pass

func sine_inout(time, from, change, duration):
	return -change / 2.0 * (cos(PI * time / duration) - 1) + from
	pass

# ---------------
# EXPO
# ---------------
func expo_in(time, from, change, duration):
	if time == 0:
		return from
	else:
		return change * pow(2, 10 * (time / duration - 1.0)) + from - change * 0.001
	pass

func expo_out(time, from, change, duration):
	if time == duration:
		return from + change
	else:
		return change * 1.001 * (-pow(2, -10 * time / duration) + 1) + from
	pass

func expo_inout(time, from, change, duration):
	if time == 0:        return from
	if time == duration: return from + change
	var percent = time / duration * 2
	if percent < 1:
		return change / 2 * pow(2, 10 * (percent - 1)) + from - change * 0.0005
	else:
		percent = percent - 1
		return change / 2 * 1.0005 * (-pow(2, -10 * percent) + 2) + from
	pass

# ---------------
# CIRC
# ---------------
func circ_in(time, from, change, duration):
	var percent = time / duration
	return (-change * (sqrt(1 - pow(percent, 2)) - 1) + from)
	pass

func circ_out(time, from, change, duration):
	var percent = time / duration - 1.0
	return (change * sqrt(1 - pow(percent, 2)) + from)
	pass

func circ_inout(time, from, change, duration):
	var percent = time / duration * 2.0
	if percent < 1:
		return -change / 2 * (sqrt(1 - percent * percent) - 1) + from
	else:
		percent = percent - 2
		return change / 2 * (sqrt(1 - percent * percent) + 1) + from
	pass

# ---------------
# ELASTIC
# ---------------
func elastic_in(time, from, change, duration, amplitud, period):
	if time == 0: return from
	
	var percent = time / duration

	if percent == 1: return from + change

	if not period: period = duration * 0.3

	var s

	if not amplitud or amplitud < abs(change):
		amplitud = change
		s = period / 4
	else:
		s = period / (2 * PI) * asin(change/amplitud)

	percent = percent - 1

	return -(amplitud * pow(2, 10 * percent) * sin((percent * duration - s) * (2 * PI) / period)) + from
	pass

func elastic_out(time, from, change, duration, amplitud, period):
	if time == 0: return from

	var percent = time / duration

	if percent == 1: return from + change

	if not period: period = duration * 0.3

	var s

	if not amplitud or amplitud < abs(change):
		amplitud = change
		s = period / 4
	else:
		s = period / (2 * PI) * asin(change/amplitud)

	return amplitud * pow(2, -10 * percent) * sin((percent * duration - s) * (2 * PI) / period) + change + from
	pass

func elastic_inout(time, from, change, duration, amplitud, period):
	if time == 0: return from
	
	var percent = time / duration * 2.0
	
	if percent == 2: return from + change
	
	if not period: period = duration * (0.3 * 1.5)
	if not amplitud: amplitud = 0
	
	var s
	
	if not amplitud or amplitud < abs(change):
		amplitud = change
		s = period / 4.0
	else:
		s = period / (2.0 * PI) * asin(change / amplitud)
	
	if percent < 1:
		percent = percent - 1
		return -0.5 * (amplitud * pow(2.0, 10.0 * percent) * sin((percent * duration - s) * (2.0 * PI) / period)) + from
	else:
		percent = percent - 1
		return amplitud * pow(2.0, -10.0 * percent) * sin((percent * duration - s) * (2.0 * PI) / period ) * 0.5 + change + from
	pass

# ---------------
# BACK
# ---------------
func back_in(time, from, change, duration, overshoot):
	if not overshoot: overshoot = 1.70158
	var percent = time / duration
	return change * percent * percent * ((overshoot + 1) * percent - overshoot) + from
	pass

func back_out(time, from, change, duration, overshoot):
	if not overshoot: overshoot = 1.70158
	var percent = time / duration - 1
	return change * (percent * percent * ((overshoot + 1) * percent + overshoot) + 1) + from
	pass

func back_inout(time, from, change, duration, overshoot):
	return
	if not overshoot: overshoot = 1.70158
	overshoot = overshoot * 1.525
	var percent = time / duration * 2.0
	if percent < 1:
		return change / 2.0 * (percent * percent * ((overshoot + 1) * percent - overshoot)) + from
	else:
		percent = percent - 2
		return change / 2.0 * (percent * percent * ((overshoot + 1) * percent + overshoot) + 2) + from
	pass

# ---------------
# BOUNCE
# ---------------
func bounce_in(time, from, change, duration):
	return change - bounce_out(duration - time, 0, change, duration) + from
	pass

func bounce_out(time, from, change, duration):
	var percent = time / duration
	if percent < 1 / 2.75:
		return change * ((7.5625) * percent * percent) + from
	elif percent < 2 / 2.75:
		percent = percent - (1.5 / 2.75)
		return change * ((7.5625) * percent * percent + 0.75) + from
	elif percent < 2.5 / 2.75:
		percent = percent - (2.25 / 2.75)
		return change * ((7.5625) * percent * percent + 0.9375) + from
	else:
		percent = percent - (2.625 / 2.75)
		return change * ((7.5625) * percent * percent + 0.984375) + from
	pass

func bounce_inout(time, from, change, duration):
	if time < duration / 2.0:
		return bounce_in(time * 2, 0, change, duration) * 0.5 + from
	else:
		return bounce_out(time * 2 - duration, 0, change, duration) * 0.5 + change * .5 + from
	pass

