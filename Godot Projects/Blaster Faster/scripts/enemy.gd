# script enemy

extends Area2D

export var armor = 2 setget set_armor

# getting available nodes
onready var sprite = get_node("sprite")

# settings
onready var screen_size = utils.view_size
onready var extents = utils.get_extents(sprite, true)

export var velocity = Vector2()

signal explosion

func _ready():
	add_to_group(game.GROUP_ENEMIES)
	connect("area_enter", self, "_on_area_enter")
	set_process(true)
	pass

func _process(delta):
	translate(velocity * delta)
	
	if get_pos().y >= screen_size.y + extents.y:
		self.call_deferred("queue_free")
	pass

func set_armor(new_value):
	if is_queued_for_deletion(): return
	
	if new_value < armor: audio_player.play("hit_enemy")
	armor = new_value
	if armor <= 0:
		utils.find_node("tex_score").score += 5
		self.call_deferred("emit_signal", "explosion", get_global_pos())
		self.call_deferred("queue_free")
	pass

func _on_area_enter(other):
	if other.is_in_group(game.GROUP_PLAYER):
		other.armor -= 1
		self.call_deferred("emit_signal", "explosion", get_global_pos())
	pass


