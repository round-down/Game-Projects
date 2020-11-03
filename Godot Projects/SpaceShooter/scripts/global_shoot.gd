extends Node2D

onready var bullet = preload("res://scenes/bullet.tscn")
onready var player = get_parent()
onready var gun_timer = get_parent().get_node("gun timer")
