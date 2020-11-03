extends CanvasLayer

onready var message = get_node("message")
onready var message_timer = get_node("message timer")
onready var player = get_node("/root/main/player")
onready var anim = get_node("anim")
onready var pause = get_node("pause")
onready var shield_bar = get_node("shield bar")
onready var under_shield_bar = get_node("under shield bar")

var modulate

func _ready():
	player.connect("shield_destroyed", self, "shield_destroyed")
	modulate = under_shield_bar.get_modulate()
	
func pause( pressed ):
	global.paused = pressed
	get_tree().set_pause(global.paused)
	get_node("pause popup").set_hidden(not global.paused)
	message.set_hidden(global.paused)
	if global.paused == true:
		pause.set_opacity(1)
	else:
		pause.set_opacity(0.5)

func update(player):
	update_shield(player.shield_level)
	get_node("score").set_text(str(global.score))

func update_shield(shield_level):
	var color = "BLUE"
	if shield_level < 25:
		color = "RED"
	var texture = load("res://art/PlayerShield%s.tex" % color)
	shield_bar.set_progress_texture(texture)
	shield_bar.set_value(shield_level)
	player.get_node("shield").set_opacity(shield_level/100)

func shield_destroyed(boolean):
	if boolean == true:
		anim.play("shield destroyed")
	else:
		anim.stop_all()
		under_shield_bar.set_modulate(modulate)
	
func show_message(text):
	message.set_text(text)
	message.show()
	message_timer.start()

func _on_message_timer_timeout():
	message.hide()
	message.set_text("")
