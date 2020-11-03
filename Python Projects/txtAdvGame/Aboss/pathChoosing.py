from inventory import *
from initGame import *
from randFunc import *
import random 

############ Future Updates ############
# add biomes


def pathFunc():
    #initialize
    choiceList = []     #to hold choices
    been = False        #bool to see if you've been to inventory
    amtDir = randNum(numDir)    #picks how many directions to show player
    
    #depending how many directions are allowed
    #pick which directions
    for i in range(amtDir):
        dirChoice = randDir(dirList)
        choiceList.append(dirChoice)
        #make sure choices don't repeat
        choiceList = list(set(choiceList))
    
    #have user choose where to go
    uI = input("\n\nChoose the direction you wish to take: " + str(choiceList) + '\nI want to go: ')

    #see if user has input that is in the allowed directions
    if (uI in choiceList) or (uI == 'i') or (uI == 'I') or (uI == 's') or (uI == 'S'):
        return uI
    #if user entered wrong choice
    else:
        wrong = True
        while wrong:
            if (uI in choiceList) or (uI == 'i') or (uI == 'I') or (uI == 's') or (uI == 'S'):
                wrong = False
                return uI
            elif uI == 's' or uI == 'S':
                return uI
            else:
                print("\n\nThat path is blocked choose from the correct path: " + str(choiceList))
                uI = input('I want to go: ')
