import os, sys, time, random, datetime



######################## TOOLS ######################

def log_err(error, comment):
    if comment == None:
        comment == 'No Comment'
    try:#WILL CHECK IF LOG FILE EXISTS
        f = open ('log.txt', 'r+')
        f.close()

        f = open('log.txt', 'a')
        f.write('\n{}\t{}\t{}'.format(datetime.datetime.now(), error, comment))
        f.close()

    except Exception as e:#WILL CREATE A NEW LOG FILE IF IT DOESNT EXIST
        f = open('log.txt', 'a')
        f.write('[Log File Created]\t{}\t{}'.format(e, datetime.datetime.now()))
        f.write('\n{}\t{}\t{}'.format(datetime.datetime.now(), error, comment))
        f.close()#WILL LOG COMMON AND FATAL ERROR MESSAGES AND CREATE A LOG FILE IF NOT FOUND

def check_save():
    set_window(75, 30, '70')
    if not os.path.exists('saves'):
        os.makedirs('saves')
        box_phrase('Creating file save directory...', '>', '|', 0.01)
    else:
        box_phrase('File save directory found...', '#', '|', 0.01)
    time.sleep(2)#CREATES AND/OR CHECKS IF saves DIR EXISTS

def set_window(x, y, color):
    os.system('mode {}, {}'.format(x, y))
    os.system('color {}'.format(color))#SETS WINDOW SIZE ALONG WITH FORGROUND AND BACKGROUND COLOR

def new_menu(currentmenu_num, clear_screen_num, screen_size_x, screen_size_y, color):#COMMON NEW MENU OPTIONS
    currentmenu(currentmenu_num)
    clear_screen(clear_screen_num)
    rg()
    set_window(screen_size_x, screen_size_y, color)

def currentmenu(num):#SETS CURRENT MENU VALUE TO HANDLE INVALID KEY REPRINTS
    global current
    current = num
    return current

def get_currentmenu_num():
    global current
    return current#RETURNS CURRENT MENU NUMBER

def clear_screen(num):#WIPE SCREEN LOG
    counter = 0
    while num >= counter:
        print('\n')
        counter += 1

def get_screen_size(num):#RETURNS EITHER THE WIDTH OR HEIGHT OF TERMINAL
    string = str(os.get_terminal_size())

    screen_size = []
    series = []

    for i in string:
        try:
            int(i)
            series.append(1)
            if series[len(series)-2] == 1:
                screen_size[len(screen_size)-1] += i
            else:
                screen_size.append(i)

        except:
            series.append(0)

    series = []
    if num == 0:#RETURNS WIDTH
        return int(screen_size[num])
    elif num == 1:#RETURNS HEIGHT
        return int(screen_size[num])

def get_global_IKC():
    global IKC
    return IKC

def rg():#RESETS Invalid Key GLOBAL VARIABLE
    global IKC
    IKC = 0



####################### T E X T  R E L A T E D ##############################

def print_alot_of(str, counter = get_screen_size(0)):
    print(str*counter)

def print_center(str, spd):
    print_slow(str.center(get_screen_size(0)), spd)#BASED ON THE WINDOW SIZE, THIS WILL CENTER ANY TEXT

def print_slow(str, num):#TEXT SPEED
    #for letter in str:
        #sys.stdout.write(letter)
        #time.sleep(num)
    time.sleep(int(num/2))
    print(str)
    time.sleep(num)

def print_IK():#HANDLES INVALID KEY PRESSES
    print_center('[Invalid Key]\n', 0.1)
    global IKC
    IKC += 1
    try:
        if IKC >= 5:
            IKC = 0
            global current
            if current == 1:
                printmenu(0.001)
            elif current == 1.25:
                print_slow('\nEnter a name for your new save file...', 0.001)
                print_slow('\n[Exit]\n', 0.01)
            elif current == 1.75:
                print_alot_of('-')
                print_center('[In-Game Name]\n', 0.001)
                print_alot_of('-')
            elif current == 1.8:
                print_alot_of('-')
                print_center('[Choose Your Pocket Mob]\n', 0.001)
                print_alot_of('-')
                print_slow('[1]   [2]   [3]\n', 0.001)
            elif current == 2:
                printcred(0.001, False)
            elif current == 3:
                print_slow('[Exit]\n', 0.001)
            elif current == 4:
                print_slow('\n[Back] [Rename Save] [Delete Save]\n', 0.001)
            elif (5 <= current <= 5.75):
                IKC = 5
    except Exception as e:
        log_err(e)

def box_phrase(str, hor, vert, spd):#Basic Form
    screen_size_x = get_screen_size(0) - 4

    string = ' '
    if len(str) >= screen_size_x:#for a paragraph
        counter = screen_size_x
    else:#for a short sentence or statement
        counter = len(str)
    while counter != - 2:#adds the horizontal configuration
        string += hor
        counter -= 1

    string_wall = ' ' + vert#same thing but has spaces in the middle and only a left and right vertical configuration
    if len(str) >= screen_size_x:
        counter = screen_size_x
    else:
        counter = len(str)
    while counter != 0:
        string_wall += ' '
        counter -= 1
    string_wall += vert

    print_slow(string, spd)
    print_slow(string_wall, spd)

    __box_phrase2(str, hor, vert, spd)

    print_slow(string_wall, spd)
    print_slow(string, spd)

