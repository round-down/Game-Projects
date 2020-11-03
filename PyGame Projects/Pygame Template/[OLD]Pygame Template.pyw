# [OLD] pygame template - skeleton for new pygame projects
import pygame as pg
from pygame.locals import *
import random
from settings import *

# Settings/Defining Variables to use
TITLE=''

WIDTH=360
HEIGHT=480
FPS=30

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

# initializes pg and creates a window
pg.init()
pg.mixer.init()
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(TITLE)
clock=pg.time.Clock()

# Creating a sprite group to put all sprites in
all_sprites=pg.sprite.Group()

# Game loop
running=True
while running:

    # Keeps loop running at the right speed
    clock.tick(FPS)

    # Process input events
    for event in pg.event.get():
        # Checks for closing window
        if event.type==QUIT:
            running=False

    # Updating sprites
    all_sprites.update()

    # Draw/render screen and then sprites
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Flip the display
    pg.display.flip()

pg.quit()
