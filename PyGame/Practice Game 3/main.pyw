# Pygame Platformer Game

import pygame as pg
from pygame.locals import *
import random
from random import randint, randrange, choice
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # initializes window, etc
        pg.init()
        pg.mixer.init()
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        ICON=pg.image.load('Images\\bunny.ico').convert()
        ICON.set_colorkey(BLACK)
        pg.display.set_icon(ICON)
        self.clock=pg.time.Clock()
        self.running=True
        #self.font_name=pg.font.match_font(FONT_NAME)
        self.load()

    def load(self):
        # Load HighScore
        self.dir=path.dirname(__file__)
        font_dir=path.join(self.dir,'Fonts')
        img_dir=path.join(self.dir,'Images')
        snd_dir=path.join(self.dir,'Sound Effects')
        self.jump_sound=pg.mixer.Sound(path.join(snd_dir,'Jump4.ogg'))
        self.powerup_sound=pg.mixer.Sound(path.join(snd_dir,'Powerup3.ogg'))
        self.jump_sound.set_volume(0.4)
        self.music_dir=path.join(self.dir,'Music')
        try:
            with open(path.join(self.dir,HS_FILE),'r') as f:
                self.highscore=int(f.read())
        except:
            self.highscore=0
            with open(path.join(self.dir,HS_FILE),'w') as f:
                f.write(str(self.highscore))
        # Load Font(s)
        self.font=path.join(font_dir,FONT_NAME)
        # Load spritesheet image
        self.spritesheet=Spritesheet(path.join(img_dir,SPRITESHEET))
        # Cloud Images
        self.cloud_images=[]
        for i in range(1,4):
            self.cloud_images.append(pg.image.load(path.join(img_dir,'cloud{}.png'.format(i))))

    def new(self):
        # Starts a new game
        pg.mixer.music.load(path.join(self.music_dir,'funbgm.ogg'))
        pg.mixer.music.set_volume(0.6)
        self.score=0
        self.all_sprites=pg.sprite.LayeredUpdates()
        self.platforms=pg.sprite.Group()
        self.powerups=pg.sprite.Group()
        self.mobs=pg.sprite.Group()
        self.clouds=pg.sprite.Group()
        self.player=Player(self)
        self.mob_timer=0
        for plat in PLATFORM_LIST:
            Platform(self,*plat)
        self.run()

    def run(self):
        # Game Loop
        pg.mixer.music.play(-1)
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(800)

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
        # Checks for closing window
            if event.type==QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    self.player.jump()
            if event.type==KEYUP:
                if event.key==K_SPACE and not self.player.jetpacking:
                    self.player.jump_cut()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # Spawn a mob?
        now=pg.time.get_ticks()
        if now - self.mob_timer > 5000 + choice([-1000,-500,0,500,1000]):
            self.mob_timer=now
            Mob(self)
        # hit mobs?
        mob_hits=pg.sprite.spritecollide(self.player,self.mobs,False)
        if mob_hits:
            mob_hits=pg.sprite.spritecollide(self.player,self.mobs,False,pg.sprite.collide_mask)
            if mob_hits:
                self.playing=False
        # Check if a player hits a platform only if falling
        if self.player.vel.y>0:
            hits=pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                lowest=hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest=hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                   self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y=lowest.rect.top
                        self.player.vel.y=0
                        self.player.jumping=False
        # If player reaches 1/4 of the screen
        if self.player.rect.top <= HEIGHT/4:
            if randrange(100) < 15:
                Cloud(self)
            self.player.pos.y += max(abs(self.player.vel.y),2)
            for cloud in self.clouds:
                cloud.rect.y += max(abs(self.player.vel.y/2),2)
            for mob in self.mobs:
                mob.rect.y += max(abs(self.player.vel.y),2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y),2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score+=10
        # If player hits a powerup
        pow_hits=pg.sprite.spritecollide(self.player,self.powerups,True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.powerup_sound.play()
                self.player.vel.y =-BOOST_POWER
                self.player.jumping=False
                self.player.jetpacking=True

        # Player dies(Goes below the screen)
        if self.player.rect.top > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y,10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms)==0:
            self.playing=False
        # Spawn new platforms to keep the same average of platforms " 5 "
        while len(self.platforms) < 8:
            width=randrange(50,100)
            Platform(self,randrange(0,WIDTH-width),randrange(-75,-30))

    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.drawtext(str(self.score),22,WHITE,WIDTH/2,15)
        # After drawing everything, flip the display
        pg.display.flip()

    def MainMenu(self):
        # Game splash/start screen
        pg.mixer.music.load(path.join(self.music_dir,'Loop-Menu.ogg'))
        pg.mixer.music.set_volume(1)
        pg.mixer.music.play(-1)
        self.screen.fill(BLACK)
        self.drawtext(TITLE,28,WHITE,WIDTH/2,HEIGHT/4)
        self.drawtext('Arrows keys to move (Left and Right)',8,WHITE,WIDTH/2,HEIGHT/2)
        self.drawtext('Space to jump',7,WHITE,WIDTH/2,HEIGHT/2+20)
        self.drawtext('Press Enter to Start',7,WHITE,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait()
        pg.mixer.music.stop()

    def GameOver(self):
        # Game Over/Continue
        if not self.running:
            return
        self.screen.fill(BLACK)
        if self.score > self.highscore:
            self.highscore=self.score
            with open(path.join(self.dir,HS_FILE),'w') as f:
                f.write(str(self.highscore))
            self.drawtext('HighScore: {}'.format(self.highscore),20,GOLD,WIDTH/2,15)
        else:
            self.drawtext('HighScore: {}'.format(self.highscore),20,GRAY,WIDTH/2,15)
        self.drawtext('Score: {}'.format(self.score),12,WHITE,WIDTH/2,40)
        self.drawtext('GameOver',30,WHITE,WIDTH/2,HEIGHT/2-20)
        self.drawtext('Press Enter to Retry',7,WHITE,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait()

    def wait(self):
        waiting=True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type==QUIT:
                    waiting=False
                    self.running=False
                if event.type==KEYDOWN:
                    if event.key==K_RETURN:
                        waiting=False

    def drawtext(self,text,size,color,x,y):
        font=pg.font.Font(self.font,size)
        text_surface=font.render(text,False,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)

# Make an instance of the Game object
g=Game()
g.MainMenu()
while g.running:
    g.new()
    g.GameOver()

pg.quit()
