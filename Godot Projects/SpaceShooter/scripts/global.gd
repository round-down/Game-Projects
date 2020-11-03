extends Node

# game settings
var game_over = false
var score = 0
var level = 0
var paused = false
var current_scene = null
var new_scene = null

# player settings
var shield_max = 100
var shield_regen = 10
var bullet_damage = 10
var cannon_damage = 50
var run_into_enemy_damage = 100

# enemy settings
var enemy_bullet_damage = 25
var enemy_health = 100
var enemy_points = 100

# asteroid settings
var break_pattern = { "big":"med",
					  "med":"sm",
					  "sm":"tiny",
					  "tiny":null}
					
var ast_damage = { "big":40,
				   "med":20,
				   "sm":15,
				   "tiny":10}
var ast_points = { "big":10,
				   "med":15,
				   "sm":20,
				   "tiny":40}

func create_timer(wait_time, boolean):
	var t = Timer.new()
	t.set_wait_time(0.5)
	t.set_one_shot(true)
	t.start()
	if boolean == true:
		yield(t, "timeout")

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

func new_game():
	game_over = false
	score = 0
	level = 0
	goto_scene("res://scenes/main.tscn")
