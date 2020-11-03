import sys
import time
from random import randint
import pygame
pygame.mixer.init()


###########
# WEAPONS #
###########
class Weapon:# SUPER CLASS
    def __init__(self):
        raise NotImplementedError('Do not create raw weapon objects.')

    def __str__(self):
        return self.name

class Fists(Weapon):
    def __init__(self):
        self.type='Natural'
        self.name='Pair of Fists'
        self.des='If all else fails, use your fists!'
        self.dam=13
        self.level=1

class Rusty_Copper_Pistol(Weapon):
    def __init__(self):
        self.type='Gun'
        self.name='Rusty Copper Pistol'
        self.des='Think of it as an overpowered slingshot.'
        self.dam=18
        self.price=10
        self.sp=5# sell price
        self.level=1

class Copper_Pistol(Weapon):
    def __init__(self):
        self.type='Gun'
        self.name='Copper Pistol'
        self.des='No signs of rust..\nThink of it as an overpowered slingshot.'
        self.dam=25
        self.price=20
        self.sp=15
        self.level=1

class Revolver(Weapon):
    def __init__(self):
        self.type='Gun'
        self.name='Revolver'
        self.des='Has a few scratches, but still retains its silver shine...\nThe clicking noise of spinning the chamber\nbrings you pleasure...'
        self.dam=50
        self.price=75
        self.sp=45
        self.level=1

class BRS(Weapon):
    def __init__(self):
        self.type='Sword'
        self.name='Blured Sword'
        self.des='A blue and red one-haned sword. Its blade takes on\nthe dull red color while the rest is a regular blue color.' \
                  '\n\n...Why does it seem so...familiar?'
        self.dam=33
        self.price=45
        self.sp=25
        self.level=1

###############
# CONSUMABLES #
###############
class Consumable:# SUPER CLASS
    def __init__(self):
        raise NotImplementedError('Do not create raw concumable objects.')

    def __str__(self):
        return self.name

class Kabob(Consumable):
    def __init__(self):
        self.type='Consumable'
        self.name='Kabob'
        self.des='Visually appealing and home-made. Every bite takes\nyou back home.'
        self.hv=35# healing value
        self.price=15
        self.sp=10

class Falafel(Consumable):
    def __init__(self):
        self.type='Consumable'
        self.name='Falafel'
        self.des='Another home-made item made by mom.'
        self.hv=15
        self.price=10
        self.sp=5

class LeftOvers(Consumable):
    def __init__(self):
        self.type='Consumable'
        self.name='LeftOvers'
        self.des='Looks appetizing!'
        self.hv=5
        self.price=5
        self.sp=3

#############################
class Player:# PLAYER CLASS #
#############################
    def __init__(self):
        self.name=None
        self.maxhp=100
        self.hp=100
        self.hhv=0# highest healing values
        self.inventory=[Rusty_Copper_Pistol(),Kabob(),Falafel()]
        self.xp=0
        self.xpbar='[                  ]'
        self.xxp=0# extra xp after reaching 80 xp to level up. will transfer it to the xpbar of the next level
        self.level=1
        self.bw=None # best weapon in inventory
        self.money=10
        self.ee=0# enemy encounters
        self.ed=0# enemies defeated
        self.x=1
        self.y=0

    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def move_north(self):
        self.move(dx=0,dy=-1)

    def move_south(self):
        self.move(dx=0,dy=1)

    def move_east(self):
        self.move(dx=1,dy=0)

    def move_west(self):
        self.move(dx=-1,dy=0)

    ###################################
    def pi(self):# PRINT BAG FUNCTION #
    ###################################
        print('\nBag: ')
        if self.inventory==[]:
            printa('\n[ EMPTY ]',0.5,0.01)
        else:
            pass
        k=-1
        for i in self.inventory:
            k+=1
            print('\n' + '[' + str(k) + ']' + str(i))
            self.bw=self.most_powerful_weapon()
        print('\n\nYou will automatically use your\nbest weapon, [ {} ]'.format(self.bw))

    ################################################################
    def most_powerful_weapon(self):# MOST POWERFUL WEAPON FUNCTION #
    ################################################################
        t=[item for item in self.inventory if isinstance(item,Weapon)]
        if not t:
            self.bw=Fists()
        else:
            md=0# max damage
            for i in self.inventory:
                try:
                    if i.dam > md:
                        self.bw = i
                        md=i.dam
                except AttributeError:
                    pass
        return self.bw

    ################################
    def heal(self):# HEAL FUNCTION #
    ################################
        while True:
            print(79*'=')
            consumables=[item for item in self.inventory if isinstance(item,Consumable)]
            if not consumables:
                printa('You don\'t have any items to heal you!\n',0.5,0.01)
                break

            printa('\nChoose an item to heal with:\n',0.5,0.01)
            for i,item in enumerate(consumables):
                print('\n[{}]{}\t[Healing Value] +{} HP'.format(i,item,item.hv))
            print('\n\t\t\t\t\t\t\t*[{} {}/{}HP]'.format(p.name,p.hp,p.maxhp))
            print('\n' + (79*'='))
            print('\nB [Back]')
            choice=input('\n[B/0-{}]: '.format(int(len(consumables)-1)))
            click()

            choice_int_list=[]

            for k in range(0,int(len(consumables))):
                choice_int_list.append(str(k))

            if choice in choice_int_list:

                if self.hp==self.maxhp:
                    print(79*'=')
                    printa('You\'re already at max health!\n',0.6,0.01)
                    break
                else:
                    try:
                        te=consumables[int(choice)]# to eat
                        printa('\nYou used {} to heal +{}HP!'.format(te.name,te.hv),0.5,0.01)
                        if te.hv + self.hp > self.maxhp:
                            printa('\nHowever, +{} HP of the {} has been wasted...'.format(te.hv + self.hp - self.maxhp,te.name),0.5,0.01)
                        self.hp=min(self.maxhp,self.hp+te.hv)# " min() " caps HP at player's max HP
                        self.inventory.remove(te)
                        print('\n\n[Current HP]: {}'.format(self.hp))
                        input('\n[Return]: ')
                        click()
                        if self.hp==self.maxhp:
                            break
                    except (ValueError, IndexError):
                        print(79*'=')
                        print('[ INVLAID KEY ]')
                        continue

            elif choice in ['b','B','back','Back']:
                break

            else:
                print(79*'=')
                print('[ INVLAID KEY ]')
                continue

    def __str__(self):
        return self.name

p=Player()

#################################
# Other Stuff not Organized Yet #
#################################
class TT:
    def __init__(self):
        self.type='???'
        self.name='Train Ticket'
        self.des='An odd item to have....It\'s not sellable after purchase\nMaybe {} knows how to use it...?'.format(p.name)
        self.price=30

    def __str__(self):
        return self.name

###########
# ENEMIES #
###########
class Enemy:# SUPER CLASS
    def __init__(self):
        self.attacks=['basic attack','heavy attack']
        raise NotImplementedError('Do not create raw enemy objects.')

    def __str__(self):
        return self.ades# approach description

class Slime(Enemy):
    def __init__(self):
        self.name='Slime'
        self.ades='gLoP...GLoP..gLoP.glOp.GLOP\nA slime approaches.'
        self.hp=100
        self.dam=5
        self.hdam=10
        self.inventory=[]
        self.money=10
        self.xpd=15#xp drop

class GiantSpider(Enemy):
    def __init__(self):
        self.name='Giant Spider'
        self.ades='AgiantSPIDERapproachesFAST'
        self.hp=35
        self.dam=7
        self.hdam=13
        self.inventory=[]
        self.money=5
        self.xpd=5

class Ogre(Enemy):
    def __init__(self):
        self.name='Ogre'
        self.ades='THUD! THUD! THUD! An Ogre stands in front of you.'
        self.hp=57
        self.dam=10
        self.hdam=15
        self.inventory=[]
        self.money=5
        self.xpd=10

class BatColony(Enemy):
    def __init__(self):
        self.name='Colony of bats'
        self.ades='sqeakSQUEAKsQeAK! A huge Colony of bats awakes from their\nslumber, their anger is ' \
                   'directed towards you!'
        self.hp=100
        self.dam=8
        self.hdam=14
        self.inventory=[]
        self.money=5
        self.xpd=15

class RockMonster(Enemy):
    def __init__(self):
        self.name='Rock Monster'
        self.ades='The beautiful rock formations make the ground tremble, they\'ve\npulled together to form ' \
                   'a towering Rock Monster!'
        self.hp=114
        self.dam=15
        self.hdam=20
        self.inventory=[]
        self.money=20
        self.xpd=25

class BOSS_Ogre(Enemy):
    def __init__(self):
        self.name='Boss Ogre'
        self.ades='THUD! THUD! THUD! THUD! A Boss Ogre stands before you.'
        self.hp=200
        self.dam=25
        self.hdam=30
        self.inventory=[]
        self.money=30
        self.xpd=75
        self.trip=-1

