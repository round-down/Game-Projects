# script game

extends Node

const GROUP_PIPES   = "pipes"
const GROUP_GROUNDS = "grounds"
const GROUP_BIRDS   = "birds"

const MEDAL_BRONZE   = 10
const MEDAL_SILVER   = 20
const MEDAL_GOLD     = 30
const MEDAL_PLATINUM = 40

# bird texture picker
var bird_texture_picker

var bird_textures = { 0:"yellow", 1:"blue", 2:"red" }

# pipe and background texture picker
var texture_picker

var pipe_top_textrures = { 0:preload("res://sprites/pipe_green_top.png"), 
						   1:preload("res://sprites/pipe_red_top.png")
}
var pipe_bottom_textures = { 0:preload("res://sprites/pipe_green_bottom.png"), 
							 1:preload("res://sprites/pipe_red_bottom.png")
}

onready var background_textures = { 0:preload("res://sprites/background_day.png"), 
									1:preload("res://sprites/background_night.png") 
}


var score_best    = 0 setget _set_score_best
var score_current = 0 setget _set_score_current

const filepath = "user://savedata.bin"

signal score_best_changed
signal score_current_changed

func _ready():
	load_points()
	randomize()
	bird_texture_picker = ( randi() % 3)
	texture_picker = ( randi() % 2 )
	stage_manager.connect("state_changed", self, "_on_state_changed")
	pass

func _set_score_best(new_value):
	if new_value > score_best:
		score_best = new_value
		save_points()
		emit_signal("score_best_changed")
	pass

func _set_score_current(new_value):
	score_current = new_value
	emit_signal("score_current_changed")
	pass

func _on_state_changed():
	score_current = 0
	pass

func load_points():
	var file = File.new()
	if not file.file_exists(filepath): return
	file.open_encrypted_with_pass(filepath, File.READ, ID())
	score_best = file.get_var()
	file.close()

func save_points():
	var file = File.new()
	file.open_encrypted_with_pass(filepath, File.WRITE, ID())
	file.store_var(score_best)
	file.close()

func ID():
	if str(OS.get_name()) == "Android":
		return OS.get_unique_ID()
	else:
		return "WITH-LIVE-SCOTLAND-lost"
	pass
