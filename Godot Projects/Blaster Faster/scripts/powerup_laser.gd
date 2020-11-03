# script powerup_laser

extends "res://scripts/powerup.gd"

func _ready():
	connect("area_enter", self, "_on_area_enter")
	pass

func _on_area_enter(other):
	if other.is_in_group(game.GROUP_PLAYER):
		other.call_deferred("emit_signal", "double_shoot")
		audio_player.play("powerup_laser")
		queue_free()
	pass
