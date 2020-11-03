extends Node

var points = 0 setget set_points
const filepath = "user://points.data"

func _ready():
	load_points()

func load_points():
	var file = File.new()
	if not file.file_exists(filepath): return
	file.open(filepath, File.READ)
	points = file.get_var()
	file.close()

func save_points():
	var file = File.new()
	file.open(filepath, File.WRITE)
	file.store_var(points)
	file.close()

func set_points(new_value):
	points += new_value
	save_points()
	get_node("/root/hud/points").set_text(str(points))