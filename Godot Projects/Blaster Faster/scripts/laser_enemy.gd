# script laser_enemy

extends "res://scripts/laser.gd"

func _ready():
	add_to_group(game.GROUP_BULLET)
	connect("area_enter", self, "_on_area_enter")
	audio_player.play("laser_enemy")
	pass

func _on_area_enter(other):
	if other.is_in_group(game.GROUP_PLAYER):
		other.armor -= 1
		create_flare()
		utils.remote_call("camera", "shake", 3, 0.13)
		queue_free()
	elif other.is_in_group(game.GROUP_BULLET):
		create_flare()
		utils.remote_call("camera", "shake", 3, 0.13)
		queue_free()
	pass
