extends Position2D

# preloading scenes
onready var scn_flare = preload("res://scenes/flare.tscn")
onready var scn_explosion = preload("res://scenes/explosion.tscn")

onready var character = get_parent().get_parent()

var scn_laser

var is_double_shooting = false

func _ready():
	character.connect("shoot", self, "_shoot")
	character.connect("explosion", self, "_create_explosion")
	pass

func _shoot():
	if not scn_laser: set_laser()
	
	_create_laser(get_global_pos())
	_create_flare()
	
	if character.get_name() == "ship" and is_double_shooting:
		var laser = _create_laser(get_global_pos())
		if sign(get_pos().x) == -1:
			laser.velocity.x = -25
		elif sign(get_pos().x) == 1:
			laser.velocity.x = 25
	
	pass

func set_laser():
	if   character.is_in_group(game.GROUP_PLAYER) :
		scn_laser = preload("res://scenes/laser_ship.tscn")
		character.connect("double_shoot", self, "_set_double_shoot")
	elif character.is_in_group(game.GROUP_ENEMIES): scn_laser = preload("res://scenes/laser_enemy.tscn")
	pass

func _create_laser(pos):
	var laser = scn_laser.instance()
	laser.set_pos(pos)
	utils.main_node.add_child(laser)
	return laser
	pass

func _create_flare():
	if character.is_in_group(game.GROUP_ENEMIES): return
	var flare = scn_flare.instance()
	flare.set_pos(get_pos())
	character.call_deferred("add_child", flare)
	pass

func _create_explosion(pos):
	var expl = scn_explosion.instance()
	expl.set_pos(pos)
	utils.main_node.add_child(expl)
	yield(expl.get_node("anim"), "finished")
	pass

func _set_double_shoot():
	is_double_shooting = true
	character.shoot_wait = 0.2
	yield(utils.create_timer(7, self), "timeout")
	character.shoot_wait = 0.35
	is_double_shooting = false
	audio_player.play("powerup_laser_gone")
	utils.remote_call("camera", "shake", 2, 0.13)
	_create_spark()
	pass

func _create_spark():
	var spark = character.scn_spark.instance()
	spark.set_pos(get_global_pos())
	utils.main_node.call_deferred("add_child", spark)
	spark.set_emitting(true)
	yield(utils.create_timer(0.5, self), "timeout")
	spark.queue_free()
	pass
