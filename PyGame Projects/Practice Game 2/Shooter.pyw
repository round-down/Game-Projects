import pygame,sys,time,os
from pygame.locals import *
import random
from random import randint, randrange

pygame.init()
pygame.mixer.init()

WIDTH=400
HEIGHT=517
FPS=60

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Shooter')
ICON=pygame.image.load('Images\\gps.ico').convert()
ICON.set_colorkey(BLACK)
pygame.display.set_icon(ICON)

clock=pygame.time.Clock()

background=pygame.image.load('Images\\purple.png').convert()
background_rect=background.get_rect()

mainmenuImg=pygame.image.load('Images\\menu.png').convert()
mainmenuImg.set_colorkey(BLACK)
mainmenuImg_rect=mainmenuImg.get_rect()

playerImg=pygame.image.load('Images\\goldspaceship2.png').convert()
bulletImg=pygame.image.load('Images\\laserRed01.png').convert()

shieldbar=pygame.image.load('Images\\PlayerProperties\\PlayerBAR(Small).png').convert()
shieldbar.set_colorkey(BLACK)

healthbarbackground=pygame.image.load('Images\\PlayerProperties\\PlayerBAR INSIDE(Small).png').convert()
healthbarbackground.set_colorkey(WHITE)
healthbar=pygame.image.load('Images\\PlayerProperties\\PlayerBAR(Small).png').convert()
healthbar.set_colorkey(BLACK)


def forImages4Enemies(FILENAME):
    filename=FILENAME+'{}'.format(i)
    img=pygame.image.load('Images\\{}.png'.format(filename)).convert()
    img.set_colorkey(BLACK)
    meteorImgs.append(img)

meteorImgs=[]
for i in range(12):
    forImages4Enemies('mt')
    forImages4Enemies('md')
for i in range(6):
    forImages4Enemies('s')
    forImages4Enemies('t')



explo_sounds=[]
for snd in ['Sound Effects\\Explosion.ogg','Sound Effects\\Explosion6.ogg']:
    explo_sounds.append(pygame.mixer.Sound(snd))


exploAnimation={}
exploAnimation['lg']=[]
exploAnimation['md']=[]
exploAnimation['sm']=[]
exploAnimation['player']=[]
for i in range(9):
    filename='regularExplosion0{}.png'.format(i)
    img=pygame.image.load('Images\\{}'.format(filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img,(75,75))
    exploAnimation['lg'].append(img_lg)
    img_sm=pygame.transform.scale(img,(48,48))
    exploAnimation['md'].append(img_sm)
    img_sm=pygame.transform.scale(img,(32,32))
    exploAnimation['sm'].append(img_sm)

    filename='sonicExplosion0{}.png'.format(i)
    img=pygame.image.load('Images\\SuperExplosion\\{}'.format(filename)).convert()
    img.set_colorkey(BLACK)
    exploAnimation['player'].append(img)
player_explode=pygame.mixer.Sound('Sound Effects\\rumble1.ogg')

powerup_images={}
powerup_images['shieldPow']=pygame.image.load('Images\\shieldPow.png').convert()
powerup_images['gunPow']=pygame.image.load('Images\\gunPow.png').convert()
powerup_images['healthPow']=pygame.image.load('Images\\healthPow.png').convert()


musicPL=['Music\\Mars.ogg','Music\\Mercury.ogg','Music\\Venus.ogg']




class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerImg,(47,35))
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.radius=19
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx=WIDTH//2
        self.rect.bottom=HEIGHT-17
        self.speedx=0
        self.health=100
        self.shieldbar=100
        self.displayshield=False
        self.score=0
        self.highscore=0
        self.howmanyingame=20
        self.explo_size=None
        self.power=1
        self.power_time=pygame.time.get_ticks()
        self.POWERUP_TIME=15000#miliseconds. Equals 15 seconds

    def powerup(self):
        self.power+=1
        self.power_time=pygame.time.get_ticks()


    def update(self):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > self.POWERUP_TIME:
            self.power=1
            self.power_time=pygame.time.get_ticks()
        self.speedx=0
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx=-5
        if keys[pygame.K_RIGHT]:
            self.speedx=5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right=WIDTH
        if self.rect.left < 0:
            self.rect.left=0

    def shoot(self):
        if self.power==1:
            bullet=Bullet(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif self.power == 2:
            bullet1=Bullet(self.rect.left,self.rect.centery)
            bullet2=Bullet(self.rect.right,self.rect.centery-1)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet1)
            bullets.add(bullet2)
        elif self.power == 3:
            bullet1=Bullet(self.rect.left,self.rect.centery)
            bullet2=Bullet(self.rect.centerx,self.rect.top-1)
            bullet3=Bullet(self.rect.right,self.rect.centery-2)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            all_sprites.add(bullet3)
            bullets.add(bullet1)
            bullets.add(bullet2)
            bullets.add(bullet3)
        elif self.power >= 4:
            self.power=1
