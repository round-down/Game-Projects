extends Node

onready var anim_company = get_node("other_hud/company/anim")
onready var anim = get_node("anim")
onready var Robo = preload("res://Scenes/101.tscn")

var secret_counter = 0

func _on_play_pressed():
	global.skip_intro = true
	global.goto_scene("res://Scenes/main.tscn")
	pass

func _on_hide_bg_toggled( pressed ):
	snd_player.play("little_click")
	if pressed == true:
		global.hide_bg = true
		get_node("stars").hide()
		get_node("stars").set_emitting(false)
		get_node("bg").hide()
	else:
		global.hide_bg = false
		get_node("stars").show()
		get_node("stars").set_emitting(true)
		get_node("bg").show()
	pass

func _unhandled_input(event):
	if event.type == InputEvent.SCREEN_TOUCH:
		anim.play("hover")
		anim_company.play("intro")
		global.skip_intro = true
		intro()

func _ready():
	intro()
	music_player.set_stream(music_player.menu)
	music_player.play()
	if global.hide_bg == true:
		get_node("bg").hide()
	else:
		get_node("bg").show()
	pass

func intro():
	if global.skip_intro == false:
		set_process_unhandled_input(true)
	else:
		set_process_unhandled_input(false)
	if global.intro == false:
		global.intro = true
		anim.play("intro")
	elif global.intro == true:
		anim.play("hover")
		anim_company.play("intro")

func _on_anim_finished():
	set_process_unhandled_input(false)
	anim.play("hover")
	anim_company.play("intro")
	pass
	
func _on_anim_company_finished():
	set_process_unhandled_input(false)
	anim_company.play("animate")
	pass


func _on_secret_pressed():
	if secret_counter < 11:
		secret_counter += 1
		snd_player.play("explode")
		var r = Robo.instance()
		add_child(r)
	pass


func _on_max_mobs_text_entered( text ):
	global.max_mobs = int(text)
	pass
