############## FUTURE UPDATE ##########
# add currency so that bum can take a certain amount
# add a function to choose from store

from inventory import *
from initGame import *
from randFunc import *
import random

def meeting(invList):
    personMet = randPer(perList)

    print('\nYou have met ' + personMet + '\n')

    trust = input('Do you trust them?\nY or N\n')

    if trust == 'Y' or trust == 'y':
        typePer = randTrust(trustList)
        print('You have met a: ' + typePer)

        merchStore = []

        if typePer == 'Thief':
            stolen = randInventory(invList)
            if stolen in invList:
                invList.remove(stolen)
                return trust
            else:
                return trust
        elif typePer == 'Merchant':
            for i in range(5):
                storeItm = randItm(fndList)
                merchStore.append(storeItm)
            merchStore.append('None')
            print('You have met a Merchant ' + personMet + ' here is what you can get: ' + merchStore + '.\n')
            #add function to choose from storeItm
            return trust
        elif typePer == 'Bum':
            #he automatically takes money
            return trust
        elif typePer == 'Villager':
            print('Bruh what you doin here go get them.')
            return trust
    else:
        return trust

    return uI
