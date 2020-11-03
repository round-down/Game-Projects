extends Node

# main settings
onready var screensize = get_tree().get_root().get_visible_rect().size

# hud
onready var hud = get_node("/root/hud")

# game settings
var game_over = false
var score = 0 setget set_score
var level = 0 setget set_level
var paused = false
var mute_sounds = false

# ball settings
const SPEED_UP = 25
const MAX_SPEED = 500
var start_direction = [Vector2(rand_range(200,400),rand_range(-400,-200)),
					   Vector2(rand_range(-400,-200),rand_range(200,400))]

# levels
var levels = [1, 2, 3, 4, 5]

# groups
var BRICKS = "BRICKS"

var bricks = ["res://images/bricks/brick0.png", "res://images/bricks/brick1.png",
			  "res://images/bricks/brick2.png", "res://images/bricks/brick3.png",
			  "res://images/bricks/brick4.png"]

# scene settings
var current_scene = null
var new_scene = null

func _ready():
	var root = get_tree().get_root()
	current_scene = root.get_child( root.get_child_count() -1)
	
# change scene functions
func goto_scene(path):
	call_deferred("_deferred_goto_scene",path)
	
func _deferred_goto_scene(path):
	current_scene.free()
	var s = ResourceLoader.load(path)
	current_scene = s.instance()
	get_tree().get_root().add_child(current_scene)
	get_tree().set_current_scene(current_scene)

# utility functions
func create_timer(wait_time, set_oneshot, set_autostart):
	var timer = Timer.new()
	timer.set_wait_time(wait_time)
	timer.set_one_shot(set_oneshot)
	timer.set_autostart(set_autostart)
	timer.connect("timeout", timer, "queue_free")
	junk_container.add_child(timer)
	timer.start()
	return timer
	
func choose(choices):
	randomize()
	var rand_index = randi() % choices.size()
	return choices[rand_index]

# game functions
func restart():
	game_over = false
	set_score(0)
	level = 0
	clear_junk_container()
	hud_settings(true)
	goto_scene("res://scenes/main.tscn")
	
func clear_junk_container():
	for i in range(junk_container.get_child_count()):
		junk_container.get_child(i).queue_free()
		
func game_over():
	hud_settings(false)
	goto_scene("res://scenes/gameover.tscn")
	
func hud_settings(boolean):
	if boolean == false:
		hud.score_lbl.hide()
		hud.pause_btn.hide()
		hud.mute_sounds_btn.set_pos(hud.pause_btn_pos)
	else:
		hud.score_lbl.show()
		hud.pause_btn.show()
		hud.mute_sounds_btn.set_pos(hud.mute_sounds_btn_pos)

func set_extents(object):
	var size = object.get_node("sprite").get_texture().get_size() / 2
	object.extents = size
	
func set_score(value):
	score = value
	get_node("/root/hud/score lbl").set_text(str(score))
	
func set_level(value):
	if level > 5:
		var load_level = load("res://scenes/levels/Level %d.tscn" % choose(levels))
		if load_level:
			var l = load_level.instance()
			junk_container.add_child(l)
	else:
		level = value
		var load_level = load("res://scenes/levels/Level %d.tscn" % level)
		if load_level:
			var l = load_level.instance()
			junk_container.add_child(l)
