from functions import *
from player import Player



######################## GAME RELATED FUNCTIONS ######################

def new_game():#CREATES A NEW GAME FILE AND STARTS GAME
    new_menu(1.25, 3, 75, 30, '70')
    print_alot_of('-')
    print_center('Enter a name for your new save file...\n', 0.01)
    print_alot_of('-')
    print_slow('\n[Exit]\n', 0.01)
    while True:
        userInput = input('[E/File Name]> ')
        if userInput == 'e' or userInput == 'E':
            printmenu(0.001)
            break
        elif userInput == '':
            print_IK()
        else:
            try:#WILL RUN IF FILE EXISTS
                f = open ('saves\{}.save'.format(userInput), 'r+')
                f.close()
                print_slow('\n{}.save already exists, overwrite it?\n'.format(userInput), 0.01)
                confirm_Input = input('[Y/n]> ')
                if confirm_Input == 'y' or confirm_Input == 'Y':
                    print_slow('\nAll previous progress will be lost. Are you sure?\n', 0.01)
                    confirm_Input_again = input('[YES/NO]: ')
                    if confirm_Input_again == 'YES' or confirm_Input_again == 'yes':
                        print_center('[WIPING SAVE FILE...]', 1)
                        os.remove('saves\{}.save'.format(userInput))
                        f = open ('saves\{}.save'.format(userInput), 'a')
                        set_save(userInput)
                    elif confirm_Input_again == 'NO' or confirm_Input_again == 'no':
                        print_center('[Canceling Overwrite...]', 2)
                        printmenu(0.001)
                        break
                    else:
                        print_center('[Invalid Key] [Canceling Overwrite...]', 2)
                        printmenu(0.001)
                        break
                elif confirm_Input == 'n' or confirm_Input == 'N':
                    print_center('[Invalid Key] [Canceling Overwrite...]', 2)
                    printmenu(0.001)
                    break
                else:
                    print_center('[Invalid Key] [Canceling Overwrite...]', 2)
                    printmenu(0.001)
                    break

            except:#WILL RUN IF FILE DOESNT EXIST
                f = open ('saves\{}.save'.format(userInput), 'a')
                set_save(userInput)


            new_menu(1.75, 3, 75, 30, '70')
            print_alot_of('-')
            print_center('[In-Game Name]\n', 0.001)
            print_alot_of('-')
            while True:
                userInput = input('[User]> ')
                if userInput == '':
                    print_IK()
                else:
                    f.write('{}'.format(userInput))
                    break

            new_menu(1.8, 3, 75, 30, '70')
            print_alot_of('-')
            print_center('[Choose Your Pocket Mob]\n', 0.001)
            print_alot_of('-')
            print_slow('[1]   [2]   [3]\n', 0.01)
            while True:
                userInput = input('[1][2][3]> ')
                if userInput == '1':
                    f.write('\n1')
                    break
                elif userInput == '2':
                    f.write('\n2')
                    break
                elif userInput == '3':
                    f.write('\n3')
                    break
                else:
                    print_IK()

            f.close()
            print('\n')
            print_center('[S a v i n g...]\n', 0.05)

            try:
                p.new_player()
            except Exception as e:
                log_err(e, '[Error whilst instantiating new_player]')
                print_alot_of('#')
                print_center('[Something Terrible Has Happened]\n', 1)
                print_alot_of('#')
                time.sleep(2)
                printmenu(0.001)
                break

            start_game()
            break

def load_game():#LOCATES SAVE FILE NAME AND SETS GLOBAL VARIABLE
    new_menu(3, 3, 75, 30, '70')
    print_slow('\n[Exit]\n', 0.01)
    while True:
        userInput = input('[E/Save Name]> ')
        if userInput == 'e' or userInput == 'E':
            set_save(None)
            printmenu(0.001)
            break
        elif userInput == '':
            print_IK()
        else:
            try:
                try:
                    f = open ('saves\{}.save'.format(userInput), 'r+')
                    f.close()
                except Exception as e:
                    log_err(e, 'Encountered While Loading Game')
                    print_center('[File not found]\n', 1)
                    printmenu(0.001)
                    break
                set_save(userInput)
                print('\n')
                print_center('[L o a d i n g...]\n', 1)

                try:
                    p.load_player()
                except Exception as e:
                    log_err(e, '[Error whilst instantiating new_player]')
                    print_alot_of('#')
                    print_center('[Something Terrible Has Happened]\n', 1)
                    print_alot_of('#')
                    time.sleep(2)
                    printmenu(0.001)
                    break

                start_game()
                break
            except Exception as e:
                log_err(e, 'Encountered While Loading Game')
                print_IK()

