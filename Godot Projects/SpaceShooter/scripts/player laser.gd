extends Area2D

onready var player = get_node("/root/main/player")

func start_at(dir, pos):
	set_rot(dir)
	set_pos(pos)

func _on_laser_body_enter( body ):
	if body.get_groups().has("asteroids"):
		body.explode(Vector2(1, -1).normalized(), true)

func _on_laser_area_enter( area ):
	if area.get_groups().has("enemies"):
		area.damage(global.bullet_damage, true)