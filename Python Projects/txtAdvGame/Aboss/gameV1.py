#Aurthor: Abbas Al-Akashi & Caleb M Hurley

################# future update #############
#   fix where if you press I it skips your  #
#       initial choices                     #
# go back to preovious choices when in inventory #
#############################################

import random
from inventory import *
from randFunc import *
from initGame import *
from pathChoosing import *
from foundItem import *

def main():
    ################    STORY   #################
    print('\n\n################## INSTRUCTIONS ##################\n\n')
    print('To stop the game press "S" or "s" at any input point.')
    print('To access inventory press "I" or "i" at any input point.\n\n')
    print('##################################################\n\n')
    print('There has been an invasion from the east...\n')
    print('Mother Nature is furious and has been wrecking havock in the lands.\n')
    print('Supplies are low and the village turns to their chief.\n')
    print('Chief has ordered every family to send a child into the world to find supplies.\n')
    print('Your mother bids you farewell as you embark on your journey.\n')

    been = False
    stop = False


    while(stop != True):
        choice = randNar(narList)
        if(choice == dilPath):
            uI = pathFunc()
            if uI == 'i' or uI == 'I':
                if been == False:
                    print('\n\nYou are in your INVENTORY! \nYou have: ' + str(invList))
                    been = True
                    invFunc(invList, been)
                else:
                    been = False
            elif uI =='s' or uI == 'S':
                break
            else:
                continue

        elif(choice == encPath):
            uI = pathFunc()
            if uI == 'i' or uI == 'I':
                if been == False:
                    print('\n\nYou are in your INVENTORY! \nYou have: ' + str(invList))
                    been = True
                    invFunc(invList, been)
                else:
                    been = False
            elif uI =='s' or uI == 'S':
                break
            else:
                continue

        elif(choice == foundPath):
            uI = fndItm()
            if uI == 'i' or uI == 'I':
                if been == False:
                    print('\n\nYou are in your INVENTORY! \nYou have: ' + str(invList))
                    been = True
                    invFunc(invList, been)
                else:
                    been = False
            elif uI =='s' or uI == 'S':
                break
            else:
                continue

        elif(choice == metPath):
            uI = meeting(invList)
            if uI == 'i' or uI == 'I':
                if been == False:
                    print('\n\nYou are in your INVENTORY! \nYou have: ' + str(invList))
                    been = True
                    invFunc(invList, been)
                else:
                    been = False
            elif uI =='s' or uI == 'S':
                break
            else:
                continue

    print('Thank you for playing. Come back again.')

main()

#make a list
#every time something is done you append it to the list could be a list of dir or biome
#if you want to go back call the most recent value in the list
