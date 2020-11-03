extends Node

onready var score_lbl = get_node("score lbl")

func _ready():
	sounds.play("gameover")
	score_lbl.set_text("Score: %d" % global.score)

func _on_play_pressed():
	sounds.play("on")
	global.restart()

func _on_quit_pressed():
	sounds.play("off")
	get_tree().quit()
