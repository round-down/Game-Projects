# script powerup_armor

extends "res://scripts/powerup.gd"

func _ready():
	connect("area_enter", self, "_on_area_enter")
	pass

func _on_area_enter(other):
	if other.is_in_group(game.GROUP_PLAYER):
		other.armor += 1
		audio_player.play("powerup_armor")
		queue_free()
	pass
