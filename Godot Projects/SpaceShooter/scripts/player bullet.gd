extends Area2D

export var speed = 1000

var vel = Vector2()

func _ready():
	set_fixed_process(true)

func start_at(dir, pos):
	set_rot(dir)
	set_pos(pos)
	vel = Vector2(speed, 0).rotated(dir + PI/2)

func _fixed_process(delta):
	set_pos(get_pos() + vel * delta)

func _on_exit_screen():
	queue_free()

func _on_player_bullet_body_enter( body ):
	if body.get_groups().has("asteroids"):
		queue_free()
		body.explode(vel.normalized(), true)

func _on_player_bullet_area_enter( area ):
	if area.get_groups().has("enemies"):
		queue_free()
		area.damage(global.bullet_damage, true)
