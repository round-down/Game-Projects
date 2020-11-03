extends StaticBody2D

onready var sprite = get_node("sprite")
onready var texture = load(global.choose(global.bricks))

func _ready():
	sprite.set_texture(texture)
	self.add_to_group(global.BRICKS)
