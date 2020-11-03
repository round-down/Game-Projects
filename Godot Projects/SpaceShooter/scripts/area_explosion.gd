extends Area2D

onready var anim_sprite = get_node("anim sprite")

func _on_area_explosion_body_enter( body ):
	if body.get_groups().has("asteroids"):
		body.explode(Vector2(1, 1), false)
		queue_free()

func _on_area_explosion_area_enter( area ):
	if area.get_groups().has("enemies"):
		area.damage(global.cannon_damage, true)
