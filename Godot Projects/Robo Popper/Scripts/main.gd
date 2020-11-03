#script main.gd
extends Node

onready var sprite  = preload("res://Scenes/101.tscn")
onready var explode  = preload("res://Scenes/explode.tscn")
onready var explo_container = get_node("explosion container")
onready var mob_container = get_node("mob container")
onready var score_lbl = get_node("/root/main/hud/score")
onready var powerup_bar = get_node("/root/main/hud/powerup")

func _process(delta):
	if global.ready_game or mob_container.get_child_count() == 0: # If True
		set_process_unhandled_input(true)
	if mob_container.get_child_count() >= global.max_mobs:
		var random_num = (randi() % global.max_mobs)
		for i in range(random_num/2):
			global.score += 5
			score_lbl.set_text(str(global.score))
			var explo = explode.instance()
			explo.set_pos(mob_container.get_child(i).get_pos())
			explo_container.add_child(explo)
		for i in range(random_num):
			mob_container.get_child(i).set_process_unhandled_input(false)
			mob_container.get_child(i).queue_free()
		snd_player.play("explode")
		powerup_bar.set_val(mob_container.get_child_count())
		
	pass
	
func _ready():
	randomize()
	set_process_unhandled_input(true)
	set_process(true)
	if global.hide_bg == false:
		get_node("background/anim").play("scroll_down")
	music_player.set_stream(music_player.main)
	music_player.play()
	pass
	
func _unhandled_input(event):
	if event.type == InputEvent.SCREEN_TOUCH:
		if event.pressed:
			spawn( event.x, event.y )
			spawn( event.x, event.y )
			spawn( event.x, event.y )
			global.ready_game = false
			set_process_unhandled_input(global.ready_game)
			powerup_bar.set_val(mob_container.get_child_count())
	pass
	
func spawn( option1, option2 ):
	var s = sprite.instance()
	s.set_pos(Vector2(option1, option2))
	mob_container.add_child(s)
	pass