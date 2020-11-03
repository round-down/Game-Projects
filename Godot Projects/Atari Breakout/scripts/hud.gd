extends CanvasLayer

# pause stuff
onready var pause_btn = get_node("pause btn")
onready var pause_popup = get_node("pause popup")
onready var quit_btn = get_node("quit btn")
onready var quit_popup = get_node("quit popup")
# score
onready var score_lbl = get_node("score lbl")
# level notifier
onready var level_lbl = get_node("level lbl")
# mute sounds button
onready var mute_sounds_btn = get_node("mute sounds btn")
# restart button
onready var restart_btn = get_node("restart btn")

# saved positions
onready var mute_sounds_btn_pos = mute_sounds_btn.get_pos()
onready var pause_btn_pos = pause_btn.get_pos()

func _ready():
	pause_popup.hide()
	quit_popup.hide()
	
func set_pause(boolean):
	global.paused = boolean
	# set pause to true if false, or false if true
	get_tree().set_pause(boolean)
	# set pause btn opacity for better view and show pause popup
	if global.paused == true:
		sounds.play("on")
		level_lbl.hide()
		pause_popup.show()
		quit_btn.show()
		restart_btn.show()
	else:
		sounds.play("off")
		quit_btn.hide()
		restart_btn.hide()
		quit_popup.hide()
		pause_popup.hide()
		level_lbl.show()

func _on_quit_btn_pressed():
	sounds.play("on")
	quit_btn.set_disabled(true)
	pause_btn.set_disabled(true)
	pause_popup.hide()
	quit_popup.show()

func _on_quit_popup_yes_btn_pressed():
	sounds.play("on")
	get_tree().quit()

func _on_quit_popup_no_btn_pressed():
	sounds.play("off")
	quit_popup.hide()
	quit_btn.set_disabled(false)
	pause_btn.set_disabled(false)
	pause_popup.show()

func _on_mute_sounds_btn_toggled( pressed ):
	if pressed == true:
		sounds.set_default_volume(0)
	else:
		sounds.set_default_volume(1)

func _on_restart_btn_pressed():
	sounds.play("on")
	global.restart()
