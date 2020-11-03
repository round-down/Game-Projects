#Aurthor: Abbas Al-Akashi & Caleb M Hurley

#you are in the inventory you choose if you want to use or drop or see stats
#if there is nothing kick you out
#ask if you want to leave

################### FUTURE UPDATE #################
# add Stats for an ITEM
# add a none option
# add functionality to USE
# add a 'are you sure you want to drop'
# add a limit
###################################################


def invFunc(inventory, been):
    #inventory is already empty go back to game
    if not inventory:
        print("Inventory is empty going back.")
        return been

    #inventory is not empty what item to select
    uI = input("\nWhat do you want to select: " + str(inventory))
    if uI in inventory:

        #send the user to choose what to do with the item
        invDo(uI, inventory)

        #once user comes back ask them if they want to leave
        #if user drops their only item kick them out
        if not inventory:
            print('Well your inventory is empty you gotta go.')
            return been

        extChoice = ['Y', 'N']
        exitI = input('Do you want to leave inventory? ' + str(extChoice) + '\n')
        if exitI in extChoice:
            if exitI == 'Y':
                return been
            if exitI == 'N':
                invFunc(inventory, been)
    elif uI == 'S' or uI == 's':
        return been
    else:
        wrong = True
        while wrong:
            if uI in inventory:
                invDo(uI)
                wrong = False
            elif uI == 's' or uI == 'S':
                return been
            else:
                print("Wrong input choose from the list:\n" + str(inventory) +'\n')
                uI = input()
    if uI =='s' or uI == 'S':
        return been


def invDo(itmSelect, inventoryList):
    itmPur = ['Use', 'Drop']
    uI = input("\nWhat do you want to do with " + itmSelect + ": " + str(itmPur) + '\n')
    if uI in itmPur:
        ############# have to change for different items ################
        if uI == 'Use':
            return
        if uI == 'Drop':
            inventoryList.remove(itmSelect)
            print('You have dropped: ' + itmSelect + '\n')
            return
        #################################################################
    elif uI == 'S' or uI == 's':
        return
    else:
        wrong = True
        while wrong:
            if uI in itmPur:
            ############# have to change for different items ################
                if uI == 'Use':
                    return
                if uI == 'Drop':
                    inventoryList.remove(itmSelect)
                    print('You have dropped: ' + itmSelect + '\n')
                    return
                wrong = False
            #################################################################
            elif uI == 's' or uI == 'S':
                break
            else:
                print("Wrong input choose from the list:\n" + str(itmPur) +'\n')
                uI = input()
    if uI =='s' or uI == 'S':
        return
