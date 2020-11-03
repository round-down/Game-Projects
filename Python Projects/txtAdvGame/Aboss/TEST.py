import random

def gab():
    while True:
        wrong = 0
        right = 0
        print('\nWhat is Kalieb\'s age?\n')
        userInput = input('[]: ')
        if int(userInput) == 21:
            print('\nYou\'re correct!!! Want a cookie?\n')
            right += 1
        else:
            print('\nWrong answer, freakin\' dork....\n')
            print('Why don\'t you try an easier one??\n')
            wrong += 1

        print('What is Gabby\'s age?\n')
        userInput = input('[]: ')
        if int(userInput) == 65:
            print('\n...Listen, Linda...')
            wrong +=1
        elif int(userInput) == 24:
            print('\nGood yob!!!')
            right += 1
        else:
            print('\nJesus...you\'re wrong')

        try:
            print('\n\nYou\'re score is {}%'.format(2/right))
        except:
            print('\n\nYou\'re score is 0%...')
        print('\nYou got {} right and {} wrong.'.format(right, wrong))

        if right == 2:
            break
        else:
            continue

class A:
    def __init__ (self):
        self.__x = 5
        self._y = 6

class Staff:
    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        #print('Creating Staff Object')

    def __str__(self):
        return 'Position = %s, Name = %s, Pay = %d' %(self._position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s: ' %(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print('Getter Method')
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
            print('{} is now {}!'.format(self.name, value))
        else:
            print('Position is invalid. No changes made.')



def run_game():
    boo = booboo_bear(15, 60)
    gab = Player(20, 100)
    global stop
    stop = True
    print('\nYou encountered an enemy!!!\n')
    while stop:
        reg = random.randrange(4)
        if reg == 3:
            booboo_bear.regen
        else:
            continue
        print('\n\n###########################################################################\n#')
        print('#\t\t\t\t[booboo_bear HP]: {}\n'.format(boo._health))
        print('#\n#[Gabby HP]: {}\n\n\n\n'.format(gab._health))
        userInput = input('[Attack/A][Exit/E]: ')

        if userInput == 'e' or userInput == 'E':
            break
        elif userInput == 'a' or userInput == 'A':
            gab.attack = boo
            print('\n\nGabby backhannded booboo_bear off a fucking chair!!! And lost {} HP.'.format(gab._attack))
            boo.attack = gab
            print('\n\nbooboo_bear returned the favor!! Gabby lost {} HP! :O'.format(boo._attack))
        else:
            print('\n\n[Invalid Key]\n\n')


class booboo_bear:
    def __init__ (self, atk, hp):
        self._attack = atk
        self._health = hp

    def __str__(self):
        return '\nHe\'s a plant AAAANNNDD and bear, who-da thought???\n'

    def regen(self):
        print('\nThe booboo_bear used their special BLUEBERRY powers to regen life!!\n')
        if self._health >= 60:
            self._health = 60
            print('\nbooboo_bear is at Full Health!!!\n')
        else:
            self._health += random.randrange(10)

    @property
    def attack(self):
        return

    @attack.setter
    def attack(self, person):
        self._health -= person._attack
        if self._health <= 0:
            self._health = 0
            print('\nGABBY has defeated booboo_bear!!!\n')
            global stop
            stop = False
        else:
            None

class Player:
    def __init__(self, atk, hp):
        self._attack = atk
        self._health = hp

    def __str__(self):
        return '\nGABBY THE MIGHTY!!!\n'

    @property
    def attack(self):
        return

    @attack.setter
    def attack(self, person):
        self._health -= person._attack
        if self._health <= 0:
            self._health = 0
            print('\nbooboo_bear has defeated Gabby!!!\n')
            global stop
            stop = False
        else:
            None


run_game()
