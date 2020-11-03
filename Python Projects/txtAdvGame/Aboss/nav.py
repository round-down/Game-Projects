#navigation/story
#fighting
#inventory
#capture/characters/pokemon

######## FUTURE UPDATES ########
# when you take a path and you loop show same path#
################################

#######################################-------------NAVIGATION/STORY-----------##########################################
#move up/left/right/down
#meet characters
#find items
#get path blocked
#store

import random
import queue

#global directions
upArr = 'w'
downArr = 's'
leftArr = 'a'
rightArr = 'd'
chosenPrevious = False
previousDir = queue.LifoQueue()
userChosenList = []

#randomize what directions can get chosen
def randDir(dirList):
    random_dir = random.choice(dirList)
    return random_dir

#randomize how many directions to choose
def randNum(numDir):
    random_Num = random.choice(numDir)
    return random_Num

#check if input is correct
def checkInput(inputVal, directionChosen):
    if inputVal in directionChosen:

        if not userChosenList:
            prevChosen = False
            oppositeVal = downArr
            userChosenList.append(inputVal)
            naviStory(oppositeVal, prevChosen)
        else:
            try:
                if (inputVal != downArr):
                    if inputVal == leftArr:
                        try:
                            if (userChosenList[len(userChosenList) - 2] != leftArr) and (userChosenList[len(userChosenList) - 1] != leftArr):
                                prevChosen = False
                                oppositeVal = downArr
                                userChosenList.append(inputVal)
                                naviStory(oppositeVal, prevChosen)
                            elif (userChosenList[len(userChosenList) - 2] == leftArr) and (userChosenList[len(userChosenList) - 1] == leftArr):
                                print("It seems like you've been here before, but something changed\n")
                                if previousDir.empty() != False:
                                    previousDir.get()
                                    prevChosen = True
                                    oppositeVal = downArr
                                    userChosenList.append(inputVal)
                                    naviStory(oppositeVal, prevChosen)
                                else:
                                    prevChosen = False
                                    oppositeVal = downArr
                                    userChosenList.append(inputVal)
                                    naviStory(oppositeVal, prevChosen)
                            else:
                                prevChosen = False
                                oppositeVal = downArr
                                userChosenList.append(inputVal)
                                naviStory(oppositeVal, prevChosen)
                        except:
                            prevChosen = False
                            oppositeVal = downArr
                            userChosenList.append(inputVal)
                            naviStory(oppositeVal, prevChosen)
                    elif inputVal == rightArr:
                        try:
                            if (userChosenList[len(userChosenList) - 2] != rightArr) and (userChosenList[len(userChosenList) - 1] != rightArr):
                                prevChosen = False
                                oppositeVal = downArr
                                userChosenList.append(inputVal)
                                naviStory(oppositeVal, prevChosen)
                            elif (userChosenList[len(userChosenList) - 2] == rightArr) and (userChosenList[len(userChosenList) - 1] == rightArr):
                                print("It seems like you've been here before, but something changed\n")
                                if previousDir.empty() != False:
                                    previousDir.get()
                                    prevChosen = True
                                    oppositeVal = downArr
                                    userChosenList.append(inputVal)
                                    naviStory(oppositeVal, prevChosen)
                                else:
                                    prevChosen = False
                                    oppositeVal = downArr
                                    userChosenList.append(inputVal)
                                    naviStory(oppositeVal, prevChosen)
                            else:
                                prevChosen = False
                                oppositeVal = downArr
                                userChosenList.append(inputVal)
                                naviStory(oppositeVal, prevChosen)
                        except:
                            prevChosen = False
                            oppositeVal = downArr
                            userChosenList.append(inputVal)
                            naviStory(oppositeVal, prevChosen)
                    else:
                        prevChosen = False
                        oppositeVal = downArr
                        userChosenList.append(inputVal)
                        naviStory(oppositeVal, prevChosen)


                #print('we are trying. This is the userChosenList: ', userChosenList)
                #list has values so continue
                else:
                    if (inputVal == downArr) and (len(userChosenList) >= 1):
                        #print('stuck')
                        prevChosen = True
                        oppositeVal = downArr
                        userChosenList.append(inputVal)
                        naviStory(oppositeVal, prevChosen)
            except IndexError:
                print("THIS AINT IT CHIEF\n\n")

    else:
        print("Stop messing around that way is blocked.\n")
        getDirIn(directionChosen)

def getDirIn(dirChoose):
    print("Choices are: ", dirChoose)
    userInput = input("Choose that DIRECTION BOIIII: ")
    checkInput(userInput, dirChoose)

def naviStory(lastVal, chosenPrevious):
    if chosenPrevious == False:
        #initialize direciton
        direction = [upArr, leftArr, rightArr]

        numDirect = [1, 2, 3]
        chosenDir = []

        #append back value
        if (lastVal != ''):
            chosenDir.append(lastVal)

        #choose num of direcitons between 1-4 do for loop that randomizes which direcitons are chosen
        number = randNum(numDirect)
        for i in range(number):
            existVal = False
            valAppend = randDir(direction)
            #make sure that only one exists
            if not chosenDir:
                chosenDir.append(valAppend)
            else:
                for k in chosenDir:
                    if (k == valAppend):
                        existVal = True
                if (existVal == False):
                    #choose direcitons
                    chosenDir.append(valAppend)

        #if chosenDir not in previousDir:
        previousDir.put(chosenDir)

        print('\n\n-----------------------------------------------------------------------------\n\n')
        getDirIn(chosenDir)

    elif chosenPrevious == True:
        if previousDir.qsize() > 1:
            previousDir.get()
            print('\n\n-----------------------------------------------------------------------------\n\n')
            print('\n\n You went back but something changed\n')
            getDirIn(previousDir.get())
        else:
            print('\n\n-----------------------------------------------------------------------------\n\n')
            print('\n\n You went back but something changed\n')
            getDirIn(previousDir.get())


print('##################################################\n\n')
print('There has been an invasion from the east...\n')
print('Mother Nature is furious and has been wrecking havock in the lands.\n')
print('Supplies are low and the village turns to their chief.\n')
print('Chief has ordered every family to send a child into the world to find supplies.\n')
print('Your mother bids you farewell as you embark on your journey.\n')
print('But becareful somethings do not appear what the seem\n')
lV = ''
naviStory(lV, False)
