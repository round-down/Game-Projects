extends Area2D

var explosion = preload("res://scenes/area_explosion.tscn")
var speed = rand_range(100, 350)
var vel = Vector2()

func _ready():
	randomize()
	set_fixed_process(true)

func start_at(dir, pos):
	set_rot(dir)
	set_pos(pos)
	vel = Vector2(speed, 0).rotated(dir + PI/2)

func _fixed_process(delta):
	set_pos(get_pos() + vel * delta)

func _on_exit_screen():
	queue_free()

func explode():
	var expl = explosion.instance()
	get_parent().add_child(expl)
	expl.set_pos(get_pos())
	expl.set_scale(Vector2(2,2))
	expl.anim_sprite.set_animation("sonic")
	expl.anim_sprite.play()
	sounds.play("sonic")

func _on_cannon_body_enter( body ):
	if body.get_groups().has("asteroids"):
		explode()
		queue_free()
		body.explode(vel.normalized(), false)

func _on_cannon_area_enter( area ):
	if area.get_groups().has("enemies"):
		explode()
		get_node("/root/main").explode_enemy(area.get_pos(), false)
		area.queue_free()
		queue_free()
