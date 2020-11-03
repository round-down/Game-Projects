# script audio_player

extends Node

onready var sample_player = get_node("sample_player")
onready var stream_player = get_node("stream_player")

onready var btn_sound = get_node("hud/btn_sound")
onready var btn_music = get_node("hud/btn_music")

func _ready():
	btn_sound.connect("toggled", self, "_on_btn_sounds_toggled")
	btn_music.connect("toggled", self, "_on_btn_music_toggled")
	pass

func _on_ship_exit_tree():
	btn_sound.show()
	btn_music.show()
	pass

func play(sample_name):
	sample_player.play(sample_name)
	pass

func hide_buttons(boolean):
	if boolean == true:
		btn_sound.hide()
		btn_music.hide()
	else:
		btn_sound.show()
		btn_music.show()
	pass

func _on_btn_music_toggled(pressed):
	if pressed == true:
		stream_player.set_volume(0.0)
	else:
		stream_player.set_volume(1.0)
	pass

func _on_btn_sounds_toggled(pressed):
	if pressed == true:
		sample_player.set_default_volume(0.0)
	else:
		sample_player.set_default_volume(1.0)
	pass
