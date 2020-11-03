from player import *

def main():
    p = Player()
    save = p.load()
    while True:
        print('P O C K E T  M O B S')
        print(f'''[Load: {p.name}]  [New Game]  [Options]  [Quit]''')
        userInput = input(('[L/N/o/Q]> ' if save else '[N/o/Q]> ')).lower()

        if save and userInput in ['l', 'load']:
            p.load()
            p.encounter()

        elif userInput in ['n', 'newgame', 'new', 'new game']:
            pass

        elif userInput in ['o', 'options']:
            pass

        elif userInput in ['q', 'quit']:
            quit()



main()
