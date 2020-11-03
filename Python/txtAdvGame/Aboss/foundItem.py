from inventory import *
from initGame import *
from randFunc import *
import random

def fndItm():
    choiceList = []
    foundItm = randItm(fndList)
    print('\nYou have found: ' + foundItm + '.') 
    choiceList.append('Take')
    choiceList.append('Leave')
    uI = input('What do you want to do: ' + str(choiceList) + '\n')

    if (uI in choiceList) or (uI == 'i') or (uI == 'I') or (uI == 's') or (uI == 'S'):
        if uI == 'Take':
            invList.append(foundItm)
            return
        elif uI == 'Leave':
            return
        else:
            return uI
    else:
        wrong = True
        while wrong:
            if (uI in choiceList) or (uI == 'i') or (uI == 'I') or (uI == 's') or (uI == 'S'):
                wrong = False
                if uI == 'Take':
                    invList.append(foundItm)
                    return
                elif uI == 'Leave':
                    return
                else:
                    return uI
            else:
                print("Boi choose from the list: \n" + str(choiceList) +'\n')
                uI = input()
