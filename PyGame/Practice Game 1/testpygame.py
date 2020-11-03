#***************************#
# Import Nescessary Modules #
#***************************#
import pygame,sys
from pygame.locals import *
from random import randint

#**************#
# Initializers #
#**************#
pygame.init()
pygame.mixer.init()

#***********#
# FPS Setup #
#***********#
FPS=30
fpsClock=pygame.time.Clock()

#*****************************************************************************************#
# Defining the Width and Height of the Window then Defining a Variable to make the Window #
#*****************************************************************************************#
#Must be 100 apart(Can fix or add definite amount later); only here so GameOver() can be centered
displayWidth=400
displayHeight=300

DISPLAYSURF=pygame.display.set_mode((displayWidth,displayHeight))

#*********************************************************#
# Setting the Display Caption and the Icon for the Window #
#*********************************************************#
pygame.display.set_caption('Test Game!')
pygame.display.set_icon(pygame.image.load('Images\\ph34.ico'))

#*********************************************#
# Setting up and Defining Colors to use Later #
#*********************************************#
WHITE=    (255,255,255)
PURPLEISH=(200,200,255)
BLACK=    (0,0,0)
RED=      (255,0,0)
GRAY=     (128,128,128)

#**********************#
# Loading Player Image #
#**********************#
ptImg=pygame.image.load('Images\\Wizard\\Wizard.png')

# Note when using "Width" it must go with X
# Not when using "Height" it must go with Y
ptImgWidth=14
ptImgHeight=24
#ptImg dimensions = ~ 16x16 Pixels

#*********************#
# Loading Enemy Image #
#*********************#
e1_Img=pygame.image.load('Images\\pt.ico')

# Note when using "Width" it must go with X
# Not when using "Height" it must go with Y
e1_ImgWidth=16
e1_ImgHeight=16
#e1_Img dimensions = ~ 16x16 Pixels

class Wizard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w1=pygame.image.load('Images\\Wizard\\Wizard.png').convert()
        self.w1.set_colorkey(WHITE)
        self.w2=pygame.image.load('Images\\Wizard\\Wizard Walking2.png')
        self.w3=pygame.image.load('Images\\Wizard\\Wizard Walking3.png')
        self.w4=pygame.image.load('Images\\Wizard\\Wizard Walking4.png')
############################################
class Player():# Defining the Player Class #
############################################
    def __init__(self):
        self.ptx=displayWidth//2
        self.pty=displayHeight-24
        self.speed=5
        self.health=100
p=Player()

######################################
class MenuSelect():# Menu Select Bar #
######################################
    def __init__(self):
        self.x=displayWidth-82
        self.y=7
ms=MenuSelect()

#######################################
class FallingTerminal(): # Test Enemy #
#######################################
    def __init__(self):
        self.x=50#randint(0,displayWidth-e1_ImgWidth)
        self.y=50#randint(-20,-5)
        self.speed=7
        self.count=1
        self.damage=randint(randint(randint(0,1),7),randint(10,randint(11,20)))
ft=FallingTerminal()

