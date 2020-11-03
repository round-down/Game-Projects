# script ship

extends Area2D

var armor = 4 setget set_armor
var shoot_wait = 0.35

# preloading scenes
onready var scn_flash = preload("res://scenes/flash.tscn")
onready var scn_spark = preload("res://scenes/spark.tscn")

# settings
onready var screen_size = utils.view_size
onready var extents = utils.get_extents(get_node("sprite"), true)

signal shoot
signal explosion
signal armor_changed
signal double_shoot

func _ready():
	utils.attach(self, "exit_tree", audio_player, "_on_ship_exit_tree")
	add_to_group(game.GROUP_PLAYER)
	pass

func _process(delta):
	if utils.mouse_pos.y <= 40: return
	
	var distance = (utils.mouse_pos.x - get_pos().x) * 0.2
	translate(Vector2(distance, 0))
	
	# clamp position from going off screen
	var pos = get_pos()
	pos.x = clamp(pos.x, extents.x, screen_size.x - extents.x)
	set_pos(pos)
	pass

func shoot():
	while !is_queued_for_deletion():
		self.call_deferred("emit_signal", "shoot")
		yield(utils.create_timer(shoot_wait, self), "timeout")
	pass

func set_armor(new_value):
	if new_value > 4: return
	if is_queued_for_deletion(): return
	
	if new_value < armor:
		audio_player.play("hit_ship")
		utils.main_node.call_deferred("add_child", scn_flash.instance())
	
	armor = new_value
	self.call_deferred("emit_signal", "armor_changed", armor)
	if armor <= 0:
		self.call_deferred("emit_signal", "explosion", get_global_pos())
		self.call_deferred("queue_free")
	pass
