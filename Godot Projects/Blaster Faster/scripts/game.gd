extends Node

# groups
var GROUP_ENEMIES = "enemies"
var GROUP_PLAYER  = "player"
var GROUP_BULLET  = "bullet"

var bestscore  = 0 setget set_bestscore
const filepath = "user://save.data"

var current_scene = null

func _ready():
	load_save()
	var root = get_tree().get_root()
	current_scene = root.get_child( root.get_child_count() -1)
	pass
	
func goto_scene(path):
	call_deferred("_deferred_goto_scene",path)
	pass
	
func _deferred_goto_scene(path):
	current_scene.free()
	var s = ResourceLoader.load(path)
	current_scene = s.instance()
	get_tree().get_root().add_child(current_scene)
	get_tree().set_current_scene(current_scene)
	pass


func load_save():
	var f = File.new()
	if not f.file_exists(filepath): return
	f.open_encrypted_with_pass(filepath, File.READ, ID())
	bestscore = f.get_var()
	f.close()
	pass

func save_data():
	var f = File.new()
	f.open_encrypted_with_pass(filepath, File.WRITE, ID())
	f.store_var(bestscore)
	f.close()
	pass

func ID():
	if str(OS.get_name()) == "Android":
		return OS.get_unique_ID()
	else:
		return "WITH-LIVE-SCOTLAND-lost"
	pass

func set_bestscore(new_value):
	bestscore = new_value
	save_data()
	pass