player=Player()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig=random.choice(meteorImgs)
        self.image_orig.set_colorkey(BLACK)
        self.image=self.image_orig.copy()
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*.85//2)
        #pygame.draw.circle(self.image_orig,RED,self.rect.center,self.radius)
        self.rect.x=randrange(0,WIDTH-self.rect.width)
        self.rect.y=randrange(-150,-100)
        self.speedy=randrange(1,8)
        self.speedx=randrange(-3,3)
        self.rot=0
        self.rot_speed=randrange(-8,8)
        self.last_update=pygame.time.get_ticks()
        self.damage=self.radius//2

    def rotate(self):
        now=pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update=now
            self.rot=(self.rot+self.rot_speed)%360
            new_image=pygame.transform.rotate(self.image_orig,self.rot)
            old_center=self.rect.center
            self.image=new_image
            self.rect=self.image.get_rect()
            self.rect.center=old_center

    def update(self):
        self.rotate()
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            m=Mob()
            all_sprites.add(m)
            mobs.add(m)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=bulletImg
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10

    def update(self):
        self.rect.y +=self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type=random.choice(('shieldPow','gunPow','healthPow'))
        self.image=powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.radius=10
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.center=center
        self.speedy=5

    def update(self):
        self.rect.y +=self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=exploAnimation[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=75


    def update(self):
        now= pygame.time.get_ticks()
        if now-self.last_update > self.frame_rate:
            self.last_update=now
            self.frame += 1
            if self.frame==len(exploAnimation[self.size]):
                self.kill()
            else:
                center=self.rect.center
                self.image=exploAnimation[self.size][self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center

all_sprites=pygame.sprite.Group()

mobs=pygame.sprite.Group()

smeteors=pygame.sprite.Group()

bullets=pygame.sprite.Group()

shield=pygame.sprite.Group()

powerups=pygame.sprite.Group()

all_sprites.add(player)




######################################
class MenuSelect():# Menu Select Bar #
######################################
    def __init__(self):
        self.x=WIDTH-97
        self.y=32
        self.MenuSelectBar=pygame.image.load('Images\\menuselectbar.png')
ms=MenuSelect()



def Difficulty(n):
    if n==1:
        n=10
    elif n==2:
        n=20
    elif n==3:
        n=30
    ReturnSound()
    PlayerAndEnemiesRestart()
    player.howmanyingame=n
    spawnEnemies()
    mainscreenupdate()
    Menu()

def spawnEnemies():
    for i in range(player.howmanyingame):
        m=Mob()
        all_sprites.add(m)
        mobs.add(m)

def drawpicture(surf,image,x,y):
    draw_surface=image
    draw_rect=draw_surface.get_rect()
    draw_rect.center=(x,y)
    surf.blit(draw_surface,draw_rect)

def drawtext(surf,text,size,color,x,y):
    BASICFONT=pygame.font.Font('Fonts\\PressStart2P.ttf',size)
    text_surface=BASICFONT.render(text,False,color)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)

def GameControls():
    drawtext(screen,'Arrow Keys To Move Left or Right',7,WHITE,WIDTH//2,HEIGHT//2-30)
    drawtext(screen,'SPACE to Shoot',7,WHITE,WIDTH//2,HEIGHT//2-10)
    drawtext(screen,'"E" to Open/Close Menu and go Back',7,WHITE,WIDTH//2,HEIGHT//2+35)
    drawtext(screen,'"P" to Pause Music, "O" to Unpause Music',7,WHITE,WIDTH//2,HEIGHT//2+50)

def pickLargeOrSmallExplo(hit):
    if hit.radius < 10:
        player.explo_size='sm'
    elif hit.radius < 25:
        player.explo_size='md'
    else:
        player.explo_size='lg'

def PlayShieldPowSound():
    click=pygame.mixer.Sound('Sound Effects\\shieldPow.ogg')
    click.play()

def PlayGunPowSound():
    click=pygame.mixer.Sound('Sound Effects\\gunPow.ogg')
    click.play()

def PlayHealthPowSound():
    click=pygame.mixer.Sound('Sound Effects\\healthPow.ogg')
    click.play()

def displayshieldbar():
    if player.displayshield==True:
        pygame.draw.rect(screen, (15,91,191), (5, HEIGHT-17, player.shieldbar, HEIGHT-11))
        screen.blit(shieldbar,(0,HEIGHT-17))

def displayhealthbar():
    if player.health > 0:
        screen.blit(healthbarbackground,(5,HEIGHT-17))
        pygame.draw.rect(screen, (199,27,0), (5, HEIGHT-17, player.health, HEIGHT-11))
        screen.blit(healthbar,(0,HEIGHT-17))
    else:
        screen.blit(healthbarbackground,(5,HEIGHT-17))
        screen.blit(healthbar,(0,HEIGHT-17))

def changeHighScore():
    if player.score > player.highscore:
        player.highscore=player.score

def PlayerAndEnemiesRestart():
    player.health=100
    player.shieldbar=100
    player.power=1
    player.score=0
    kill_all_sprites()
    player.rect.centerx=WIDTH//2
    player.rect.bottom=HEIGHT-17

def GameOver():
    pygame.mixer.music.fadeout(250)
    Lost=pygame.mixer.Sound('Sound Effects\\Lose Jingle.ogg')
    Lost.play()
    changeHighScore()
    FPS=5
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        if player.highscore==player.score:
            drawtext(screen,'Highscore: {}'.format(str(player.highscore)),18,(255,215,0),WIDTH//2-10,10)
        else:
            drawtext(screen,'Highscore: {}'.format(str(player.highscore)),18,GRAY,WIDTH//2-10,10)
        drawtext(screen,'Score: {}'.format(str(player.score)),13,WHITE,WIDTH//2-10,40)
        if player.howmanyingame==10:
            drawtext(screen,'Mode: EASY'.format(str(player.score)),15,WHITE,WIDTH//2-10,100)
        elif player.howmanyingame==20:
            drawtext(screen,'Mode: NORMAL'.format(str(player.score)),15,YELLOW,WIDTH//2-10,100)
        elif player.howmanyingame==30:
            drawtext(screen,'Mode: HARD'.format(str(player.score)),15,RED,WIDTH//2-10,100)
        drawtext(screen,'GameOver',20,WHITE,WIDTH//2,HEIGHT//2-10)
        drawtext(screen,'Enter To Retry',9,WHITE,WIDTH//2,HEIGHT//2+85)
        drawtext(screen,'"E" to return to Main Menu',9,WHITE,WIDTH//2,HEIGHT//2+100)

        for event in pygame.event.get():
            if event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_RETURN:
                    Lost.stop()
                    PlayMusic()
                    PlayerAndEnemiesRestart()
                    spawnEnemies()
                    main()
                elif event.key==K_e:
                    Lost.stop()
                    MainMenu()

        pygame.display.update()

def kill_all_sprites():
    for sprites in all_sprites:
        sprites.kill()
    for sprites in mobs:
        sprites.kill()
    all_sprites.add(player)

def Intro2():
    screen.fill(BLACK)
    counter=0
    while True:
        GameControls()
        for event in pygame.event.get():
            if event.type==QUIT:
                exitGame()
        pygame.display.update()
        counter+=1
        time.sleep(0.125)
        if counter==32:
            break
    PlayMusic()
    PlayerAndEnemiesRestart()
    spawnEnemies()
    main()

def Intro():
    pygame.draw.rect(screen, BLACK, (0, HEIGHT-17, WIDTH, HEIGHT))
    IntroSound()
    counter=0
    while True:
        drawtext(screen,'Abbacus Inc.',20,WHITE,WIDTH//2,HEIGHT//2-10)
        for event in pygame.event.get():
            if event.type==QUIT:
                exitGame()
        pygame.display.update()

        counter+=1
        time.sleep(0.125)
        if counter==27:
            MainMenu()

def IntroSound():
    intro=pygame.mixer.Sound('Sound Effects\\Intro Jingle.ogg')
    intro.play()

def explode():
    sd=random.choice(explo_sounds)
    sd.set_volume(0.35)
    sd.play()

def ReturnShootSound():
    shoot=pygame.mixer.Sound('Sound Effects\\shootsound.ogg')
    shoot.set_volume(0.35)
    shoot.play()

def PlayMusic():
    pygame.mixer.music.set_endevent(USEREVENT)
    rm=random.choice(musicPL)
    pygame.mixer.music.load(rm)
    pygame.mixer.music.play(randint(1,2))

#***************************************#
def ReturnSound():# Returns Click Sound #
#***************************************#
    click=pygame.mixer.Sound('Sound Effects\\click.ogg')
    click.set_volume(0.5)
    click.play()

def blitMenuBar():
    screen.blit(ms.MenuSelectBar,(ms.x,ms.y))

#*************************************#
def exitGame():# Self Explanatory ... #
#*************************************#
    pygame.quit()
    sys.exit()

#***************************#
def Save():# Save HighScore #
#***************************#
    pass

#**************************#
def GameMode():# Game Mode #
#**************************#
    while True:

        MenuBox()

        drawtext(screen,'Easy',8,BLACK,WIDTH-50,33)
        drawtext(screen,'Normal',8,BLACK,WIDTH-50,50)
        drawtext(screen,'Hard',8,BLACK,WIDTH-50,67)

        blitMenuBar()

                    #^^^ Goes up by increments of 17  ^^^#
                #Y Positions =[33=mode 50=??? 67=???]


        for event in pygame.event.get():
            if event.type==USEREVENT:
                rm=random.choice(musicPL)
                pygame.mixer.music.load(rm)
                pygame.mixer.music.play(randint(1,2))
            elif event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    Settings()
                elif event.key==K_p:
                    pygame.mixer.music.pause()
                elif event.key==K_o:
                    pygame.mixer.music.unpause()
                elif event.key==K_DOWN:
                    if ms.y==66:
                        ms.y=32
                    else:
                        ms.y+=17

                elif event.key==K_UP:
                    if ms.y==32:
                        ms.y=66
                    else:
                        ms.y-=17

                elif event.key==K_RETURN and ms.y==32:#EASY
                    Difficulty(1)

                elif event.key==K_RETURN and ms.y==49:#NORMAL(DEFAULT)
                    Difficulty(2)

                elif event.key==K_RETURN and ms.y==66:#HARD
                    Difficulty(3)


                    #^^^ Goes up by increments of 17  ^^^#
                #Y Positions =[32=mode 49=??? 66=???]

        pygame.display.update()
        clock.tick(FPS)

#******************************************#
def Settings():# Settings Option From Menu #
#******************************************#
    while True:

        MenuBox()

        drawtext(screen,'Mode',8,BLACK,WIDTH-50,33)
        drawtext(screen,'???',8,BLACK,WIDTH-50,50)
        drawtext(screen,'???',8,BLACK,WIDTH-50,67)

        blitMenuBar()

                    #^^^ Goes up by increments of 17  ^^^#
                #Y Positions =[33=mode 50=??? 67=???]


        for event in pygame.event.get():
            if event.type==USEREVENT:
                rm=random.choice(musicPL)
                pygame.mixer.music.load(rm)
                pygame.mixer.music.play(randint(1,2))
            elif event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    Menu()
                elif event.key==K_p:
                    pygame.mixer.music.pause()
                elif event.key==K_o:
                    pygame.mixer.music.unpause()
                elif event.key==K_DOWN:
                    if ms.y==66:
                        ms.y=32
                    else:
                        ms.y+=17

                elif event.key==K_UP:
                    if ms.y==32:
                        ms.y=66
                    else:
                        ms.y-=17

                elif event.key==K_RETURN and ms.y==32:
                    ReturnSound()
                    GameMode()


                elif event.key==K_RETURN and ms.y==49:
                    ReturnSound()
                    #ADD MORE HERE LATER
                elif event.key==K_RETURN and ms.y==66:
                    ReturnSound()
                    #ADD MORE HERE LATER


                    #^^^ Goes up by increments of 17  ^^^#
                #Y Positions =[32=mode 49=??? 66=???]

        pygame.display.update()
        clock.tick(FPS)

#**********************************#
def Help():# Help Option From Menu #
#**********************************#
    FPS=5
    pygame.mixer.music.set_volume(0.3)
    while True:
        GameControls()
        for event in pygame.event.get():
            if event.type==USEREVENT:
                rm=random.choice(musicPL)
                pygame.mixer.music.load(rm)
                pygame.mixer.music.play(randint(1,2))
            elif event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    pygame.mixer.music.set_volume(0.9)
                    mainscreenupdate()
                    Menu()
                elif event.key==K_p:
                    pygame.mixer.music.pause()
                elif event.key==K_o:
                    pygame.mixer.music.unpause()
        pygame.display.update()
        clock.tick(FPS)

#**********************************#
def Exit():# Exit Option From Menu #
#**********************************#
    Save()
    MainMenu()
    pass

#************************************************************#
def MenuBox():# Box That Contains the Menu Text and Such ... #
#************************************************************#

    pygame.draw.rect(screen, WHITE, (WIDTH-100, 25, WIDTH, 54))#WHITE BOX
    pygame.draw.line(screen, BLACK, (WIDTH-100, 26), (WIDTH, 26), 4)#TOP LINE
    pygame.draw.line(screen, BLACK, (WIDTH-100, 26), (WIDTH-100, 79), 4)#LEFT LINE
    pygame.draw.line(screen, BLACK, (WIDTH-100, 79), (WIDTH, 79), 4)#BOTTOM LINE
    pygame.draw.line(screen, BLACK, (WIDTH-2, 26), (WIDTH-2, 79), 4)#RIGHT LINE

#********************************************#
def Menu():# Main Menu Function for Settings #
#********************************************#
    FPS=15
    pygame.mixer.music.set_volume(0.3)
    while True:

        MenuBox()
        drawtext(screen,'Settings',8,BLACK,WIDTH-45,33)
        drawtext(screen,'Help',8,BLACK,WIDTH-50,50)
        drawtext(screen,'Exit',8,BLACK,WIDTH-50,67)

        blitMenuBar()

                    #^^^ Goes up by increments of 17  ^^^#
                #Y Positions =[33=settings 50=help 67=quit]


        for event in pygame.event.get():
            if event.type==USEREVENT:
                rm=random.choice(musicPL)
                pygame.mixer.music.load(rm)
                pygame.mixer.music.play(randint(1,2))
            elif event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    pygame.mixer.music.set_volume(0.9)
                    main()
                if event.key==K_DOWN:
                    if ms.y==66:
                        ms.y=32
                    else:
                        ms.y+=17

                elif event.key==K_UP:
                    if ms.y==32:
                        ms.y=66
                    else:
                        ms.y-=17

                elif event.key==K_RETURN and ms.y==32:
                    ReturnSound()
                    Settings()
                elif event.key==K_RETURN and ms.y==49:
                    ReturnSound()
                    Help()
                elif event.key==K_RETURN and ms.y==66:
                    ReturnSound()
                    pygame.mixer.music.fadeout(800)
                    pygame.mixer.music.set_volume(0.9)
                    Exit()
                elif event.key==K_p:
                    pygame.mixer.music.pause()
                elif event.key==K_o:
                    pygame.mixer.music.unpause()

                    #^^^ Goes up by increments of 17  ^^^#
                #Y Positions =[32=settings 49=help 66=quit]

        pygame.display.update()
        clock.tick(FPS)

##############################################
def mainscreenupdate():# Updates Game Screen #
##############################################
        screen.blit(background,background_rect)
        all_sprites.draw(screen)
        drawtext(screen,str(player.score),18,WHITE,WIDTH//2,10)
        pygame.draw.rect(screen, BLACK, (0, HEIGHT-17, WIDTH, HEIGHT))
        displayhealthbar()
        displayshieldbar()
        pygame.display.flip()

#*********************************#
def MainMenu():# Main Menu Screen #
#*********************************#
    PlayerAndEnemiesRestart()
    pygame.mixer.music.load('Music\\Map.ogg')
    pygame.mixer.music.play(-1)
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    FPS=10
    while True:

        drawpicture(screen,mainmenuImg,WIDTH//2,HEIGHT//2)

        drawtext(screen,'ASTERIOD SHOOTER',20,WHITE,WIDTH//2,HEIGHT//8)
        drawtext(screen,'Abbacus Inc.',8,WHITE,WIDTH-55,HEIGHT-10)
        drawtext(screen,'???',10,BLACK,WIDTH//2,HEIGHT//2-50)
        drawtext(screen,'Settings',10,BLACK,WIDTH//2,HEIGHT//2-25)
        drawtext(screen,'Help',10,BLACK,WIDTH//2,HEIGHT//2)
        drawtext(screen,'Start',10,BLACK,WIDTH//2.5+3,HEIGHT//2+35)
        drawtext(screen,'Quit',10,BLACK,WIDTH//2+38,HEIGHT//2+35)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.mixer.music.fadeout(600)
                exitGame()
            elif event.type==KEYDOWN:

                if event.key==K_e:
                    pygame.mixer.music.fadeout(1500)
                    Intro2()
                elif event.key==K_p:
                    pygame.mixer.music.pause()
                elif event.key==K_o:
                    pygame.mixer.music.unpause()

        pygame.display.flip()
        clock.tick(FPS)

######################################
def main():# Main Function/Game Loop #
######################################

    FPS=60

    while True:

        for event in pygame.event.get():
            if event.type==USEREVENT:
                rm=random.choice(musicPL)
                pygame.mixer.music.load(rm)
                pygame.mixer.music.play(randint(1,2))
            elif event.type==QUIT:
                pygame.mixer.music.fadeout(600)
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE and player.health > 0:
                    ReturnShootSound()
                    player.shoot()

                elif event.key==K_e:
                    Menu()
                elif event.key==K_p:
                    pygame.mixer.music.pause()
                elif event.key==K_o:
                    pygame.mixer.music.unpause()


        hits=pygame.sprite.groupcollide(mobs,shield,True,False,pygame.sprite.collide_circle)
        for hit in hits:
            explode()
            pickLargeOrSmallExplo(hit)
            expl=Explosion(hit.rect.center,player.explo_size)
            all_sprites.add(expl)
            m=Mob()
            all_sprites.add(m)
            mobs.add(m)

        hits=pygame.sprite.spritecollide(player,powerups,True,pygame.sprite.collide_circle)
        for hit in hits:
            if hit.type=='shieldPow' and player.health > 0:
                PlayShieldPowSound()
                player.displayshield=True
                player.shieldbar=100
                if player.shieldbar > 100:
                    player.shieldbar=100
            if hit.type=='gunPow':
                PlayGunPowSound()
                player.powerup()
            if hit.type=='healthPow':
                PlayHealthPowSound()
                player.health+=randrange(10,22)
                if player.health > 100:
                    player.health=100

        #checks if bullet hit mob
        hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
        for hit in hits:
            if hit.radius==62 and player.power==1:
                pickLargeOrSmallExplo(hit)
                expl=Explosion(player.rect.center,player.explo_size)
                all_sprites.add(expl)
                player_explode.play()
                explode_FIREMETEOR=Explosion(hit.rect.center,'player')
                all_sprites.add(explode_FIREMETEOR)

                if player.displayshield==False:
                    player.health-=35
                    if player.health <= 0:
                            player_explode.play()
                            player.health=0
                            explode_player=Explosion(player.rect.center,'player')
                            all_sprites.add(explode_player)
                            player.kill()
                else:
                    ShieldRemaining=player.shieldbar-35
                    if ShieldRemaining <= 0:
                        player.displayshield=False
                        player.health+=ShieldRemaining
                    else:
                        player.shieldbar-=35
            else:
                explode()
                pickLargeOrSmallExplo(hit)
                expl=Explosion(hit.rect.center,player.explo_size)
                all_sprites.add(expl)
                if hit.radius <= 13:
                    player.score+=hit.radius*7
                else:
                    player.score+=hit.radius//5
                m=Mob()
                all_sprites.add(m)
                mobs.add(m)
                if random.random() > 0.99:
                    pow=Pow(hit.rect.center)
                    all_sprites.add(pow)
                    powerups.add(pow)

        #checks if mob hit player
        hits=pygame.sprite.spritecollide(player,mobs,True,pygame.sprite.collide_circle)
        if hits:
            for hit in hits:
                if hit.radius==62:# FIREMETEOR
                    player_explode.play()
                    explode_FIREMETEOR=Explosion(hit.rect.center,'player')
                    all_sprites.add(explode_FIREMETEOR)
                    if player.displayshield==False:
                        player.health-=35
                        if player.health <= 0:
                                player_explode.play()
                                player.health=0
                                explode_player=Explosion(player.rect.center,'player')
                                all_sprites.add(explode_player)
                                player.kill()
                    else:
                        ShieldRemaining=player.shieldbar-35
                        if ShieldRemaining <= 0:
                            player.displayshield=False
                            player.health+=ShieldRemaining
                        else:
                            player.shieldbar-=35

                else:# REGULAR METEOR
                    explode()
                    if player.displayshield==False:
                        player.health-=Mob().damage
                        if player.health <= 0:
                            player_explode.play()
                            player.health=0
                            explode_player=Explosion(player.rect.center,'player')
                            all_sprites.add(explode_player)
                            player.kill()
                    else:
                        ShieldRemaining=player.shieldbar-Mob().damage
                        if ShieldRemaining <= 0:
                            player.displayshield=False
                            player.health+=ShieldRemaining
                        else:
                            player.shieldbar-=Mob().damage

            for hit in hits:
                pickLargeOrSmallExplo(hit)
                expl=Explosion(hit.rect.center,player.explo_size)
                all_sprites.add(expl)
                m=Mob()
                all_sprites.add(m)
                mobs.add(m)

        if not player.alive() and not explode_player.alive():
            GameOver()

        all_sprites.update()
        mainscreenupdate()
        clock.tick(FPS)

Intro()