def __box_phrase2(str, hor, vert, spd):#General Form
    screen_size_x = get_screen_size(0) - 4
    constant = __line_counter(str, screen_size_x)#2 Constants

    lines = __line_counter(str, screen_size_x)
    start_phrase = ' ' + vert
    while lines != 0:#Controls the amount of lines to print based on the 'lines' variable
        start_phrase = ' ' + vert
        counter = 0
        if len(str) >= screen_size_x:#used if the text length is greater than the screen width
            fix = __para_fix(str, screen_size_x)
            difference = screen_size_x - fix
            while counter != fix:#Calls and sets an appropriate limit for counter to go to based on the fixer output
                start_phrase += str[0]
                str = str[1:len(str)]
                counter += 1
            while difference != 0:#fixes the amount of spaces needed to add a vert configuration
                start_phrase += ' '
                difference -= 1
        else:#used if length of text and/or the rest of the text in a paragraph is shorter than the screen width
            max = len(str)
            while counter != max:
                start_phrase += str[0]
                str = str[1:len(str)]
                counter += 1

        if lines == 1 and constant >= 2:#if text is a paragraph with at least 2 lines, this will add spaces to then end of the last line
            counter = screen_size_x - len(start_phrase) + 2
            while counter != 0:
                start_phrase += ' '
                counter -= 1
            new_phrase = start_phrase + vert
        else:
            new_phrase = start_phrase + vert
        print_slow(new_phrase, spd)

        lines -= 1

#ADD TWO UNDERSCORES AFTER FINISHED TESTING...
def __line_counter(str, width):#Returns the amount of lines needed to be boxed
    phrase_length = len(str)
    quotient = int(phrase_length/width)
    if quotient * width != phrase_length:#Therefore a Float Value
        quotient += 1
        return quotient
    else:#An integer
        return quotient

def __para_fix(str, width):#will output the total value of words and spaces that can fit within the screen size
    str += ' '
    sum = 0
    distance = 0
    for i in str:
        if i == ' ':
            if sum + distance >= width:
                break
            else:
                sum += distance + 1
                distance = 0
        else:
            distance += 1
    return sum


############################################################################



###################################################

################### M E N U  P R I N T S ####################

def printmenu(spd):#MAIN MENU
    new_menu(1, 5, 75, 30, '70')
    print_alot_of('-')
    print_center('P O C K E T  M O B S', spd)
    print_center('[New Game]  [Load Game]  [Credits]  [Options]  [Quit]\n', spd/10)
    print_alot_of('-')
    return

def printcred(spd, condition):#CREDITS MENU
    new_menu(2, 5, 75, 30, '07')
    print_alot_of('-')
    print_center('ABBACUS INC.', spd)
    print_center('Co-Creators: AbossDev & Parlite\n\n', spd/10)
    print_slow('[Back]\n', 0.01)
    if condition == True:
        while True:
            userInput = input('[B]> ')
            if userInput == 'b' or userInput == 'B':
                rg()
                printmenu(0.01)
                break
            else:
                print_IK()
                continue

def intro(str, spd):
    x = get_screen_size(0)

    string = '\n'
    while x != 0:
        string += str
        x -= 1
        print_slow(string[::-1], spd)


    x = get_screen_size(0)
    z = 0

    string = ''
    while x != 0:
        if len(string) < x-1:
            string += str
        elif len(string) == x-1:
            x -= 1

            z += 1
            z_counter = 0
            while z_counter != z:
                string += ' '
                z_counter += 1

            print_slow(string[::-1], spd)
            string = ''



    x = get_screen_size(0)
    z = 0

    string = ''
    while x != 0:
        if len(string) < x-1:
            string += ' '
        elif len(string) == x-1:
            x -= 1

            z += 1
            z_counter = 0
            while z_counter != z:
                string += str
                z_counter += 1

            print_slow(string[::-1], spd)
            string = ''


    x = get_screen_size(0)
    z = 0

    string = ''
    while x != 0:
        if len(string) < x-1:
            string += str
        elif len(string) == x-1:
            x -= 1

            z += 1
            z_counter = 0
            while z_counter != z:
                string += ' '
                z_counter += 1

            print_slow(string, spd)
            string = ''


    x = get_screen_size(0) * 5
    z = random.randint(x-random.randint(1, 5), x)

    string = ''
    while x != 0:
        if x == z:
            string += str
            z = random.randint(x-random.randint(1, 5), x)
            x -= 1
        else:
            string += ' '
            x -= 1
            z = random.randint(x-random.randint(1, 5), x)

        print_slow(string[::-1], spd)


    x = get_screen_size(0)
    y = get_screen_size(1)

    string = ''
    while x != 0:
        string += str
        x -= 1
    while y != 0:
        print_slow(string, spd)
        y -= 1

    time.sleep(1)


##############################################################
