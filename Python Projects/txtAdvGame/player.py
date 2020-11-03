from items import *
from pocketmobs import *

class Player:
    def __init__(self):
        self.name = None
        self.party = []
        self.pc = []
        self.bag = {'Medicines': {}, 'Battle Items': {}, 'Pocket Balls': {}, 'Key Items': {}, 'Discs': {}}
        self.in_encounter = False

    def load(self):
        try:
            with open('save.stat', 'r') as f:
                raw_data = f.readlines()
                self.name = raw_data[0].strip('\n')

                party = eval(raw_data[1].strip('\n'))
                stats = []
                for obj_key in party.keys():
                    for stat in party[obj_key].keys():
                        stats.append(party[obj_key][stat])
                    if stats: self.party.append(PocketMob(*stats))
                    stats = []

                pc = eval(raw_data[2].strip('\n'))
                stats = []
                for obj_key in pc.keys():
                    for stat in pc[obj_key].keys():
                        stats.append(pc[obj_key][stat])
                    if stats: self.pc.append(PocketMob(*stats))
                    stats = []

                self.bag = eval(raw_data[3])
                for key in self.bag.keys():
                    for nested_key in self.bag[key]:
                        count = self.bag[key][nested_key]
                        self.bag[key][nested_key] = ItemStack()
                        self.bag[key][nested_key].auto_push(nested_key[0:-1], count)

        except Exception as e:
            print(e)
            userInput = input('[Input User]> ')
            self.name = userInput

    def save(self):
        with open('save.stat', 'w') as f:
            f.write(str(self.name) + '\n')

            party = {}
            for obj_key in self.party:
                party[str(obj_key)] = {}
                party[str(obj_key)]['Name'] = obj_key.name
                party[str(obj_key)]['Type'] = obj_key.type
                party[str(obj_key)]['Next'] = obj_key.next
                party[str(obj_key)]['Base Stats'] = obj_key.base_stats
                for move in obj_key.moves:
                    if move: obj_key.moves[obj_key.moves.index(move)] = move.technical_name
                    party[str(obj_key)]['Moves'] = obj_key.moves
                    party[str(obj_key)]['Health Points'] = obj_key.hp
                party[str(obj_key)]['Level'] = obj_key.lvl
                party[str(obj_key)]['Nature'] = obj_key.nature
                party[str(obj_key)]['Item'] = (obj_key.item.name if obj_key.item else obj_key.item)
            f.write(str(party) + '\n')

            pc = {}
            for obj_key in self.pc:
                pc[str(obj_key)] = {}
                pc[str(obj_key)]['Name'] = obj_key.name
                pc[str(obj_key)]['Type'] = obj_key.type
                pc[str(obj_key)]['Next'] = obj_key.next
                pc[str(obj_key)]['Base Stats'] = obj_key.base_stats
                for move in obj_key.moves:
                    if move: obj_key.moves[obj_key.moves.index(move)] = move.technical_name
                    pc[str(obj_key)]['Moves'] = obj_key.moves
                    pc[str(obj_key)]['Health Points'] = obj_key.hp
                pc[str(obj_key)]['Level'] = obj_key.lvl
                pc[str(obj_key)]['Nature'] = obj_key.nature
                pc[str(obj_key)]['Item'] = (obj_key.item.name if obj_key.item else obj_key.item)
            f.write(str(pc) + '\n')

            f.write(str(self.bag))

    def party_is_full(self):
        return len(self.party) == 6

    def add_item(self, location, type_of_item, count):
        if type_of_item + 's' in self.bag[location].keys():
            self.bag[location][type_of_item + 's'].auto_push(type_of_item, count)
        else:
            self.bag[location][type_of_item + 's'] = ItemStack()
            self.bag[location][type_of_item + 's'].auto_push(type_of_item, count)

    def caught_pokemon(self, mob):
        location = (self.pc if self.party_is_full() else self.party)
        location.append(mob)

    def printbag(self, location):
        reference = {'M':'Medicines', 'B':'Battle Items', 'P':'Pocket Balls', 'K':'Key Items', 'D':'Discs'}
        print(f'''\n{reference[location[0]]}''')
        commands = ['M', 'B', 'P', 'K', 'D']
        commands.remove(location[0])

        command_numbers = []
        bag_ref = {}
        for num, item in enumerate(self.bag[location].keys()):
            command_numbers.append(str(num))
            bag_ref[str(num)] = self.bag[location][item]
            print(f'''{num}| {item} x{self.bag[location][item]}\t{self.bag[location][item].head.description}''')

        command_string = '['
        for character in commands:
            command_string += str(character) + '/'
        command_string += ('Empty/E]> ' if command_numbers == [] else '{}-{}/E]> '.format(command_numbers[0], command_numbers[-1]))
        commands += command_numbers
        while True:
            userInput = input(command_string).upper()

            if userInput in commands:
                try:
                    int(userInput)
                    bag_ref[userInput].info(self)
                    if pocket_ball_to_use: return
                except:
                    self.printbag(reference[userInput])
                    break
            elif userInput.lower() in ['e', 'exit']: break

            re_print = []
            for num, item in enumerate(self.bag[location].keys()):
                if not self.bag[location][item].num_elements == 0: re_print.append(f'''{num}| {item} x{self.bag[location][item]}\t{self.bag[location][item].head}''')
                else:
                    del self.bag[location][item]
                    self.printbag(reference[location[0]])
                    return

            print(f'''\n{reference[location[0]]}''')
            for item in re_print: print(item)

    def list_and_choose_party_member(self):
        print(f'''\nParty:''')
        for num, pocketmob in enumerate(self.party):
            print(f'''{num}| {pocketmob.name}, Lvl: {pocketmob.lvl}, HP: {pocketmob.hp}, Item: {pocketmob.item}''')
        while True:
            userInput = input('[0-{}/B]> '.format(len(self.party) - 1))
            try:
                if 0 <= int(userInput) <= len(self.party) - 1: return self.party[int(userInput)]
            except:
                if userInput.lower() in ['b', 'back']: break

    def set_global_pocket_ball_to_use(self, obj=None):
        global pocket_ball_to_use
        pocket_ball_to_use = obj

    def encounter(self):
        wild_mob = create()
        player_mob = self.party[0]
        self.in_encounter = True
        self.set_global_pocket_ball_to_use()
        while True:
            print(30*'#')
            print(f'''{wild_mob.name}  Lvl: {wild_mob.lvl}  HP: {wild_mob.hp}''')
            print(f'''{player_mob.name}  Lvl: {player_mob.lvl}  HP: {player_mob.hp}''')
            userInput = input('[Fight/Bag/Party/Run]> ').lower()

            if userInput in ['f', 'fight']:
                pass

            elif userInput in ['b', 'bag']:
                self.printbag('Medicines')
                if pocket_ball_to_use:
                    wild_mob = wild_mob.catch(self)
                    self.set_global_pocket_ball_to_use()

            elif userInput in ['p', 'party']:
                new_player_mob = self.list_and_choose_party_member()
                if player_mob == new_player_mob:
                    print('That Pocket Mob is already out!')
                    continue
                elif new_player_mob: player_mob = new_player_mob
                else: continue

            elif userInput in ['c', 'catch']: wild_mob = wild_mob.catch(self)

            elif userInput in ['r', 'run']:
                self.save()
                self.in_encounter = False
                break

            elif userInput in ['t', 'test']:
                    print(f'''\nParty: {self.party}''')
                    for mob in self.party:
                        print(f'''{mob.name} Lvl: {mob.lvl}, HP: {mob.hp}, Moves: {mob.moves}, Type: {mob.type}, Item: {mob.item}''')
                    print(f'''\nPC: {self.pc}''')
                    for mob in self.pc:
                        print(f'''{mob.name} Lvl: {mob.lvl}, HP: {mob.hp}, Moves: {mob.moves}, Type: {mob.type}, Item: {mob.item}''')
                    print(f'''\nBag: {self.bag}\n''')

            elif userInput in ['g', 'give']:
                p.add_item('Pocket Balls', 'PokeBall', 3)
                p.add_item('Medicines', 'Potion', 5)
                p.add_item('Discs', 'TM_01', 2)

p = Player()
p.encounter()
