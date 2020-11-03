import random


def getNum(a, b):
    randomNum = round(random.uniform(a, b), 2)
    return randomNum



outNum = getNum(1,2)
print(outNum)