class goblin(Enemy):
    def __init__(self):
        self.name='goblin'
        self.ades='A small goblin approaches wearing a large rucksack...\nIts contents entrigue you..'
        self.hp=300
        self.dam=2
        self.hdam=20
        self.inventory=[]
        self.money=40
        self.xpd=20
        self.trip=-1

# NON-ENEMIES

class Friendlies():# SUPER CLASS
    def __str__(self):
        return self.name

#############################################
class Trader_Jack(Friendlies):# TRADER CLASS#
#############################################
    def __init__(self):
        self.name='Trader Jack'
        self.inventory=[Copper_Pistol(),LeftOvers(),LeftOvers(),LeftOvers(),Kabob(),Kabob(),Kabob(),Falafel(),Falafel(),Falafel()]
        self.bb=[]# Jack's Buy Back Inventory, let's you buy back any items you sold. But will clear when you leave

TJ=Trader_Jack()
############################################
def spawnTJ():# SPAWN TRADER JACK FUNCTION #
############################################
    if p.ed > 9:
        stj=randint(randint(3,4),randint(7,8))# chance to spawn TJ
    elif p.ed==9:# Will spawn Trader Jack when the player has killed 10 enemies
        stj=7

    elif p.ed==10:# no chance of spawning after a couple of enemies defeated
        stj=0
    elif p.ed==11:
        stj=0

    else:
        stj=0# CHANGE THIS TO 7 IF TESTING #
    if stj == 7:
        print('\n\n' + (79*'='))
        printa('\n!You encounter a fidgity old man clinking two coins together..\nHe looks willing to trade!',0.5,0.02)
        print('\n\n' + (79*'='))
        sw=randint(1,4)
        if sw==2:
            TJ.inventory.append(TT())
            printa('I have something special today...\n',0.5,0.01)
        else:
            pass
        while True:
            print(79*'=')
            printa('\n\t\t\t\t[ Trader Jack\'s Shop ]',0.5,0.01)
            printa('\n\n\nB [Buy]   S [Sell]   BB [Buy Back]   L [Lotto]   G [Goodbye]',0.01,0.01)
            tjmm=input('\n[B/S/BB/L/G]: ') # trader jack main menu
            click()
            #############################################
            if tjmm in ['b','B','buy','Buy']:#BUY OPTION#
            #############################################
                while True:
                    print(79*'=')
                    print('\n\t\t\t\t[ GOODS ]: ')
                    k=-1
                    for i in TJ.inventory:
                        k+=1
                        try:
                            if i.name in ['Train Ticket']:
                                print('\n[Special Item(s)]')
                                if i.price < 10:# 1 digit
                                    print('\n   ' + str(i.price) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                                elif i.price < 100:# 2 digit
                                    print('\n  ' + str(i.price) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                            else:
                                if i.price < 10:# 1 digit
                                    print('\n   ' + str(i.price) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                                elif i.price < 100:# 2 digit
                                    print('\n  ' + str(i.price) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                        except:
                            pass

                    print('\n\t\t\t\t\t\t\t*[{} {}/{}HP ]\n\t\t\t\t\t\t\t*[Gold: {} ]'.format(p.name,p.hp,p.maxhp,p.money))
                    print(79*'=')
                    print('\nB [Back]')
                    tjo=input('\n[B/[0-{}]]: '.format(int(len(TJ.inventory)-1))) # trader jack options
                    click()

                    tjo_int_list=[]
                    for k in range(0,int(len(TJ.inventory))):
                        tjo_int_list.append(str(k))

                    if tjo in tjo_int_list:
                        try:
                            print(79*'=')
                            print('\n\t\t\t[{} Description]'.format(TJ.inventory[int(tjo)].name))
                            try:
                                print('\n[Level]: ' + str(TJ.inventory[int(tjo)].level))
                            except:
                                pass
                            try:
                                printa('\n[Type]: ' + TJ.inventory[int(tjo)].type,0.01,0.01)
                            except:
                                pass
                            try:
                                printa('\n[Healing Value]: ' + str(TJ.inventory[int(tjo)].hv),0.01,0.01)
                            except:
                                pass
                            try:
                                printa('\n[Damage]: ' + str(TJ.inventory[int(tjo)].dam),0.01,0.01)
                            except:
                                pass
                            try:
                                printa('\n[Price]: ' + str(TJ.inventory[int(tjo)].price),0.01,0.01)
                            except:
                                pass
                            printa('\n\n' + TJ.inventory[int(tjo)].des,0.5,0.01)
                            print('\n' + (79*'='))
                            while True:
                                printa('\nB [Back]   P [Purchase Item]',0.5,0.01)
                                io=input('\n[B/P]: ')# item options
                                click()
                                if io in ['p','P','purchase','Purchase']:
                                    if p.money < TJ.inventory[int(tjo)].price:
                                        print(79*'=')
                                        printa('You don\'t have enough Gold to buy this!\n',0.5,0.01)
                                        print(79*'=')

                                        print('\n\t\t\t[{} Description]'.format(TJ.inventory[int(tjo)].name))
                                        try:
                                            print('\n[Level]: ' + str(TJ.inventory[int(tjo)].level))
                                        except:
                                            pass
                                        try:
                                            print('\n[Type]: ' + TJ.inventory[int(tjo)].type)
                                        except:
                                            pass
                                        try:
                                            print('\n[Healing Value]: ' + str(TJ.inventory[int(tjo)].hv))
                                        except:
                                            pass
                                        try:
                                            print('\n[Damage]: ' + str(TJ.inventory[int(tjo)].dam))
                                        except:
                                            pass
                                        try:
                                            print('\n[Price]: ' + str(TJ.inventory[int(tjo)].price))
                                        except:
                                            pass
                                        print('\n\n' + TJ.inventory[int(tjo)].des)
                                        print('\n' + (79*'='))
                                        continue
                                    elif p.money >= TJ.inventory[int(tjo)].price:
                                        printa('\nPurchase [ {} ]?'.format(TJ.inventory[int(tjo)].name),0.5,0.01)
                                        agtp=input('\n[Y/N]: ')# ask again to purchase
                                        click()
                                        if agtp in ['y','Y','yes','Yes']:
                                            printa('\n\n{} Purchased [ {} ] for {} G!\n' \
                                                   .format(p.name,TJ.inventory[int(tjo)],TJ.inventory[int(tjo)].price),0.5,0.01)
                                            p.inventory.append(TJ.inventory[int(tjo)])
                                            p.money-=TJ.inventory[int(tjo)].price
                                            del TJ.inventory[int(tjo)]
                                            break
                                        elif agtp in ['n','N','no','No']:
                                            break
                                        else:
                                            print(79*'=')
                                            print('[ INVALID KEY ]')
                                            print(79*'=')
                                            print('\n\t\t\t[{} Description]'.format(TJ.inventory[int(tjo)].name))
                                            try:
                                                print('\n[Level]: ' + str(TJ.inventory[int(tjo)].level))
                                            except:
                                                pass
                                            try:
                                                print('\n[Type]: ' + TJ.inventory[int(tjo)].type)
                                            except:
                                                pass
                                            try:
                                                print('\n[Healing Value]: ' + str(TJ.inventory[int(tjo)].hv))
                                            except:
                                                pass
                                            try:
                                                print('\n[Damage]: ' + str(TJ.inventory[int(tjo)].dam))
                                            except:
                                                pass
                                            try:
                                                print('\n[Price]: ' + str(TJ.inventory[int(tjo)].price))
                                            except:
                                                pass
                                            print('\n\n' + TJ.inventory[int(tjo)].des)
                                            print('\n' + (79*'='))
                                            continue
                                elif io in ['b','B','back','Back']:
                                    break
                                else:
                                    print(79*'=')
                                    print('[ INVALID KEY ]')
                                    print(79*'=')
                                    continue
                        except:
                            break

                    elif tjo in ['b','B','back','Back']:
                        break

                    else:
                        print(79*'=')
                        print('[ INVALID KEY ]')
                        continue
            ##################################################
            elif tjmm in ['s','S','sell','Sell']:#SELL OPTION#
            ##################################################
                if p.inventory==[]:
                    print(79*'=')
                    printa('You have nothing to sell!\n',0.01,0.01)
                    continue
                while True:
                    print(79*'=')
                    print('\n\t\t\t\t[BAG]: ')
                    k=-1
                    for i in p.inventory:
                        k+=1
                        try:
                            if i.sp < 10:# 1 digit
                                print('\n   ' + str(i.sp) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                            elif i.sp < 100:# 2 digit
                                print('\n  ' + str(i.sp) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                        except:
                            pass

                    print('\n\t\t\t\t\t\t\t*[{} {}/{}HP ]\n\t\t\t\t\t\t\t*[Gold: {} ]'.format(p.name,p.hp,p.maxhp,p.money))
                    print(79*'=')
                    print('\nB [Back]')
                    tjo=input('\n[B/[0-{}]]: '.format(int(len(p.inventory)-1))) # trader jack options
                    click()

                    tjo_int_list=[]
                    for k in range(0,int(len(p.inventory))):
                        tjo_int_list.append(str(k))

                    if tjo in tjo_int_list:
                        try:
                            print(79*'=')
                            print('\n\t\t\t[{} Description]'.format(p.inventory[int(tjo)].name))
                            try:
                                print('\n[Level]: ' + str(p.inventory[int(tjo)].level))
                            except:
                                pass
                            try:
                                print('\n[Type]: ' + p.inventory[int(tjo)].type)
                            except:
                                pass
                            try:
                                print('\n[Healing Value]: ' + str(p.inventory[int(tjo)].hv))
                            except:
                                pass
                            try:
                                print('\n[Damage]: ' + str(p.inventory[int(tjo)].dam))
                            except:
                                pass
                            try:
                                print('\n[Sell Price]: ' + str(p.inventory[int(tjo)].sp))
                            except:
                                pass
                            print('\n' + p.inventory[int(tjo)].des)
                            print('\n' + (79*'='))
                            while True:
                                printa('\nB [Back]   S [Sell Item]',0.5,0.01)
                                io=input('\n\n[B/S]: ')# item options
                                click()
                                if io in ['s','S','sell','Sell']:
                                    ciow=[item for item in p.inventory if isinstance(item,Weapon)]# check if the player is selling their only weapon
                                    try:
                                        if len(ciow)==1 and p.inventory[int(tjo)]==ciow[0]:
                                            printa('\nAre you sure you want to sell your only weapon, [ {} ]?' \
                                                   .format(ciow[0].name),0.5,0.01)
                                            ai=input('\n[Y/N]: ')#ask input, yes or no
                                            click()
                                            if ai in ['y','Y','yes','Yes']:
                                                printa('\n\n{} sold [ {} ] for {} G!\n' \
                                                       .format(p.name,p.inventory[int(tjo)],p.inventory[int(tjo)].sp),0.7,0.01)
                                                TJ.bb.append(p.inventory[int(tjo)])
                                                p.money+=p.inventory[int(tjo)].sp
                                                del p.inventory[int(tjo)]
                                                break
                                            elif ai in ['n','N','no','No']:
                                                break
                                            else:
                                                print(79*'=')
                                                print('[ INVALID KEY ]')
                                                print(79*'=')
                                                print('\n\t\t\t[{} Description]'.format(p.inventory[int(tjo)].name))
                                                try:
                                                    print('\n[Level]: ' + str(p.inventory[int(tjo)].level))
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Type]: ' + p.inventory[int(tjo)].type)
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Healing Value]: ' + str(p.inventory[int(tjo)].hv))
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Damage]: ' + str(p.inventory[int(tjo)].dam))
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Sell Price]: ' + str(p.inventory[int(tjo)].sp))
                                                except:
                                                    pass
                                                print('\n' + p.inventory[int(tjo)].des)
                                                print('\n' + (79*'='))
                                                continue
                                        else:
                                            printa('\nSell [ {} ]?'.format(p.inventory[int(tjo)].name),0.5,0.01)
                                            agts=input('\n[Y/N]: ')# ask again to sell
                                            click()
                                            if agts in ['y','Y','yes','Yes']:
                                                printa('\n\n{} sold [ {} ] for {} G!\n' \
                                                        .format(p.name,p.inventory[int(tjo)],p.inventory[int(tjo)].sp),0.7,0.01)
                                                TJ.bb.append(p.inventory[int(tjo)])
                                                p.money+=p.inventory[int(tjo)].sp
                                                del p.inventory[int(tjo)]
                                                break
                                            elif agts in ['n','N','no','No']:
                                                break
                                            else:
                                                print(79*'=')
                                                print('[ INVALID KEY ]')
                                                print(79*'=')
                                                print('\n\t\t\t[{} Description]'.format(p.inventory[int(tjo)].name))
                                                try:
                                                    print('\n[Level]: ' + str(p.inventory[int(tjo)].level))
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Type]: ' + p.inventory[int(tjo)].type)
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Healing Value]: ' + str(p.inventory[int(tjo)].hv))
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Damage]: ' + str(p.inventory[int(tjo)].dam))
                                                except:
                                                    pass
                                                try:
                                                    print('\n[Sell Price]: ' + str(p.inventory[int(tjo)].sp))
                                                except:
                                                    pass
                                                print('\n' + p.inventory[int(tjo)].des)
                                                print('\n' + (79*'='))
                                                continue
                                    except:
                                        pass

                                    else:
                                        break
                                elif io in ['b','B','back','Back']:
                                    break
                                else:
                                    print(79*'=')
                                    print('[ INVALID KEY ]')
                                    print(79*'=')
                                    continue
                        except:
                            break

                    elif tjo in ['b','B','back','Back']:
                        break

                    else:
                        print(79*'=')
                        print('[ INVALID KEY ]')
                        continue
            #########################################################
            elif tjmm in ['bb','BB','buy back','Buy Back']:#BUY BACK#
            #########################################################
                if TJ.bb==[]:
                    print(79*'=')
                    printa('There\'s nothing to Buy Back!\n',0.01,0.01)
                    continue
                while True:
                    print(79*'=')
                    print('\n\t\t\t\t[BUY BACK]: ')
                    k=-1
                    for i in TJ.bb:
                        k+=1
                        try:
                            if i.sp < 10:# 1 digit
                                print('\n   ' + str(i.sp) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                            elif i.sp < 100:# 2 digit
                                print('\n  ' + str(i.sp) + ' G' + '  |  ','[' + str(k) + ']' + str(i))
                        except:
                            pass

                    print('\n\t\t\t\t\t\t\t*[{} {}/{}HP ]\n\t\t\t\t\t\t\t*[Gold: {} ]'.format(p.name,p.hp,p.maxhp,p.money))
                    print('\n\n' + (79*'='))
                    print('\nB [Back]')
                    tjo=input('\n[B/[0-{}]]: '.format(int(len(TJ.bb)-1))) # trader jack options
                    click()

                    tjo_int_list=[]
                    for k in range(0,int(len(TJ.bb))):
                        tjo_int_list.append(str(k))

                    if tjo in tjo_int_list:
                        printa('\nBuy Back [ {} ]?'.format(TJ.bb[int(tjo)]),0.01,0.01)
                        atbb=input('\n\n[Y/N]: ')# ask to buy back
                        click()
                        if atbb in ['y','Y','yes','Yes']:
                            if p.money < TJ.bb[int(tjo)].sp:
                                printa('\nYou don\'t have enough Gold to buy this!\nTry selling somethings you bought.\n',0.01,0.01)
                                continue
                            else:
                                printa('\n\nBought back [ {} ].'.format(TJ.bb[int(tjo)]),0.01,0.01)
                                p.inventory.append(TJ.bb[int(tjo)])
                                p.money-=TJ.bb[int(tjo)].sp
                                p.inventory.append(TJ.bb[int(tjo)])
                                del TJ.bb[int(tjo)]
                                if TJ.bb==[]:
                                    print('\n' + (79*'='))
                                    printa('There\'s nothing to Buy Back...\n',0.01,0.01)
                                    break
                                else:
                                    continue

                    elif tjo in ['b','B','back','Back']:
                        break

                    else:
                        print(79*'=')
                        print('[ INVALID KEY ]')
                        continue
            ###################################################
            elif tjmm in ['g','G','goodbye','Goodbye']:# EXIT #
            ###################################################
                printa('\n\nGoodbye!\n\nHopefully you get to see him again..',0.5,0.01)
                TJ.inventory=[Copper_Pistol(),LeftOvers(),LeftOvers(),LeftOvers(),Kabob(),Kabob(),Kabob(),Falafel(),Falafel(),Falafel()]
                TJ.bb=[]
                break
            ################################################
            elif tjmm in ['l','L','lotto','Lotto']:# LOTTO #
            ################################################
                Lotto()
            else:
                print(79*'=')
                print('[ INVALID KEY ]')
                continue

##############################
def Lotto():# LOTTO FUNCTION ## Maybe add more stuff later #
##############################
    print(79*'=')
    printa('\n\t\t\t\t[LOTTO]',0.5,0.01)
    while True:
        print('\n\t\t\t\t\t\t\t\t*[Gold: {}]\nB [Back]   C [Chance] | 1 G'.format(p.money))
        li=input('\n[B/C]: ')# lotto input
        click()
        if li in ['b','B','back','Back']:
            break
        elif li in ['c','C','chance','Chance']:
            if p.money < 1:
                print(79*'=')
                printa('You don\'t have enough gold to chance!\n',0.5,0.01)
                print(79*'=')
                continue
            printa('- 1 G',0.5,0.01)
            p.money-=1
            printa('\nChancing..',0.5,0.01)
            chance=randint(1,50)
            if chance in [1,2,3,4,5]:
                printa('\nYou\'ve won [ {} ]!'.format(LeftOvers()),0.5,0.05)
                p.inventory.append(LeftOvers())
                continue
            elif chance in [11,12]:
                printa('\nYou\'ve won [ {} ]!'.format(Falafel()),0.5,0.05)
                p.inventory.append(Falafel())
                continue
            elif chance in [12,14]:
                printa('\nYou\'ve won 2*[ {} ]!'.format(Kabob()),0.5,0.05)
                p.inventory.append(Kabob())
                p.inventory.append(Kabob())
                continue
            elif chance in [15]:
                printa('\nYou\'ve won a Special item, [ {} ]!'.format(TT()),0.5,0.05)
                p.inventory.append(TT())
                continue
            else:
                printa('\nTry again!',0.5,0.01)
                continue
        else:
            print(79*'=')
            print('[ INVALID KEY ]')
            print(79*'=')
            continue

##########################
def Bag():# BAG FUNCTION #
##########################
    while True:
        print(79*'=')
        printa('\n\t\t\t\t[BAG]',0.5,0.01)
        p.pi()# prints bag inventory
        try:
            DFR=p.ed/p.ee# Defeated enemies over Enemies Encountered Ratio (F means Flee, reason for " DFR "
                         #best ratio is ~.50-100% which is always defeating enmies when you encounter them.
        except ZeroDivisionError:
            DFR='Error'
        if DFR=='Error':# For Bag testing #
            print('\nLvl.[%d] EXP [%d/80]%s\nEnemies Defeated    [ %d ]\t\t\t\t*[%s %d/%dHP]\nEnemies Encountered [ %d ]' \
                  '\t\t\t\t*[Gold: %d]\nD/E Ratio [ %s ]' \
                  %(p.level,p.xp,p.xpbar,p.ed,p.name,p.hp,p.maxhp,p.ee,p.money,DFR))
        else:
            # Fixes the movement of the EXP Bar if the number is two digits #
            if len(str(p.xp))==2:
                print('\nLvl.[%d] EXP [%d/80]%s\nEnemies Defeated    [ %d ]\t\t\t\t*[%s %d/%dHP]\nEnemies Encountered [ %d ]' \
                      '\t\t\t\t*[Gold: %d]\nD/E Ratio [ %4.2f ]' \
                      %(p.level,p.xp,p.xpbar,p.ed,p.name,p.hp,p.maxhp,p.ee,p.money,DFR))
            else:
                print('\nLvl.[%d] EXP [ %d/80]%s\nEnemies Defeated    [ %d ]\t\t\t\t*[%s %d/%dHP]\nEnemies Encountered [ %d ]' \
                      '\t\t\t\t*[Gold: %d]\nD/E Ratio [ %4.2f ]' \
                      %(p.level,p.xp,p.xpbar,p.ed,p.name,p.hp,p.maxhp,p.ee,p.money,DFR))
        print(79*'=')
        print('\nB [Back]   H [Heal]')
        if int(len(p.inventory)-1) == -1:
            bo=str(input('\n[B/H]: '))# bag options
            click()
        else:
            bo=str(input('\n[B/[0-{}]/H]: '.format(int(len(p.inventory)-1))))
            click()

        bo_int_list=[]
        for k in range(0,int(len(p.inventory))):
            bo_int_list.append(str(k))

        if bo in bo_int_list:
            try:
                print(79*'=')
                print('\n\t\t\t[{} Description]'.format(p.inventory[int(bo)].name))
                try:
                    print('\n[Level]: ' + str(p.inventory[int(bo)].level))
                except:
                    pass
                try:
                    printa('\n[Type]: ' + p.inventory[int(bo)].type,0.01,0.01)
                except:
                    pass
                try:
                    printa('\n[Healing Value]: ' + str(p.inventory[int(bo)].hv),0.01,0.01)
                except:
                    pass
                try:
                    printa('\n[Damage]: ' + str(p.inventory[int(bo)].dam),0.01,0.01)
                except:
                    pass
                printa('\n\n' + p.inventory[int(bo)].des,0.5,0.01)
                print('\n\n' + (79*'='))
                while True:
                    if p.inventory[int(bo)].type in ['Gun','Sword']:# If more types are added, put them in here too for upgrades
                        printa('\nB [Back]   T [Trash Item]   U [Upgrade]',0.5,0.01)
                        io=input('\n[B/T/U]: ')
                        click()
                    else:
                        printa('\n\nB [Back]   T [Trash Item]',0.5,0.01)
                        io=input('\n[B/T]: ')# item options
                        click()
                    if io in ['t','T','trash','Trash','trash item','Trash Item']:

                        ciow=[item for item in p.inventory if isinstance(item,Weapon)]# check if the player is trashing their only weapon
                        try:
                            if len(ciow)==1 and p.inventory[int(bo)]==ciow[0]:
                                printa('\n\nAre you sure you want to Trash your only weapon, [ {} ]?' \
                                        .format(ciow[0].name),0.5,0.01)
                                ai=input('\n\n[Y/N]: ')#ask input, yes or no
                                if ai in ['y','Y','yes','Yes']:
                                    printa('\nTrashing..\n',0.5,0.01)
                                    del p.inventory[int(bo)]
                                    del bo_int_list[int(bo)]
                                    break
                                elif ai in ['n','N','no','No']:
                                    print(79*'=')
                                    print('\n\t\t\t[{} Description]'.format(p.inventory[int(bo)].name))
                                    try:
                                        print('\n[Level]: ' + str(p.inventory[int(bo)].level))
                                    except:
                                        pass
                                    try:
                                        print('\n[Type]: ' + p.inventory[int(bo)].type)
                                    except:
                                        pass
                                    try:
                                        print('\n[Healing Value]: ' + str(p.inventory[int(bo)].hv))
                                    except:
                                        pass
                                    try:
                                        print('\n[Damage]: ' + str(p.inventory[int(bo)].dam))
                                    except:
                                        pass
                                    print('\n\n' + p.inventory[int(bo)].des)
                                    print('\n' + (79*'='))
                                    continue
                                else:
                                    print(79*'=')
                                    print('[ INVALID KEY ]')
                                    print(79*'=')
                                    print('\n\t\t\t[{} Description]'.format(p.inventory[int(bo)].name))
                                    try:
                                        print('\n[Level]: ' + str(p.inventory[int(bo)].level))
                                    except:
                                        pass
                                    try:
                                        print('\n[Type]: ' + p.inventory[int(bo)].type)
                                    except:
                                        pass
                                    try:
                                        print('\n[Healing Value]: ' + str(p.inventory[int(bo)].hv))
                                    except:
                                        pass
                                    try:
                                        print('\n[Damage]: ' + str(p.inventory[int(bo)].dam))
                                    except:
                                        pass
                                    print('\n\n' + p.inventory[int(bo)].des)
                                    print('\n' + (79*'='))
                                    continue
                            else:
                                printa('\nTrash the item [ {} ]?'.format(p.inventory[int(bo)].name),0.5,0.01)
                                agtt=input('\n[Y/N]: ')# ask again to trash
                                click()
                                if agtt in ['y','Y','yes','Yes']:
                                    printa('\nTrashing..\n',0.5,0.01)
                                    del p.inventory[int(bo)]
                                    del bo_int_list[int(bo)]
                                    break
                                elif agtt in ['n','N','no','No']:
                                    break
                                else:
                                    print(79*'=')
                                    print('[ INVALID KEY ]')
                                    print(79*'=')
                                    print('\n\t\t\t[{} Description]'.format(p.inventory[int(bo)].name))
                                    try:
                                        print('\n[Level]: ' + str(p.inventory[int(bo)].level))
                                    except:
                                        pass
                                    try:
                                        print('\n[Type]: ' + p.inventory[int(bo)].type)
                                    except:
                                        pass
                                    try:
                                        print('\n[Healing Value]: ' + str(p.inventory[int(bo)].hv))
                                    except:
                                        pass
                                    try:
                                        print('\n[Damage]: ' + str(p.inventory[int(bo)].dam))
                                    except:
                                        pass
                                    print('\n\n' + p.inventory[int(bo)].des)
                                    print('\n\n' + (79*'='))
                                    continue
                        except:
                            pass

                    elif io in ['b','B','back','Back']:
                        break

                    #############################################################################################################
                    elif io in ['u','U','upgrade','Upgrade'] and p.inventory[int(bo)].type in ['Gun','Sword']:# UPGRADE WEAPONS #
                    #############################################################################################################

                    #*******************************************************************************************#
                    # Note: Find a way to make items seperate so the player won't pick up the same level weapon #
                    #*******************************************************************************************#

                        if p.inventory[int(bo)].level==5:
                            print(79*'=')
                            printa('[ {} ] is at Max Level!\n'.format(p.inventory[int(bo)]),0.5,0.01)
                            print(79*'=')
                            continue
                        print(79*'=')
                        print('\n\t\t\t[{}] Upgrade'.format(p.inventory[int(bo)].name))
                        print('\n[Level]: {}'.format(str(int(p.inventory[int(bo)].level))))
                        try:
                            printa('\n[Damage]: {} + {}'
                                   .format(str(int(p.inventory[int(bo)].dam)),str(int(p.inventory[int(bo)].dam//5.75))),0.05,0.01)
                            printa('\n\n{} G'.format(int(p.inventory[int(bo)].dam//1.40)),0.5,0.01)
                        except:
                            pass
                        print('\n\t\t\t\t\t\t\t\t*[Gold: {}]'.format(p.money))
                        print(79*'=')
                        while True:
                            p.most_powerful_weapon()
                            printa('\nB [Back]   P [Purchase Upgrade]',0.5,0.01)
                            ugis=input('\n[B/P]: ')# up-grade info screen
                            click()
                            if ugis in ['b','B','back','Back']:
                                print(79*'=')
                                print('\n\t\t\t[{} Description]'.format(p.inventory[int(bo)].name))
                                try:
                                    print('\n[Level]: ' + str(p.inventory[int(bo)].level))
                                except:
                                    pass
                                try:
                                    print('\n[Type]: ' + p.inventory[int(bo)].type)
                                except:
                                    pass
                                try:
                                    print('\n[Healing Value]: ' + str(p.inventory[int(bo)].hv))
                                except:
                                    pass
                                try:
                                    print('\n[Damage]: ' + str(p.inventory[int(bo)].dam))
                                except:
                                    pass
                                print('\n\n' + p.inventory[int(bo)].des)
                                print('\n' + (79*'='))
                                break # Goes back to Bag

                            elif ugis in ['p','P','purchase','Purchase']:
                                if p.money < int(p.inventory[int(bo)].dam//1.40):
                                    print(79*'=')
                                    printa('You don\'t have enough gold to purchase this upgrade!\n',0.5,0.01)
                                    print(79*'=')
                                    continue
                                p.money-=int(p.inventory[int(bo)].dam//1.40)
                                p.inventory[int(bo)].dam+=int(p.inventory[int(bo)].dam//5.75)
                                p.inventory[int(bo)].level+=1
                                printa('\n\nUpgraded [ {} ] to Level {}!\n'.format(p.inventory[int(bo)],p.inventory[int(bo)].level),0.5,0.02)
                                nsp=int(p.inventory[int(bo)].sp//2.75) # New Sell Price
                                p.inventory[int(bo)].sp+=nsp
                                if p.inventory[int(bo)].level==5:
                                    printa('Reached Max Level!\n',0.5,0.05)
                                    print(79*'=')
                                    print('\n\t\t\t[{} Description]'.format(p.inventory[int(bo)].name))
                                    try:
                                        print('\n[Level]: ' + str(p.inventory[int(bo)].level))
                                    except:
                                        pass
                                    try:
                                        print('\n[Type]: ' + p.inventory[int(bo)].type)
                                    except:
                                        pass
                                    try:
                                        print('\n[Healing Value]: ' + str(p.inventory[int(bo)].hv))
                                    except:
                                        pass
                                    try:
                                        print('\n[Damage]: ' + str(p.inventory[int(bo)].dam))
                                    except:
                                        pass
                                    print('\n\n' + p.inventory[int(bo)].des)
                                    print('\n' + (79*'='))
                                    break
                                print(79*'=')
                                print('\n\t\t\t[{}] Upgrade'.format(p.inventory[int(bo)].name))
                                print('\n[Level]: {}'.format(str(int(p.inventory[int(bo)].level))))
                                try:
                                    printa('\n[Damage]: {} + {}'
                                           .format(str(int(p.inventory[int(bo)].dam)),str(int(p.inventory[int(bo)].dam//5.75))),0.05,0.01)
                                    printa('\n\n{} G'.format(int(p.inventory[int(bo)].dam//1.40)),0.5,0.01)
                                except:
                                    pass
                                print('\n\t\t\t\t\t\t\t\t*[Gold: {}]'.format(p.money))
                                print(79*'=')
                                continue
                            else:
                                print(79*'=')
                                print('[ INVALID KEY ]')
                                print(79*'=')
                    #*****************************************#



                    else:
                        print(79*'=')
                        print('[ INVALID KEY ]')
                        print(79*'=')
                        continue
            except:
                break

        elif bo in ['b','B','back','Back']:
            break

        elif bo in ['h','H','heal','Heal']:
            if p.hp==p.maxhp:
                print(79*'=')
                printa('You\'re already at max HP!\n',0.5,0.01)
                continue
            p.heal()
        else:
            print('\n\n' + (79*'='))
            print('[ INVALID KEY ]')
            continue

#########################################
# EXPERIENCE BAR AND LEVELS FUNCTION(S) #
#########################################

level_hp={1:100, 2:105, 3:115, 4:130, 5:150}

def pxl():
    if p.level==1:
        level_1()
    elif p.level==2:
        level_2()
    elif p.level==3:
        level_3()
    elif p.level==4:
        level_4()
    else:
        #player at max level, 5
        pass

def level_1():
    while True:
        if 0 <= p.xp <= 4:
            p.xpbar='[                  ]'
            break
        elif 5 <= p.xp <= 8:
            p.xpbar='[#                 ]'
            break
        elif 9 <= p.xp <= 12:
            p.xpbar='[##                ]'
            break
        elif 13 <= p.xp <= 16:
            p.xpbar='[###               ]'
            break
        elif 17 <= p.xp <= 20:
            p.xpbar='[####              ]'
            break
        elif 21 <= p.xp <= 24:
            p.xpbar='[#####             ]'
            break
        elif 25 <= p.xp <= 28:
            p.xpbar='[######            ]'
            break
        elif 29 <= p.xp <= 32:
            p.xpbar='[#######           ]'
            break
        elif 33 <= p.xp <= 36:
            p.xpbar='[########          ]'
            break
        elif 37 <= p.xp <= 40:
            p.xpbar='[#########         ]'
            break
        elif 41 <= p.xp <= 44:
            p.xpbar='[##########        ]'
            break
        elif 45 <= p.xp <= 48:
            p.xpbar='[###########       ]'
            break
        elif 49 <= p.xp <= 52:
            p.xpbar='[############      ]'
            break
        elif 53 <= p.xp <= 56:
            p.xpbar='[#############     ]'
            break
        elif 57 <= p.xp <= 60:
            p.xpbar='[##############    ]'
            break
        elif 61 <= p.xp <= 64:
            p.xpbar='[###############   ]'
            break
        elif 65 <= p.xp <= 68:
            p.xpbar='[################  ]'
            break
        elif 69 <= p.xp <= 72:
            p.xpbar='[################# ]'
            break
        elif 73 <= p.xp <= 79:
            p.xpbar='[##################]'
            break
        elif p.xp >= 80:
            if p.xp > 80:
                p.xxp=p.xp-80
            p.xp=0
            p.xp+=p.xxp
            pxl()
            p.xxp=0
            p.xpbar='[                  ]'
            p.level+=1# Player goes to level 2
            printa('\n!You\'ve leveled up!\nHP increased by {}'.format(level_hp[p.level]-level_hp[p.level-1]),0.5,0.05)
            p.maxhp=level_hp[2]
            p.hp=p.maxhp
            printa('\nHP Restored!',0.5,0.05)
            break
        else:
            break

def level_2():
    while True:
        if 0 <= p.xp <= 4:
            p.xpbar='[                  ]'
            break
        elif 5 <= p.xp <= 8:
            p.xpbar='[#                 ]'
            break
        elif 9 <= p.xp <= 12:
            p.xpbar='[##                ]'
            break
        elif 13 <= p.xp <= 16:
            p.xpbar='[###               ]'
            break
        elif 17 <= p.xp <= 20:
            p.xpbar='[####              ]'
            break
        elif 21 <= p.xp <= 24:
            p.xpbar='[#####             ]'
            break
        elif 25 <= p.xp <= 28:
            p.xpbar='[######            ]'
            break
        elif 29 <= p.xp <= 32:
            p.xpbar='[#######           ]'
            break
        elif 33 <= p.xp <= 36:
            p.xpbar='[########          ]'
            break
        elif 37 <= p.xp <= 40:
            p.xpbar='[#########         ]'
            break
        elif 41 <= p.xp <= 44:
            p.xpbar='[##########        ]'
            break
        elif 45 <= p.xp <= 48:
            p.xpbar='[###########       ]'
            break
        elif 49 <= p.xp <= 52:
            p.xpbar='[############      ]'
            break
        elif 53 <= p.xp <= 56:
            p.xpbar='[#############     ]'
            break
        elif 57 <= p.xp <= 60:
            p.xpbar='[##############    ]'
            break
        elif 61 <= p.xp <= 64:
            p.xpbar='[###############   ]'
            break
        elif 65 <= p.xp <= 68:
            p.xpbar='[################  ]'
            break
        elif 69 <= p.xp <= 72:
            p.xpbar='[################# ]'
            break
        elif 73 <= p.xp <= 79:
            p.xpbar='[##################]'
            break
        elif p.xp >= 80:
            if p.xp > 80:
                p.xxp=p.xp-80
            p.xp=0
            p.xp+=p.xxp
            pxl()
            p.xxp=0
            p.xpbar='[                  ]'
            p.level+=1# Player goes to level 3
            printa('\n!You\'ve leveled up!\nHP increased by {}'.format(level_hp[p.level]-level_hp[p.level-1]),0.5,0.05)
            p.maxhp=level_hp[3]
            p.hp=p.maxhp
            printa('\nHP Restored!',0.5,0.05)
            break
        else:
            break

def level_3():
    while True:
        if 0 <= p.xp <= 4:
            p.xpbar='[                  ]'
            break
        elif 5 <= p.xp <= 8:
            p.xpbar='[#                 ]'
            break
        elif 9 <= p.xp <= 12:
            p.xpbar='[##                ]'
            break
        elif 13 <= p.xp <= 16:
            p.xpbar='[###               ]'
            break
        elif 17 <= p.xp <= 20:
            p.xpbar='[####              ]'
            break
        elif 21 <= p.xp <= 24:
            p.xpbar='[#####             ]'
            break
        elif 25 <= p.xp <= 28:
            p.xpbar='[######            ]'
            break
        elif 29 <= p.xp <= 32:
            p.xpbar='[#######           ]'
            break
        elif 33 <= p.xp <= 36:
            p.xpbar='[########          ]'
            break
        elif 37 <= p.xp <= 40:
            p.xpbar='[#########         ]'
            break
        elif 41 <= p.xp <= 44:
            p.xpbar='[##########        ]'
            break
        elif 45 <= p.xp <= 48:
            p.xpbar='[###########       ]'
            break
        elif 49 <= p.xp <= 52:
            p.xpbar='[############      ]'
            break
        elif 53 <= p.xp <= 56:
            p.xpbar='[#############     ]'
            break
        elif 57 <= p.xp <= 60:
            p.xpbar='[##############    ]'
            break
        elif 61 <= p.xp <= 64:
            p.xpbar='[###############   ]'
            break
        elif 65 <= p.xp <= 68:
            p.xpbar='[################  ]'
            break
        elif 69 <= p.xp <= 72:
            p.xpbar='[################# ]'
            break
        elif 73 <= p.xp <= 79:
            p.xpbar='[##################]'
            break
        elif p.xp >= 80:
            if p.xp > 80:
                p.xxp=p.xp-80
            p.xp=0
            p.xp+=p.xxp
            pxl()
            p.xxp=0
            p.xpbar='[                  ]'
            p.level+=1# Player goes to level 4
            printa('\n!You\'ve leveled up!\nHP increased by {}'.format(level_hp[p.level]-level_hp[p.level-1]),0.5,0.05)
            p.maxhp=level_hp[4]
            p.hp=p.maxhp
            printa('\nHP Restored!',0.5,0.05)
            break
        else:
            break

def level_4():
    while True:
        if 0 <= p.xp <= 4:
            p.xpbar='[                  ]'
            break
        elif 5 <= p.xp <= 8:
            p.xpbar='[#                 ]'
            break
        elif 9 <= p.xp <= 12:
            p.xpbar='[##                ]'
            break
        elif 13 <= p.xp <= 16:
            p.xpbar='[###               ]'
            break
        elif 17 <= p.xp <= 20:
            p.xpbar='[####              ]'
            break
        elif 21 <= p.xp <= 24:
            p.xpbar='[#####             ]'
            break
        elif 25 <= p.xp <= 28:
            p.xpbar='[######            ]'
            break
        elif 29 <= p.xp <= 32:
            p.xpbar='[#######           ]'
            break
        elif 33 <= p.xp <= 36:
            p.xpbar='[########          ]'
            break
        elif 37 <= p.xp <= 40:
            p.xpbar='[#########         ]'
            break
        elif 41 <= p.xp <= 44:
            p.xpbar='[##########        ]'
            break
        elif 45 <= p.xp <= 48:
            p.xpbar='[###########       ]'
            break
        elif 49 <= p.xp <= 52:
            p.xpbar='[############      ]'
            break
        elif 53 <= p.xp <= 56:
            p.xpbar='[#############     ]'
            break
        elif 57 <= p.xp <= 60:
            p.xpbar='[##############    ]'
            break
        elif 61 <= p.xp <= 64:
            p.xpbar='[###############   ]'
            break
        elif 65 <= p.xp <= 68:
            p.xpbar='[################  ]'
            break
        elif 69 <= p.xp <= 72:
            p.xpbar='[################# ]'
            break
        elif 73 <= p.xp <= 79:
            p.xpbar='[##################]'
            break
        elif p.xp >= 80:
            p.xpbar='[##################]'
            p.xp=80
            p.level+=1# Player goes to level 5
            printa('\n!You\'ve leveled up!\nHP increased by {}\n\nReached max level!'.format(level_hp[p.level]-level_hp[p.level-1]),0.5,0.05)
            p.maxhp=level_hp[5]
            p.hp=p.maxhp
            printa('\nHP Restored!',0.5,0.05)
            break
        else:
            break

#########################################################
# DEFINITIONS AND FUNCTION TO RANDOMLY GENERATE ENEMIES #
#########################################################
e1=Slime()
e2=GiantSpider()
e3=Ogre()
e4=BatColony()
e5=RockMonster()
e6=goblin()
#e7=
e8=BOSS_Ogre()

enegen={1:e1, 2:e2, 3:e2, 4:e2, 5:e3, 6:e3, 7:e4, 8:e5, 9:e6, 10:e8}
# NOTE TO SELF, START ADDING MORE ENEMIES AFTER " e6 ". MOVE " Boss Ogre " to higher number don't leave at 10 in dictionary #

def enemygenerator():
    while True:
        if p.ed < 20:# for Boss Ogre spawn chance
            n=7
        else:
            n=10
            break
        if p.ee >= 5:# For goblin and RockMonster spawn chance
            n=9
            break
        else:
            n=7
            break
    i=enegen[randint(1,n)]
    return i

############################################
# FUNCTION TO PRINT TEXT LIKE A VIDEO GAME #
############################################
def printa(str,a,b):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter in [',',':','HP','?','.','!','{}']:
            time.sleep(a)
        elif letter in ['\t']:
            time.sleep(0.001)
        else:
            time.sleep(b)

#####################################
# CLICK SOUND FROM POKEMON FUNCTION #
#####################################
def click():
        click=pygame.mixer.Sound('Sound Effects\\c.ogg')
        click.set_volume(.3)
        pygame.mixer.Sound.play(click)
        time.sleep(0.35)

###########################
# FUNCTION TO STACK ITEMS #
###########################
def stack():
    pass

####################################
def chields_tale():# GAME FUNCTION #
####################################

    pygame.mixer.music.load('Music\\mugen.ogg')
    pygame.mixer.music.play(-1)

    atcs=input('\nWould you like to clear the screen?\n\n[Y/Return]: ')# ask to clear screen
    click()
    if atcs in ['y','Y']:
        for i in range(53):
            print()
    else:
        pass

    ##################################
    while True:# GAME MAIN MENU LOOP #
    ##################################
            print(79*'=')

            ######################################################
            # PLAYER RELOAD PROPERTIES ###########################
            ######################################################
            p.hp=100
            p.maxhp=100
            p.hhv=0
            p.xp=0
            p.level=1
            p.xpbar='[                  ]'
            p.money=10
            p.ee=0
            p.ed=0
            p.inventory=[Rusty_Copper_Pistol(),Kabob(),Falafel()]
            #####################################################

            printa('\nS [Start]\tQ [Quit]\tH [Help]',0.5,0.01)
            tgmo=input('\n\n[S/Q/H]: ')# test game mode options
            click()
            ###############################################################
            if tgmo in ['q','Q','quit','Quit']:# QUIT OPTION IN MAIN MENU #
            ###############################################################
                pygame.mixer.music.fadeout(600)
                break
            #################################################################
            elif tgmo in ['h','H','help','Help']:# HELP OPTION IN MAIN MENU #
            #################################################################
                printa('\n\n\t\t\t   [IN DEVELOPMENT]' \
                       '\n\nThe several features included in this version are:' \
                       '\nCombat, LootDrops, Weapon Upgradability, Bag Functionality' \
                       '\nHealing, EXP and Levels(Max 5), Player Stats, Menus' \
                       '\nTrader(chance spawn starts after 10 enemy kills), etc...' \
                       '\n\n\t\t\tversion 5.0 alpha\n\n\t\t\t\t\t-Abbacus Inc.',0.5,0.01)
                input('\n[Return]: ')
                click()
                continue
            ####################################################################
            elif tgmo in ['s','S','start','Start']:# START OPTION IN MAIN MENU #
            ####################################################################
                pygame.mixer.music.fadeout(600)
                pass
            #################################
            else:# INVALID KEY IN MAIN MENU #
            #################################
                print(79*'=')
                print('[ INVALID KEY ]')
                continue

            p.name=input('Username: ')
            click()
            printa('\nHello {}, here\'s what you should know:\n\nA [Attack]\tN [do Nothing]\t\tB [Bag]\t\tF [Flee]\nE [Exit Game]'
                    .format(p.name),0.7,0.01)
            input('\n\nGot it!\n[Return]: ')
            click()
            printa('\nStarting..',0.5,0.01)

            pygame.mixer.music.load('Music\\testmusic.ogg')
            pygame.mixer.music.play(-1)
            time.sleep(1)

            ###########################################################
            ################## STUFF TO LOAD BEFORE GAME LOOP #########
            ###########################################################
            e=enemygenerator()
            esh={e1:100, e2:35, e3:57, e4:100, e5:115, e6:300, e8:200}# enemy starting health(will access this inside the game loop to reset enemy health)
            e1.hp=100
            e2.hp=35
            e3.hp=57
            e4.hp=100
            e5.hp=115
            e6.hp=300
            #e7.hp
            e8.hp=200

            print('\n' + (79*'='))
            printa(e.ades + '\n',0.5,0.01)
            p.ee+=1

            ###################################
            while True:#GAME LOOP STARTS HERE #
            ###################################
                print(79*'=')
                ###############################################################################
                # STUFF TO ALWAYS LOAD AT TOP OF GAME LOOP ####################################
                ###############################################################################
                p.bw=p.most_powerful_weapon()# ASSIGNS most_powerful_weapon() TO best weapon ##
                g=p.bw# ASSIGNS g TO BEST WEAPON ##############################################
                g.dam=p.bw.dam# ASSIGNS best weapon damage TO best weapon damage IF IT CHANGED#
                ###############################################################################
                print('\t\t\t\t\t\t[{} {}/{}HP]'.format(e.name,e.hp,esh[e]))
                if len(str(p.xp))==2:# fixes space issues with exp numbers
                    print('\nLvl.{} [{} {}/{}HP]'.format(p.level,p.name,p.hp,p.maxhp))
                    print('EXP [{}/80]{}'.format(p.xp,p.xpbar))
                else:
                    print('\nLvl.{} [{} {}/{}HP]'.format(p.level,p.name,p.hp,p.maxhp))
                    print('EXP [ {}/80]{}'.format(p.xp,p.xpbar))
                pa=input('\n\n[A/N/B/F/E]: ')# player action
                click()
################################################################
                if pa in ['n','N']:# DO NOTHING OPTION IN GAME # # FOR MYSTERY PART IN GAME #
################################################################
                    p.hp-=e.dam
                    printa('\n{} has decided to do nothing?'.format(p.name),0.6,0.01)
                    if p.hp <= 0:
                        printa('\nYou\'ve taken {} damage and are left with {} HP...'\
                          '\nYou collapse on the floor fainted.'.format(e.dam,p.hp),0.5,0.01)
                        input('[Quit]: ')
                        click()
                        break
                    else:
                        printa('\nYou\'ve taken {} damage from a {}, and are left '\
                          'with {} HP remaining\n'.format(e.dam,e.name,p.hp),0.5,0.01)
                        continue
################################################################################
                elif pa in ['a','A','attack','Attack']:# ATTACK OPTION IN GAME #
################################################################################
                    echa=randint(3,10)# Enemy Critical Hit Attack # This links to enemy attack below #
                    # check if player will die if attacking and check if they have items to heal #
                    if e.hp-g.dam <=0:
                        pass
                    else:
                        if p.hp-e.hdam <= 0 or p.hp-(e.dam+echa) <= 0 or p.hp-(e.hdam-echa) <= 0:
                            ciphhi=[item for item in p.inventory if isinstance(item,Consumable)]
                            for i in ciphhi:
                                p.hhv+=i.hv
                            if p.hp-e.hdam <= 0 and len(ciphhi) >= 1 and p.hhv >= e.hdam:# ask if user is paying attention to their health #
                                    printa('\nAre you sure you want to attack?\nYou have {}HP available in your bag.' \
                                            '\nUse your items to heal so you might not die!'.format(p.hhv),0.5,0.01)
                                    while True:
                                        printa('\n\nH [Heal]   A [Attack Anyways]',0.5,0.01)
                                        aiuipa=input('\n[H/A]: ')
                                        click()
                                        if aiuipa in ['h','H','heal','Heal']:
                                            p.heal()
                                            p.hhv=0
                                            print(79*'=')
                                            break
                                        elif aiuipa in ['a','A','attack','Attack']:
                                            p.hhv=0
                                            break
                                        else:
                                            print(79*'=')
                                            print('[ INVALID KEY ]')
                                            print(79*'=')
                                            continue
                    p.hhv=0
                    printa('\n\n{} used {}.'.format(p.name,p.bw),0.5,0.01)
                    e.hp-=g.dam

                    ################################
                    # CRITICAL HIT AND OTHER STUFF #
                    ################################

                    sfeo=randint(1,5)# Finish Enemy Off Chance #
                    if 1 <= e.hp <= g.dam and sfeo in [1,2]:
                        e.hp-=g.dam
                        if g.type=='Sword':
                            printa('\nYou swiftly lunge back toward the enemy and finish the job...',0.5,0.01)
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,2*g.dam,e.hp),0.5,0.01)
                        elif g.type=='Gun':
                            printa('\nYou quickly reload again and finish the job...',0.5,0.01)
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,2*g.dam,e.hp),0.5,0.01)
                        elif g.type=='Natural':
                            printa('\nYou swiftly lunge back toward and uppercut the enemy...',0.5,0.01)
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,2*g.dam,e.hp),0.5,0.01)
                    elif 1 <= e.hp <= g.dam and sfeo==4:
                        if g.type=='Sword':
                            printa('\nYou swiftly lunge back toward the enemy..you trip and\nfail miserably..-1 dignity.',0.5,0.01)
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,g.dam,e.hp),0.5,0.01)
                        elif g.type=='Gun':
                            printa('\nYou quickly shoot again..*click*..but forgot to reload.',0.5,0.01)
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,g.dam,e.hp),0.5,0.01)
                        elif g.type=='Natural':
                            printa('\nYou can\'t bring yourself to finish the enemy off\n*rubbing fists*',0.5,0.01)
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,g.dam,e.hp),0.5,0.01)
                    else:
                        ch=randint(0,randint(4,5))# Critical Hit Chance
                        if ch==2:
                            cha=randint(3,10)# Critical Hit Attack
                            printa('\n\n!Critical Hit! {} does an extra {} damage!'.format(p.bw,cha),0.5,0.01)
                            e.hp-=cha
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,g.dam+cha,e.hp),0.5,0.01)
                        else:
                            printa('\n\n{} has taken a direct hit of {} damage!'
                                   .format(e.name,g.dam,e.hp),0.5,0.01)
                    #######################################
                    if e.hp <= 0:# IF ENEMY IS DEAD STUFF #
                    #######################################
                        printa('\n\nAH-HA! the {} has been obliterated..\nYou dance around in triumph.'
                               .format(e.name),0.5,0.01)
                        #*********************#
                        # EXP AND LEVEL STUFF #
                        #*********************#
                        if p.level==5:# Level cap at 5
                            pass
                        ################
                        else:# XP GAIN #
                        ################
                            printa('\n\n{} has gained {} exp!'.format(p.name,e.xpd),0.5,0.01)
                            p.xp+=e.xpd
                            #******************************************#
                            pxl()# EXP BAR AND LEVEL HANDLING FUNCTION #
                            #******************************************#

                        ##############################################
                        rei=randint(0,10)# RANDOMIZE ENEMY INVENTORY #
                        ##############################################
                        if rei in [0,1]:
                            e.inventory=[Falafel(),Falafel()]
                        elif rei in [2,3]:
                            e.inventory=[Falafel(),Kabob(),LeftOvers()]
                        elif rei in [4,5,6]:
                            e.inventory=[LeftOvers(),LeftOvers()]
                        elif rei in [7,8,9]:
                            e.inventory=[Falafel(),Falafel(),LeftOvers()]
                        elif rei in [10]:
                            e.inventory=[Kabob(),Kabob(),Kabob()]
                        if e==e5:# RockMonster inventory
                            e.inventory=[Kabob(),Falafel(),Falafel()]
                        elif e==e6:# goblin inventory
                            e.inventory=[BRS(),Kabob(),Kabob(),Kabob(),LeftOvers()]
                        elif e==e8:# Boss Ogre inventory
                            e.inventory=[Revolver(),Kabob(),Kabob(),Falafel(),LeftOvers(),LeftOvers()]
                        #######################################
                        ld=randint(0,randint(2,3))# LOOT DROP #
                        #######################################
                        if e == e8:# Special Conditions for Boss Ogre
                            ld=0
                            e.trip+=1
                            if e.trip == 1:
                                del e.inventory[0]
                                e.inventory.append(Kabob())
                        elif e == e6:# Special Conditions for goblin
                            ld=0
                            e.trip+=1
                            if e.trip == 0:
                                pass
                            elif e.trip == 1:
                                e.inventory=[Kabob(),Kabob(),LeftOvers()]
                                e.money=15
                            elif e.trip == 2:
                                e.inventory=[Kabob(),LeftOvers()]
                                e.money=10
                            elif e.trip == 3:
                                e.inventory=[Kabob(),Kabob(),Kabob(),LeftOvers()]
                                e.money=20
                            else:
                                e.inventory=[Falafel(),LeftOvers()]
                                e.money=5
                        elif e == e5:
                            ld=randint(0,1)
                        if p.inventory==[] or len(p.inventory)==2:
                            ld=randint(0,1)
                        if ld==0:
                            printa('\n\n!{} has droped some loot!\nYou eagerly collect it.'.format(e.name),0.5,0.01)
                            printa('\n\n\t\t\t[ {} LOOT ]'.format(e.name),0.5,0.01)
                            print('\n')
                            for i in e.inventory:
                                print(i)
                            print(str(e.money) + ' G')

                            ccifl=input('\n\nReturn [Collect All]   L [Open Loot Bag]\n[Return/L]: ')# collect certain items from loot
                            click()
                            if ccifl in ['l','L']:
                                print(79*'=')
                                #*********************************************************************#
                                printa('\n\t\t\t\t[LOOT BAG]',0.5,0.01)# TAKE CERTAIN ITEMS FROM LOOT #
                                #*********************************************************************#
                                k=-1
                                for i in e.inventory:
                                    k+=1
                                    print('\n' + '[' + str(k) + ']' + str(i))
                                print(79*'=')
                                while True:
                                    lbi=input('\n[E/0-{}]: '.format(len(e.inventory)-1))# loot bag input
                                    lbi_int_list=[]
                                    for n in range(0,int(len(e.inventory))):
                                        lbi_int_list.append(str(n))
                                    if lbi in lbi_int_list:
                                        print(79*'=')
                                        printa('Looted {}\n'.format(e.inventory[int(lbi)]),0.5,0.03)
                                        p.inventory.append(e.inventory[int(lbi)])
                                        del e.inventory[int(lbi)]
                                        if len(e.inventory)==0:
                                            print(79*'=')
                                            break
                                        print(79*'=')
                                        print('\n\t\t\t\t[LOOT BAG]')
                                        k=-1
                                        for i in e.inventory:
                                            k+=1
                                            print('\n' + '[' + str(k) + ']' + str(i))
                                        print(79*'=')
                                        continue
                                    elif lbi in ['e','E','exit','Exit']:
                                        break
                                    else:
                                        print(79*'=')
                                        print('[ INVALID KEY ]')
                                        print(79*'=')
                                        print('\n\t\t\t\t[LOOT BAG]')
                                        k=-1
                                        for i in e.inventory:
                                            k+=1
                                            print('\n' + '[' + str(k) + ']' + str(i))
                                        print(79*'=')
                                        continue
                            else:
                                i=0
                                while True:
                                    try:
                                        p.inventory.append(e.inventory[i])
                                        i+=1
                                    except:
                                        break
                            p.money+=e.money

                            ######################################

                        '''
                        sipnr=[item for item in p.inventory if isinstance(item,Consumable)]# see if player needs rest
                        ###################################################
                        if len(sipnr==0 and p.hp >= 10):# LET PLAYER REST #
                        ###################################################
                            printa('\nWould you like to stop and rest?',0.5,0.01)
                            atr=input('\n[Return/N]:')# ask to rest
                            if atr in ['n','N','no','No']:
                                pass
                            else:
                                ########################################
                                spawnTJ()# CHANCE TO SPAWN TRADER JACK #
                                ########################################
                                printa('\n\n{} rests for a while...'.format(p.name),0.5,0.01)
                                p.hp=p.maxhp
                                printa('\nYou\'ve regained your health!',0.5,0.01)
                        else:
                            ########################################
                            spawnTJ()# CHANCE TO SPAWN TRADER JACK #
                            ########################################
                        '''
                        ########################################
                        spawnTJ()# CHANCE TO SPAWN TRADER JACK #
                        ########################################

                        atc=input('\n\nContinue?\n[Return/N]: ')# ask to continue
                        click()

                        if atc in ['n','N','no','No']:
                            break
                        else:
                            e.hp=esh[e]
                            enemygenerator()
                            e=enemygenerator()
                            print('\n' + (79*'='))
                            printa(e.ades + '\n',0.5,0.01)
                            p.ed+=1# enemy defeated + 1
                            p.ee+=1 # enemy encounter + 1
                            continue
                    ###########################################
                    else:# ENEMY ATTACKS BACK AFTER ATTACKING #
                    ###########################################
                        ######################################################################
                        hoba=randint(randint(1,2),randint(7,8))# Enemy Heavy or Basic Attack #
                        ######################################################################
                        if hoba==5:
                            printa('\n\n!{} uses a heavy attack causing you to lose {} HP!\n'
                                   .format(e.name,e.hdam),0.6,0.01)
                            p.hp-=e.hdam
                        else:
                            printa('\n\n{} uses a basic attack causing you to lose {} HP.\n'
                                   .format(e.name,e.dam),0.5,0.01)
                            p.hp-=e.dam
                        ########################################################
                        ech=randint(0,randint(4,5))# Enemy Critical Hit Chance #
                        ########################################################
                        if p.hp - e.dam <= 0:# Don't display critical hit if enemy damage will already kill player
                            pass
                        else:
                            if ech == 0:
                                printa('\n!Critical Hit! {} does an extra {} damage!\n'.format(e.name,echa),0.5,0.01)
                                p.hp-=echa
                        if p.hp <= 0:
                            pygame.mixer.music.fadeout(600)
                            time.sleep(0.2)
                            printa('\nAfter the attack are left with {} HP...'\
                              '\nYou collapse on the floor fainted.'.format(p.hp),0.5,0.01)
                            input('\n[Quit]: ')
                            click()
                            pygame.mixer.music.load('Music\\mugen.ogg')
                            pygame.mixer.music.play(-1)
                            break
                        continue

#######################################################################
                elif pa in ['b','B','bag','Bag']:# BAG OPTION IN GAME #
#######################################################################
                    pygame.mixer.music.set_volume(0.2960937)
                    time.sleep(0.35)
                    Bag()
                    pygame.mixer.music.set_volume(0.9921875)
##########################################################################
                elif pa in ['f','F','flee','Flee']:# FLEE OPTION IN GAME #
##########################################################################
                    ########################################
                    # PLAYER ITEM/GOLD DROP CHANCE IF FLED #
                    ########################################
                    printa('{} has Fled!'.format(p.name),0.5,0.01)
                    drop=randint(0,randint(3,4))
                    try:# IF PLAYER HAS NOTHING IN INVENTORY, DROP GOLD #
                        itemn=randint(randint(0,1),int(len(p.inventory))-1)# item number
                    except:
                        if p.inventory==[]:
                            drop=2
                    if drop==1:# ITEM DROP
                        printa('\n\n!by fleeing, {} dropped [ {} ].\n\n..{} has picked it up!'.format(p.name,p.inventory[itemn],e.name),0.5,0.01)
                        e.inventory.append(itemn)
                        del p.inventory[itemn]
                        p.most_powerful_weapon()
                    elif drop==2:
                        gp=randint(randint(0,p.money//5))#GOLD DROP
                        if p.money==0:
                            pass
                        else:
                            printa('\n\n!by fleeing, {} dropped [ {} ].\n\n..{} has picked it up!' \
                                   .format(p.name,str(gp) + ' G',e.name),0.5,0.01)
                            p.money-=gp
                            e.money+=gp

                    ########################################
                    spawnTJ()# CHANCE TO SPAWN TRADER JACK #
                    ########################################

                    atc=input('\n\nContinue?\n[Return/N]: ')# ask to continue
                    click()

                    if atc in ['n','N','no','No']:
                        break
                    else:
                        e.hp=esh[e]
                        enemygenerator()
                        e=enemygenerator()
                        print('\n' + (79*'='))
                        printa(e.ades + '\n',0.5,0.01)
                        p.ee+=1 # enemy encounter + 1
                        continue
#######################################################################
                elif pa in ['e','E','exit','Exit']:# EXIT KEY IN GAME #
#######################################################################
                    print('Exiting...')
                    pygame.mixer.music.fadeout(600)
                    time.sleep(0.2)
                    pygame.mixer.music.load('Music\\mugen.ogg')
                    pygame.mixer.music.play(-1)
                    break
############################################
                else:# INVALID KEY IN GAME #
############################################
                    print(79*'=')
                    print('[ INVALID KEY ]')
                    continue
            #######################
            # BOTTOM OF GAME LOOP #
            #######################

# Can test functions here, remove the " # " below then " F5 ". Put back when done.
#heal()
#spawnTJ()
#Bag()
#chields_tale()
