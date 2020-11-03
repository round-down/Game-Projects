#Aurthor: Abbas Al-Akashi & Caleb M Hurley

import random
from inventory import *
from randFunc import *

###################     INITIALIZE     ####################

#add south later because need to keep list of what happened previously
#maybe use an array to keep track
dirList = ['North', 'East', 'West']
numDir = [1, 2, 3]

#narration:
#see if you encountered and enemy, see if you have found an item, you meet someone

dilPath = 'You have come across a path, you can go: '

#monsters
monList = ['Orc', 'Ogre', 'Tree Monster', 'Goblin', 'Spider', 'Undead', 'Thief']

#biomes
biomeList = ['Mountains', 'Plains', 'Desert', 'Beach']

#make it to where in different biomes some monsters are added or changed
biLand = randBiome(biomeList)
if biLand == 'Mountains':
    monList.append('DRAGON')
    monList.append('Griffin')
    monList.append('Golem')
    monster = randMon(monList)
    encPath = 'You have encountered: ' + monster
    monList = ['Orc', 'Ogre', 'Tree Monster', 'Goblin', 'Spider', 'Undead', 'Thief']
elif biLand == 'Beach':
    monList = ['Mermaid', 'Serpent', 'Crab', 'Siren', 'Undead', 'Thief']
    monster = randMon(monList)
    encPath = 'You have encountered: ' + monster
    monList = ['Orc', 'Ogre', 'Tree Monster', 'Goblin', 'Spider', 'Undead', 'Thief']
elif biLand == 'Plain':
    monList.append('Golem')
    monList.remove('Tree Monster')
    monster = randMon(monList)
    encPath = 'You have encountered: ' + monster
    monList = ['Orc', 'Ogre', 'Tree Monster', 'Goblin', 'Spider', 'Undead', 'Thief']
elif biLand == 'Desert':
    monList.append('Snake')
    monList.append('Scorpion')
    monList.remove('Tree Monster')
    monster = randMon(monList)
    encPath = 'You have encountered: ' + monster
    monList = ['Orc', 'Ogre', 'Tree Monster', 'Goblin', 'Spider', 'Undead', 'Thief']


fndList = ['Poison', 'Kabob', 'BOMB', 'Sword', 'Armor', 'Shoe', 'grass']
fndItm = randItm(fndList)
foundPath = 'You found: '

perList = ['Kalieb', 'Gabby', 'Jak', 'Steve', 'Linda']
metPer = randPer(perList)
metPath = 'You met: ' + metPer

narList = [dilPath] * 83 + [encPath] * 15 + [foundPath] * 1 + [metPath] * 1

#items
itmList = ['Kabob', 'Sword', 'Armor', 'BOMB']
itmDrop = 'The monster has dropped... ' + monDrop(itmList)

trustList = ['Merchant'] * 1 + ['Theif'] * 10 + ['Bum'] * 5 + ['Villager'] * 84 

vilDia = ['Monsters have been invading us. Please Help.', 'Thank you for stopping by have a great day', 'You look nice today.', 'Get outa my face!']

choiceList = []

history = []

invList = []




