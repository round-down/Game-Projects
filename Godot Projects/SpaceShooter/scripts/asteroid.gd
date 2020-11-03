extends KinematicBody2D

signal explode

export var bounce = 1.1

var size
var vel = Vector2()
var rot_speed
var screensize = Vector2(Globals.get("display/width"), Globals.get("display/height"))
var extents

var textures = {"big": ["res://art/mt4.png",
						"res://art/mt3.png",
						"res://art/mt1.png"],
				"med": ["res://art/md7.png",
						"res://art/md3.png"],
				"sm": ["res://art/s0.png",
						"res://art/s1.png"],
				"tiny": ["res://art/t1.png",
						"res://art/t4.png"]
				}

onready var puff = get_node("puff")

func _ready():
	add_to_group("asteroids")
	randomize()
	set_process(true)

func init(init_size, init_pos, init_vel):
	size = init_size
	if init_vel.length() > 0:
		vel = init_vel
	else:
		vel = Vector2(rand_range(30, 100), 0).rotated(rand_range(0, 2*PI))
	rot_speed = rand_range(-1.5, 1.5)
	var texture = load(textures[size][randi() % textures[size].size()])
	get_node("rock").set_texture(texture)
	extents = texture.get_size() / 2
	var shape = CircleShape2D.new()
	shape.set_radius(min(texture.get_width()/2, texture.get_height()/2))
	add_shape(shape)
	set_pos(init_pos)

func _process(delta):
	vel = vel.clamped(300)
	set_rot(get_rot() + rot_speed * delta)
	move(vel * delta)
	if is_colliding():
		puff.set_global_pos(get_collision_pos())
		puff.set_emitting(true)
		vel += get_collision_normal() * (get_collider().vel.length() * bounce)
	# warp around screen edges
	var pos = get_pos()
	if pos.x - extents.width > screensize.x:
		pos.x = -extents.width
	if pos.x + extents.width < 0:
		pos.x = screensize.x + extents.width
	if pos.y - extents.height > screensize.y:
		pos.y = -extents.height
	if pos.y + extents.height < 0:
		pos.y = screensize.y + extents.height
	set_pos(pos)
	

func explode(hit_vel, boolean):
	emit_signal("explode", size, get_pos(), vel, hit_vel, boolean)
	global.score += global.ast_points[size]
	queue_free()
