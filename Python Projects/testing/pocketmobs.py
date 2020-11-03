from random import randint
from items import *
from pocketmoblist import *


class PocketMob:
    def __init__(self, name='Testing Pocket Mob', type=Types[randint(0, len(Types) - 1)], next=None, base_stats={'HP': 5, 'ATK': 5, 'SP.ATK': 5, 'DEF': 5, 'SP.DEF': 5, 'SPD': 5}, moves=['TM_01', None, None, None], hp=randint(20, 30), lvl=randint(1, 5), nature=Natures[randint(0, len(Natures) - 1)], item=None):
        self.name = name
        self.nature = nature
        self.lvl = int(lvl)
        self.hp = int(hp)
        self.max_hp = self.hp
        self.moves = [eval(move + '()') if move else None for move in moves]
        self.type = type
        self.item = (eval(item + '()') if item else None)
        self.next = next
        self.base_stats = base_stats

    def catch(self, player):
        print('HELLO!')
        if randint(0, 3) == 2:
            print(f'''You caught {self.name}!!''')
            player.caught_pokemon(self)
            return create()
        print(f'''They were almost caught!''')
        return self

    def learn_move(self, disc_stack):
        for num, move in enumerate(self.moves):
            print(f'''[{num}] [{move}]''')
        while True:
            userInput = input('[0-3/B]> ')
            try:
                if 0 <= int(userInput) <= 3:
                    self.moves[int(userInput)] = disc_stack.pop()
                    print(self.moves)
                    break
            except:
                if userInput.lower() in ['b', 'back']: break

    def hold_item(self, item_stack, player):
        if self.item:
            if self.item.type == 'Disc': self.item.name = self.item.technical_name
            try: player.bag[self.item.type + 's'][self.item.name + 's'].auto_push(self.item.name, 1)
            except: player.add_item(self.item.type + 's', self.item.name, 1)
        self.item = item_stack.pop()

def create():
    stats = []
    pocketmobs = list(Poke_Keys_Evo_1.keys())
    key = pocketmobs[randint(0, len(pocketmobs) - 1)]
    for stat in Poke_Keys_Evo_1[key]:
        stats.append(Poke_Keys_Evo_1[key][stat])
    return PocketMob(*stats)
