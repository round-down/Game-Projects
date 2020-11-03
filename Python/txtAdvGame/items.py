
class TM_01():
    def __init__(self):
        self.name = 'Scratch'
        self.next = None
        self.technical_name = 'TM_01'
        self.types = ['Normal']
        self.dmg = 5
        self.type = 'Disc'
        self.description = f'''[Physical Dmg]: {self.dmg}'''

    def __repr__(self):
        return f'''{self.name}'''

class Potion:
    def __init__(self):
        self.name = 'Potion'
        self.next = None
        self.restore = 20
        self.type = 'Medicine'
        self.description = f'''Restores: {self.restore} HP'''

    def __repr__(self):
        return str(self.name)

class PokeBall:
    def __init__(self):
        self.name = 'PokeBall'
        self.next = None
        self.catch_rate = 1.0
        self.type = 'Pocket Ball'
        self.description = f'''Catch Rate: {self.catch_rate}'''

    def __repr__(self):
        return self.name

class ItemStack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, type_of_item):
        if self.head:
            new_head  = type_of_item
            new_head.next = self.head
            self.head = new_head
            self.num_elements += 1
            return
        self.head = type_of_item
        self.num_elements += 1

    def auto_push(self, type_of_item, count):
        for num in range(0, count):
            self.push(eval(type_of_item + '()'))

    def pop(self):
        if not self.head:
            return None
        old_head = self.head
        self.head = self.head.next
        self.num_elements -= 1
        old_head.next = None
        return old_head

    def info(self, player):
        while True:
            userInput = input('[Use/Give/B]> ').lower()

            if userInput in ['u', 'use']:
                self.use(player)
                break
            elif userInput in ['g', 'give']:
                self.give(player)
                break
            elif userInput in ['b', 'back']: break

    def use(self, player):
        if self.head.type == 'Disc':
            party_member = player.list_and_choose_party_member()
            if party_member: party_member.learn_move(self)
        elif self.head.type == 'Pocket Ball' and player.in_encounter:
            if player.in_encounter == False:
                print('You\'re not allowed to use that here!!')
                return
            print(f'''{player.name} Threw a {self.head.name}!!''')
            player.set_global_pocket_ball_to_use(self.pop())

        #### A D D  M O R E  F U N C T I O N A L I T Y  H E R E ####


    def give(self, player):
        party_member = player.list_and_choose_party_member()
        if party_member: party_member.hold_item(self, player)


    def __repr__(self):
        return str(self.num_elements)
