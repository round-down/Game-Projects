# script enemy_clever

extends "res://scripts/enemy.gd"

func _ready():
	randomize()
	velocity.x = utils.choose([velocity.x, -velocity.x])
	shoot()
	pass

signal shoot

func _process(delta):
	# bouncing on the edges
	if get_pos().x <= extents.x:
		velocity.x = abs(velocity.x)
	if get_pos().x >= utils.view_size.width - extents.x:
		velocity.x = -abs(velocity.x)
	pass

func shoot():
	while !is_queued_for_deletion():
		self.call_deferred("emit_signal", "shoot")
		yield(utils.create_timer(1.5, self), "timeout")
	pass
