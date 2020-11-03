# Pygame Template

import pygame as pg
from pygame.locals import *
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initializes window, etc
        pg.init()
        pg.mixer.init()
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock=pg.time.Clock()
        self.running=True

    def new(self):
        # Starts a new game
        self.all_sprites=pg.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
        # Checks for closing window
            if event.type==QUIT:
                if self.playing:
                    self.playing=False
                self.running=False

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def MainMenu(self):
        # Game splash/start screen
        pass

    def GameOver(self):
        # Game Over/Continue
        pass

# Make an instance of the Game object
g=Game()
g.MainMenu()
while g.running:
    g.new()
    g.GameOver()

pg.quit()
