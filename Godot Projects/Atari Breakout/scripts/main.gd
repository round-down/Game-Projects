extends Node

onready var paddle = get_node("paddle")
onready var ball = get_node("ball")

func _ready():
	change_level()
	paddle.set_pos(Vector2(global.screensize.x / 2, global.screensize.y / 2))
	ball.set_pos(Vector2(global.screensize.x / 2, global.screensize.y / 2.1))
	set_process(true)
	
func _process(delta):
	if global.game_over == true:
		global.game_over()
	
	
func change_level():
	sounds.play("intro")
	global.level += 1
	if global.level >= 2:
		game.points = global.score
	hud.level_lbl.set_text("Level %d" % global.level)
	hud.level_lbl.show()
	var timer = global.create_timer(2.3, true, false)
	yield(timer, "timeout")
	hud.level_lbl.set_text("")
	hud.level_lbl.hide()
