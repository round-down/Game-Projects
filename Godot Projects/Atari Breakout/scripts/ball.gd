extends RigidBody2D

onready var main = get_node("/root/main")
onready var anim = get_node("anim")
onready var score_lbl = get_node("/root/hud/score lbl")


func _ready():
	randomize()
	set_linear_velocity(global.choose(global.start_direction))
	set_fixed_process(true)
	
func _fixed_process(delta):
	if get_pos().y > global.screensize.y / 1.75 or get_pos().y < -10:
		global.game_over = true

func _on_ball_body_enter( body ):
	if body.is_in_group("BRICKS"):
		sounds.play("hit_brick")
		body.queue_free()
		global.score += 5
	elif body.get_name() == "paddle":
		sounds.play("hit_paddle")
		body.anim.play("shake")
		self.anim.play("squish_bottom")
		var speed = get_linear_velocity().length()
		var direction = get_pos() - body.middle.get_global_pos()
		var velocity = direction.normalized() * min(speed + global.SPEED_UP, global.MAX_SPEED)
		set_linear_velocity(velocity)
	elif body.get_name() in ["top_wall", "left_wall", "right_wall"]:
		sounds.play("hit_wall")
		if body.get_name() == "left_wall":
			self.anim.play("squish_left")
		elif body.get_name() == "right_wall":
			self.anim.play("squish_right")
		elif body.get_name() == "top_wall":
			self.anim.play("squish_top")
