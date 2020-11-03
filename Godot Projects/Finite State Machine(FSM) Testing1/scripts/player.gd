# SCRIPT: player

extends KinematicBody2D

onready var ground_ray = get_node("ground ray")
onready var sprite = get_node("sprite")
onready var state_lbl = get_node("state")

var screensize = Vector2(Globals.get("display/width"),Globals.get("display/height"))

var acc = Vector2()
var vel = Vector2()

const ACCEL = 1500
const MAX_SPEED = 500
const FRICTION = -700
const GRAVITY = 4000
const JUMP_SPEED = -1400
const MIN_JUMP = -500

onready var state = IdleState.new(self)
enum States { IDLE, RUNNING, JUMPING }

func _ready():
	set_fixed_process(true)
	set_process_unhandled_input(true)
	
func _fixed_process(delta):
	# physics calculations fixed every frame because player is a physics body type 'Kinematic2D'
	# set animation flip horizontal. Gets used globally, so writing it for each state isn't nesscessary
	if vel.x > 0:
		sprite.set_flip_h(false)
	elif vel.x < 0:
		sprite.set_flip_h(true)
	
	# physics based movement
	acc.y = GRAVITY
	acc.x = Input.is_action_pressed("ui_right") - Input.is_action_pressed("ui_left")
	acc.x *= ACCEL
	if acc.x == 0:
		acc.x = vel.x * FRICTION * delta
		
	vel += acc * delta
	vel.x = clamp(vel.x, -MAX_SPEED, MAX_SPEED)
	
	var motion = move(vel * delta)
	if is_colliding():
		var n = get_collision_normal()
		motion = n.slide(motion)
		vel = n.slide(vel)
		move(motion)
	if abs(vel.x) < 10:
		vel.x = 0
		
	state.update(delta)# calls on the current state's update method and passes in delta
	
func _unhandled_input(event):
	# handles all unhandled input events
	if event.is_action_pressed("ui_select") and ground_ray.is_colliding():
		vel.y = JUMP_SPEED
	if event.is_action_released("ui_select"):
		vel.y = clamp(vel.y, MIN_JUMP, vel.y)
	
	state.input(event)# calls on the current states input method and passes in event



func set_state(new_state):
	# set the new state you want to enter
	state.exit()
	state = new_state
	
	if new_state == IDLE:
		state = IdleState.new(self)
	elif new_state == RUNNING:
		state = RunningState.new(self)
	elif new_state == JUMPING:
		state = JumpingState.new(self)
	
func get_state():
	# returns the state reference to other scripts if needed
	if state extends IdleState:
		return IDLE
	elif state extends RunningState:
		return RUNNING
	elif state extends JumpingState:
		return JUMPING



# class IdleState ************************************************************************************
class IdleState:
	var p
	
	func _init(p):
		# ready function when the state is initialized
		self.p = p
		p.vel.y = 0
		p.vel.x = 0
		p.sprite.set_animation("idle")
		p.state_lbl.set_text("IDLE")
		pass
	
	func update(delta):
		# fixed process update every frame
		if Input.is_action_pressed("ui_right") or Input.is_action_pressed("ui_left"):
			p.set_state(RUNNING)
		elif Input.is_action_pressed("ui_select"):
			p.set_state(JUMPING)
		pass
	
	func input(event):
		# unhandled input event every frame
		pass
	
	func exit():
		# clean up anything before exiting the state
		pass


# class RunningState ************************************************************************************
class RunningState:
	var p
	
	func _init(p):
		# ready function when the state is initialized
		self.p = p
		p.sprite.set_animation("running")
		p.state_lbl.set_text("RUNNING")
		pass
	
	func update(delta):
		# fixed process update every frame
		if p.vel == Vector2(0,0):
			p.set_state(IDLE)
		
		# if player is falling off the map, reset positon to origin
		if p.get_pos().y > p.screensize.y + 450:
			p.set_pos(Vector2(360,175))
			p.vel.y = 0
	
	func input(event):
		# unhandled input event every frame
		if event.is_action_pressed("ui_select"):
			p.set_state(JUMPING)
		pass
	
	func exit():
		# clean up anything before exiting the state
		pass


# class JumpingState ************************************************************************************
class JumpingState:
	var p
	
	func _init(p):
		# ready function when the state is initialized
		self.p = p
		p.sprite.set_animation("jumping")
		p.sprite.set_frame(0)
		p.state_lbl.set_text("JUMPING")
		pass
	
	func update(delta):
		# fixed process update every frame
		if p.vel.y > 0:# if moving upwards
			p.sprite.set_frame(1)
		
		if p.vel.y == 0:# if touching a platform and not jumping
			p.set_state(RUNNING)# Why RUNNING? Because it has more realistic effects when landing
		
		# if player is falling off the map, reset positon to origin
		if p.get_pos().y > p.screensize.y + 450:
			p.set_pos(Vector2(360,175))
			p.vel.y = 0
		pass
	
	func input(event):
		# unhandled input event every frame
		pass
	
	func exit():
		# clean up anything before exiting the state
		pass
