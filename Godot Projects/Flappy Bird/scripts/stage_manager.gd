# script stage_manager

extends CanvasLayer

const STAGE_GAME = "res://stages/game_stage.tscn"
const STAGE_MENU = "res://stages/menu_stage.tscn"

onready var AMOUNT_TO_FILL_VIEW = ceil(utils._get_view_size().x)

signal state_changed

# scene settings
var current_scene = null
var new_scene = null
var is_changing = false

func _ready():
	var root = get_tree().get_root()
	current_scene = root.get_child( root.get_child_count() -1)
	
	# screen_resized signal
	get_tree().connect("screen_resized", self, "_on_screen_resized")

func _on_screen_resized():
	AMOUNT_TO_FILL_VIEW = ceil(utils._get_view_size().x)
	pass

# change scene functions
func change_stage(stage_path):
	call_deferred("_deferred_goto_scene",stage_path)
	
func _deferred_goto_scene(stage_path):
	if is_changing: return
	
	is_changing = true
	
	# fade to black
	get_node("anim").play("fade_in")
	audio_player.play("sfx_swooshing")
	yield(get_node("anim"), "finished")
	
	current_scene.free()
	var s = ResourceLoader.load(stage_path)
	current_scene = s.instance()
	get_tree().get_root().add_child(current_scene)
	
	# change stage
	emit_signal("state_changed")
	
	get_tree().set_current_scene(current_scene)
	
	#fade from black
	get_node("anim").play("fade_out")
	yield(get_node("anim"), "finished")
	
	is_changing = false
	pass