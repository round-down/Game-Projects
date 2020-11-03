# script laser_ship

extends "res://scripts/laser.gd"

func _ready():
	connect("area_enter", self, "_on_area_enter")
	audio_player.play("laser_ship")
	pass

func _on_area_enter(other):
	if other.is_in_group(game.GROUP_ENEMIES):
		other.armor -= 1
		create_flare()
		utils.remote_call("camera", "shake", 1, 0.13)
		queue_free()
	pass
