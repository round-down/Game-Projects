from functions import *



areas = ['Home', 'Revial\'s House', 'Pine\'s Lab', 'Kid', 'Pond', 'Town Folk']
areas2 = ['Home', 'Revial\'s House', 'Pine\'s Lab', 'Kid', 'Pond', 'Town Folk', 'Gym', 'Charger', 'Mart']
areas3 = ['Home', 'Revial\'s House', 'Pine\'s Lab', 'Kid', 'Pond', 'Town Folk', 'Gym', 'CHARGER', 'Mart', 'Tower', '45678', 'Test', 'PC Center']
areas4 = ['Home', 'Revial\'s House', 'Pine\'s Lab', 'Kid', 'Pond', 'Town Folk', 'Gym', 'CHARGER', 'Mart', 'Tower', '5456789', 'Test', 'PC Center']
areas5 = ['Home', 'Revial\'s House', 'Pine\'s Lab', 'Kid', 'Pond', 'Town Folk', 'Gym', 'CHARGER', 'Mart', 'Tower', '145678912345', 'Test', 'PC Center']
areas6 = ['Home', 'Revial\'s House', 'Pine\'s Lab', 'Kid', 'Pond', 'Town Folk', 'Gym', 'CHARGER', 'Mart', 'Tower', '6123456', 'Test', 'PC Center']

def map_menu(list, hor = ')', vert = '|', spacing = '   ', screen_size_x = get_screen_size(0) - 2):
    top_string = ' ' + hor * screen_size_x
    line_space = ' ' + vert + ' ' * (screen_size_x - 2) + vert
    print(top_string, line_space)
    middle_string = ' ' + vert + ' '
    for place in list:
        if len(middle_string + place + spacing) < screen_size_x:
            middle_string += place.upper() + spacing
            if place == list[-1]:
                middle_string += ' '*(screen_size_x - len(middle_string)) + vert
                print(middle_string, line_space)
        else:
            middle_string += ' '*(screen_size_x - len(middle_string)) + vert
            print(middle_string, line_space)
            middle_string = ' ' + vert + ' '
    print(top_string)

map_menu(areas)
map_menu(areas2)
map_menu(areas3)
map_menu(areas4)
map_menu(areas5)
map_menu(areas6, spacing = '     ')