def options():#GAME SETTINGS MENU
    new_menu(4, 5, 75, 30, '07')
    print_slow('\n[Back] [Rename Save] [Delete Save]\n', 0.01)
    while True:
        userInput = input('[B][R][D]> ')
        if userInput == 'b' or userInput == 'B':
            printmenu(0.01)
            break
        elif userInput == 'r' or userInput == 'R':
            userInput = input('\n[File Name]> ')
            try:
                f = open('saves\{}.save'.format(userInput), 'r+')
                f.close()
                rename_userInput = input('\n[New name for {}.save]> '.format(userInput))
                if rename_userInput == '':
                    print_center('[Invalid Key] [Canceling Rename...]\n\n', 1)
                    print_slow('[Back] [Rename Save] [Delete Save]\n', 0.01)
                else:
                    os.rename('saves\{}.save'.format(userInput),'saves\{}.save'.format(rename_userInput))
                    print_center('Renamed!\n\n', 1)
                    print_slow('[Back] [Rename Save] [Delete Save]\n', 0.01)
            except Exception as e:
                log_err(e, 'Options Menu')
                print_slow('\n{}.save doesn\'t exist...'.format(userInput), 1)
                print_IK()
        elif userInput == 'd' or userInput == 'D':
            userInput = input('\n[File Name]> ')
            try:
                f = open('saves\{}.save'.format(userInput), 'r+')
                f.close()
                print_slow('\nAre you sure you want to delete {}.save\n'.format(userInput), 0.01)
                confirm_userInput = input('[Y/n]> ')
                if confirm_userInput == 'y' or confirm_userInput == 'Y':
                    os.remove('saves\{}.save'.format(userInput))
                    print_center('Deleted!\n', 1)
                    print_slow('[Back] [Rename Save] [Delete Save]\n', 0.01)
                elif confirm_userInput == 'n' or confirm_userInput == 'N':
                    print_center('[Canceling Deletion...]\n\n', 1)
                    print_slow('\n[Back] [Rename Save] [Delete Save]\n', 0.01)
                else:
                    print_center('[Invalid Key] [Canceling Deletion...]\n\n', 1)
                    print_slow('[Back] [Rename Save] [Delete Save]\n', 0.01)
            except Exception as e:
                log_err(e, 'Options Menu')
                print_slow('\n{}.save doesn\'t exist...'.format(userInput), 1)
                print_IK()
        else:
            print_IK()

def start_game():#PREMATURE START GAME FUNCTION
    printmenu(0.001)
    None

######################################################################


######################## M A I N    L O O P    B E L O W ######################

def main_menu():
    p = Player()

    intro('#', 0.01)
    printmenu(0.1)

    try:

        while True:
            userInput = input('[N][L][C][O][Q]> ')

            if userInput == 'n' or userInput == 'N':#NEW GAME
                new_game()

            elif userInput == 'l' or userInput == 'L':#LOAD GAME
                load_game()

            elif userInput == 'c' or userInput == 'C':#CREDITS
                printcred(0.05, True)

            elif userInput == 'o' or userInput == 'O':#OPTIONS
                options()

            elif userInput == 'q' or userInput == 'Q':#KILL PROGRAM
                break

            else:#INVALID KEY PRESS
                print_IK()

    except Exception as e:
        #save_game()#SAVES GAME BEFORE ERROR IS LISTED
        log_err(e, 'Something Terrible Has Happened...')
        print('\n\n', e, '\n\n')


main_menu()