#***********************************************************#
def StartSpawningEnemies():# Test Spawning Enemy That Falls #
#***********************************************************#
    DISPLAYSURF.blit(e1_Img,(ft.x,ft.y))
    '''
    #directions=randint(1,4)
    #if directions==1:#TOP
        ft.y+=ft.speed
        if ft.y > displayHeight + 15:
            ft.count+=randint(1,3)
            ft.x=randint(0,displayWidth-e1_ImgWidth)
            ft.y=randint(-20,-5)
            chanceSpawnOverPlayer=randint(1,randint(2,3))
            if chanceSpawnOverPlayer == 2:
                ft.x=p.ptx
            if ft.count >= 2:
                ft.count=1
                ft.speed+=2
                changeSpeed=randint(1,2)
                if changeSpeed == 2:
                    ft.speed=randint(5,7)
                    '''
    #elif directions==2:#LEFT
    #ft.x=randint(-64,-24)
    #ft.y=randint(randint(0,10),displayHeight-randint(10,30))
    ft.x+=ft.speed
    if ft.x > displayWidth + 15:
        ft.count+=randint(1,3)
        ft.x=randint(-64,-24)
        ft.y=randint(randint(0,10),displayHeight-randint(10,30))
        chanceSpawnOverPlayer=randint(1,randint(2,3))
        if chanceSpawnOverPlayer == 2:
            ft.y=p.pty
        if ft.count >= 2:
            ft.count=1
            ft.speed+=2
            changeSpeed=randint(1,2)
            if changeSpeed == 2:
                ft.speed=randint(5,7)
    '''
    elif directions==3:#RIGHT
        ft.y+=ft.speed
        if ft.y > displayHeight + 15:
            ft.count+=randint(1,3)
            ft.x=randint(0,displayWidth-e1_ImgWidth)
            ft.y=randint(-20,-5)
            chanceSpawnOverPlayer=randint(1,randint(2,3))
            if chanceSpawnOverPlayer == 2:
                ft.x=p.ptx
            if ft.count >= 2:
                ft.count=1
                ft.speed+=2
                changeSpeed=randint(1,2)
                if changeSpeed == 2:
                    ft.speed=randint(5,7)
    elif directions==4:#BOTTOM
        ft.y+=ft.speed
        if ft.y > displayHeight + 15:
            ft.count+=randint(1,3)
            ft.x=randint(0,displayWidth-e1_ImgWidth)
            ft.y=randint(-20,-5)
            chanceSpawnOverPlayer=randint(1,randint(2,3))
            if chanceSpawnOverPlayer == 2:
                ft.x=p.ptx
            if ft.count >= 2:
                ft.count=1
                ft.speed+=2
                changeSpeed=randint(1,2)
                if changeSpeed == 2:
                    ft.speed=randint(5,7)
'''
#*************************************#
def GameOver():# Self Explanatory ... #
#*************************************#

    BASICFONT=pygame.font.Font('Fonts\\PressStart2P.ttf',24)
    GameOverSurf = BASICFONT.render('GameOver',1,BLACK)
    DISPLAYSURF.blit(GameOverSurf,(displayWidth//3.5, displayHeight//2.2))

    BASICFONT=pygame.font.Font('Fonts\\PressStart2P.ttf',12)
    GameOverSurf2 = BASICFONT.render('Enter to Retry',1,BLACK)
    DISPLAYSURF.blit(GameOverSurf2,((displayWidth//3.5)+10, (displayHeight//2.2)+25))
    
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                exitGame()
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    p.health=100
                    main()
        pygame.display.update()
        fpsClock.tick(FPS)
     
#**************************************************************#
def LooseHealth():# Loose Health if Enemy Collides with Player #
#**************************************************************#
    if p.pty <= ft.y <= p.pty + ptImgHeight or p.pty <= ft.y + e1_ImgHeight <= p.pty + ptImgHeight:
        if p.ptx <= ft.x <= p.ptx + ptImgWidth or p.ptx <= ft.x + e1_ImgWidth <= p.ptx + ptImgWidth:
            p.health-=ft.damage
            print('\nHIT! at X{}'.format(ft.x))# Remove Later
            ft.x=randint(0,displayWidth-e1_ImgWidth)
            ft.y=randint(-20,-5)
            if p.health <= 0:
                GameOver()
            

#Note: integer " 16 " repesents the Length and/or Width of the Image.
#In this case it is both.
'''

        p.ptx through p.ptx + ptImgWidth    ft.x through ft.x + ptImgWidth

        p.pty through p.pty + ptImgHeight    ft.y through ft.y + ptImgHeight

                         X Increases Right -->
                         
                      X    Y          X    Y
                    (200, 380) ---- (216, 380)
                        |                |
Y Increases Down        |                |        Y Increases Down
                        |                |
                      X    Y          X    Y
                    (200, 396) ---- (216, 396)
                    
                         X Increases Right -->

'''

#***********************************************************************************#
def blockx(PlusOrMinus):# Blocks Player From Going Outside the LEFT and RIGHT Sides #
#***********************************************************************************#
    keys=pygame.key.get_pressed()
    if p.ptx>=displayWidth-ptImgWidth:
        p.ptx=displayWidth-ptImgWidth
        if keys[pygame.K_LEFT]:
            p.ptx-=p.speed
        else:
            pass
    elif p.ptx<=0:
        p.ptx=0
        if keys[pygame.K_RIGHT]:
            p.ptx+=p.speed
        else:
            pass
    else:
        if PlusOrMinus=='+':
            p.ptx+=p.speed
        elif PlusOrMinus=='-':
            p.ptx-=p.speed
        
#***********************************************************************************#
def blocky(PlusOrMinus):# Blocks Player From Going Outside the TOP and BOTTOM Sides #
#***********************************************************************************#
    keys=pygame.key.get_pressed()
    if p.pty<=-1:
        p.pty=-1
        if keys[pygame.K_DOWN]:
            p.pty+=p.speed
        else:
            pass
    elif p.pty>=displayHeight-ptImgHeight:
        p.pty=displayHeight-ptImgHeight
        if keys[pygame.K_UP]:
            p.pty-=p.speed
        else:
            pass
    else:
        if PlusOrMinus=='+':
            p.pty+=p.speed
        elif PlusOrMinus=='-':
            p.pty-=p.speed

#*****************************************#
def exitGame():# Simple ExitGame Function #
#*****************************************#
    pygame.quit()
    sys.exit()

#***************************************#
def ReturnSound():# Returns Click Sound #
#***************************************#
    click=pygame.mixer.Sound('Sound Effects\\c.ogg')
    click.set_volume(0.3)
    click.play()

#*******************************************#
def displayHealth():# Displays Health Meter #
#*******************************************#
    LooseHealth()

    healthbarBackground=pygame.draw.rect(DISPLAYSURF, GRAY, (1, 1, 100, 15))
    healthbar=pygame.draw.rect(DISPLAYSURF, RED, (1, 1, p.health, 15))

    pygame.draw.line(DISPLAYSURF, BLACK, (0, 0), (100, 0), 2)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 0), (0, 15), 2)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 15), (100, 15), 2)
    pygame.draw.line(DISPLAYSURF, BLACK, (100, 0), (100, 16), 2)

#**********************************#
def Info():# Info Option From Menu #
#**********************************#
    pass

#********************************#
def Bag():# Bag Option From Menu #
#********************************#
    pass

#**********************************#
def Save():# Save Option From Menu #
#**********************************#
    pass

#******************************************#
def Settings():# Settings Option From Menu #
#******************************************#
    pass

#**********************************#
def Help():# Help Option From Menu #
#**********************************#
    pass

#**********************************#
def Quit():# Quit Option From Menu #
#**********************************#
    Save()
    exitGame()
    pass

#*****************************************************#
def Menu():# Menu Function for Settings and Inventory #
#*****************************************************#
    while True:
        
        pygame.draw.rect(DISPLAYSURF, WHITE, (displayWidth-84, 0, displayWidth-320, 105))

        pygame.draw.line(DISPLAYSURF, BLACK, (displayWidth-84, 1), (displayWidth-4, 1), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (displayWidth-84, 1), (displayWidth-84, 105), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (displayWidth-84, 105), (displayWidth-4, 105), 4)
        pygame.draw.line(DISPLAYSURF, BLACK, (displayWidth-4, 1), (displayWidth-4, 105), 4)
        
        BASICFONT=pygame.font.Font('Fonts\\PressStart2P.ttf',8)
        menuSurf1 = BASICFONT.render('Info',1,BLACK)
        DISPLAYSURF.blit(menuSurf1,(displayWidth-69, 8))

        menuSurf2 = BASICFONT.render('Bag',1,BLACK)
        DISPLAYSURF.blit(menuSurf2,(displayWidth-69, 25))

        menuSurf3 = BASICFONT.render('Save',1,BLACK)
        DISPLAYSURF.blit(menuSurf3,(displayWidth-69, 42))

        menuSurf4 = BASICFONT.render('Settings',1,BLACK)
        DISPLAYSURF.blit(menuSurf4,(displayWidth-69, 59))

        menuSurf5 = BASICFONT.render('Help',1,BLACK)
        DISPLAYSURF.blit(menuSurf5,(displayWidth-69, 76))

        menuSurf6 = BASICFONT.render('Quit',1,BLACK)
        DISPLAYSURF.blit(menuSurf6,(displayWidth-69, 93))

        MenuSelectBar=pygame.image.load('Images\\menuselectbar.png')
        DISPLAYSURF.blit(MenuSelectBar,(ms.x,ms.y))

                    #^^^ Goes up by increments of 17  ^^^#
        #Y Positions =[8=info 25=bag 42=save 59=settings help=76 quit=93]


        for event in pygame.event.get():
            if event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    main()
                if event.key==K_DOWN:
                    if ms.y==92:
                        ms.y=7
                    else:
                        ms.y+=17
                        
                elif event.key==K_UP:
                    if ms.y==7:
                        ms.y=92
                    else:
                        ms.y-=17
                        
                elif event.key==K_RETURN and ms.y==7:
                    ReturnSound()
                    Info()
                elif event.key==K_RETURN and ms.y==24:
                    ReturnSound()
                    Bag()
                elif event.key==K_RETURN and ms.y==41:
                    ReturnSound()
                    Save()
                elif event.key==K_RETURN and ms.y==58:
                    ReturnSound()
                    Settings()
                elif event.key==K_RETURN and ms.y==75:
                    ReturnSound()
                    Help()
                elif event.key==K_RETURN and ms.y==92:
                    ReturnSound()
                    Quit()

                        #^^^ Goes up by increments of 17  ^^^#
            #Y Positions =[7=info 24=bag 41=save 58=settings help=75 quit=92]
                    
            print(event)# Remove Later
                    
        pygame.display.update()
        fpsClock.tick(FPS)

######################################
def main():# Main Game Function/Loop #
######################################
    while True:
        
        DISPLAYSURF.fill(PURPLEISH)
        
        DISPLAYSURF.blit(ptImg,(p.ptx,p.pty))

        displayHealth()

        StartSpawningEnemies()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            blocky('-')
        if keys[pygame.K_DOWN]:
            blocky('+')
        if keys[pygame.K_LEFT]:
            blockx('-')
        if keys[pygame.K_RIGHT]:
            blockx('+')
            
        if keys[pygame.K_g]:
            GameOver()
            
        if keys[pygame.K_o]:
            p.speed-=4
        if keys[pygame.K_p]:
            p.speed+=4
        if keys[pygame.K_l]:
            p.speed=5
        
        for event in pygame.event.get():
            if event.type==QUIT:
                exitGame()
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    Menu()
                    
            print(event)# Remove Later
                

        pygame.display.update()
        fpsClock.tick(FPS)


main()
