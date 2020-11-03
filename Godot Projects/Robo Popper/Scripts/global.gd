extends Node

var mute_sounds_toggled = false
var mute_music_toggled = false

var skip_intro = false
var intro = false

var hide_bg = false

var ready_game = true 

var powerup = 0

var score = 0

var mob_timer = 0.95
var max_mobs = 75

var current_scene = null


func _ready():
	var root = get_tree().get_root()
	current_scene = root.get_child( root.get_child_count() -1)
	
func goto_scene(path):
	call_deferred("_deferred_goto_scene",path)
	
func _deferred_goto_scene(path):
	current_scene.free()
	var s = ResourceLoader.load(path)
	current_scene = s.instance()
	get_tree().get_root().add_child(current_scene)
	get_tree().set_current_scene(current_scene)