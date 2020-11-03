
Types = ['Fire', 'Water', 'Grass', 'Normal', 'Rock', 'Fighting', 'Bug', 'Electric', 'Psychic', 'Flying']
Natures = [None]

Poke_Keys_Evo_1 = {'Charmander': {'Name': 'Charmander',
                                  'Type': ['Fire'],
                                  'Next': [16, 'Charmeleon'],
                                  'Base Stats':{'HP': 39,
                                                'ATK': 52,
                                                'DEF': 43,
                                                'SP.ATK': 60,
                                                'SP.DEF': 50,
                                                'SPD': 60}},
                  'Squirtle': {'Name': 'Squirtle',
                                                    'Type': ['Water'],
                                                    'Next': [16, 'Wartortle'],
                                                    'Base Stats':{'HP': 44,
                                                                  'ATK': 48,
                                                                  'DEF': 65,
                                                                  'SP.ATK': 50,
                                                                  'SP.DEF': 64,
                                                                  'SPD': 43}},
                  'Magikarp': {'Name': 'Magikarp',
                                                    'Type': ['Water'],
                                                    'Next': [20, 'Gyarados'],
                                                    'Base Stats':{'HP': 20,
                                                                  'ATK': 10,
                                                                  'DEF': 55,
                                                                  'SP.ATK': 15,
                                                                  'SP.DEF': 20,
                                                                  'SPD': 80}},
                  'Bulbasaur': {'Name': 'Bulbasaur',
                                                    'Type': ['Grass'],
                                                    'Next': [16, 'Ivysaur'],
                                                    'Base Stats':{'HP': 45,
                                                                  'ATK': 49,
                                                                  'DEF': 49,
                                                                  'SP.ATK': 65,
                                                                  'SP.DEF': 65,
                                                                  'SPD': 45}},
                  'Exeggcute': {'Name': 'Exeggcute',
                                                    'Type': ['Grass', 'Psychic'],
                                                    'Next': ['Leaf_Stone', 'Exeggutor'],
                                                    'Base Stats':{'HP': 60,
                                                                  'ATK': 40,
                                                                  'DEF': 80,
                                                                  'SP.ATK': 60,
                                                                  'SP.DEF': 45,
                                                                  'SPD': 40}},
                  'Chansey': {'Name': 'Chansey',
                                                    'Type': ['Normal'],
                                                    'Next': [],
                                                    'Base Stats':{'HP': 250,
                                                                  'ATK': 5,
                                                                  'DEF': 5,
                                                                  'SP.ATK': 35,
                                                                  'SP.DEF': 105,
                                                                  'SPD': 50}},
                  'Diglett': {'Name': 'Diglett',
                                                    'Type': ['Ground'],
                                                    'Next': [26, 'Dugtrio'],
                                                    'Base Stats':{'HP': 10,
                                                                  'ATK': 55,
                                                                  'DEF': 25,
                                                                  'SP.ATK': 35,
                                                                  'SP.DEF': 45,
                                                                  'SPD': 95}},
                  'Geodude': {'Name': 'Geodude',
                                                    'Type': ['Rock', 'Ground'],
                                                    'Next': [25, 'Graveler'],
                                                    'Base Stats':{'HP': 40,
                                                                  'ATK': 80,
                                                                  'DEF': 100,
                                                                  'SP.ATK': 30,
                                                                  'SP.DEF': 30,
                                                                  'SPD': 20}},
                  'Onix': {'Name': 'Onix',
                                                    'Type': ['Rock', 'Ground'],
                                                    'Next': [],
                                                    'Base Stats':{'HP': 35,
                                                                  'ATK': 45,
                                                                  'DEF': 160,
                                                                  'SP.ATK': 30,
                                                                  'SP.DEF': 45,
                                                                  'SPD': 70}},
                  'Machop': {'Name': 'Machop',
                                                    'Type': ['Fighting'],
                                                    'Next': [28, 'Machoke'],
                                                    'Base Stats':{'HP': 70,
                                                                  'ATK': 80,
                                                                  'DEF': 50,
                                                                  'SP.ATK': 35,
                                                                  'SP.DEF': 35,
                                                                  'SPD': 35}},
                  'Hitmonlee': {'Name': 'Hitmonlee',
                                                    'Type': ['Fighting'],
                                                    'Next': [],
                                                    'Base Stats':{'HP': 50,
                                                                  'ATK': 120,
                                                                  'DEF': 53,
                                                                  'SP.ATK': 35,
                                                                  'SP.DEF': 110,
                                                                  'SPD': 87}},
                  'Caterpie': {'Name': 'Caterpie',
                                                    'Type': ['Bug'],
                                                    'Next': [7, 'Metapod'],
                                                    'Base Stats':{'HP': 45,
                                                                  'ATK': 30,
                                                                  'DEF': 35,
                                                                  'SP.ATK': 20,
                                                                  'SP.DEF': 20,
                                                                  'SPD': 45}},
                  'Weedle': {'Name': 'Weedle',
                                                    'Type': ['Bug'],
                                                    'Next': [7, 'Kakuna'],
                                                    'Base Stats':{'HP': 40,
                                                                  'ATK': 35,
                                                                  'DEF': 30,
                                                                  'SP.ATK': 20,
                                                                  'SP.DEF': 20,
                                                                  'SPD': 50}},
                  'Pikachu': {'Name': 'Pikachu',
                                                    'Type': ['Electric'],
                                                    'Next': [],
                                                    'Base Stats':{'HP': 60,
                                                                  'ATK': 90,
                                                                  'DEF': 55,
                                                                  'SP.ATK': 90,
                                                                  'SP.DEF': 80,
                                                                  'SPD': 110}},
                  'Magnemite': {'Name': 'Magnemite',
                                                    'Type': ['Electric'],
                                                    'Next': [30, 'Magneton'],
                                                    'Base Stats':{'HP': 25,
                                                                  'ATK': 35,
                                                                  'DEF': 70,
                                                                  'SP.ATK': 95,
                                                                  'SP.DEF': 55,
                                                                  'SPD': 45}},
                  'Abra': {'Name': 'Abra',
                                                    'Type': ['Psychic'],
                                                    'Next': [16, 'Kadabra'],
                                                    'Base Stats':{'HP': 25,
                                                                  'ATK': 20,
                                                                  'DEF': 15,
                                                                  'SP.ATK': 105,
                                                                  'SP.DEF': 55,
                                                                  'SPD': 90}}}


Poke_Keys_Evo_2 = {'Charmeleon' :{'Name': 'Charmeleon',
                                  'Type': ['Fire'],
                                  'Next': [36, 'Charizard'],
                                  'Base Stats':{'HP': 58,
                                                'ATK': 64,
                                                'DEF': 58,
                                                'SP.ATK': 80,
                                                'SP.DEF': 65,
                                                'SPD': 80}},
                   'Wartortle': {'Name': 'Wartortle',
                                                     'Type': ['Water', 'Flying'],
                                                     'Next': [36, 'Blastoise'],
                                                     'Base Stats':{'HP': 59,
                                                                   'ATK': 63,
                                                                   'DEF': 80,
                                                                   'SP.ATK': 65,
                                                                   'SP.DEF': 80,
                                                                   'SPD': 58}},
                   'Gyarados' : {'Name': 'Gyarados',
                                                     'Type': ['Water'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 95,
                                                                   'ATK': 125,
                                                                   'DEF': 79,
                                                                   'SP.ATK': 60,
                                                                   'SP.DEF': 100,
                                                                   'SPD': 81}},
                   'Ivysaur': {'Name': 'Ivysaur',
                                                     'Type': ['Grass'],
                                                     'Next': [32, 'Venusaur'],
                                                     'Base Stats':{'HP': 60,
                                                                   'ATK': 62,
                                                                   'DEF': 63,
                                                                   'SP.ATK': 80,
                                                                   'SP.DEF': 80,
                                                                   'SPD': 60}},
                   'Exeggutor': {'Name': 'Exeggutor',
                                                     'Type': ['Grass', 'Psychic'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 95,
                                                                   'ATK': 95,
                                                                   'DEF': 85,
                                                                   'SP.ATK': 125,
                                                                   'SP.DEF': 75,
                                                                   'SPD': 55}},
                   'Dugtrio': {'Name': 'Dugtrio',
                                                     'Type': ['Ground'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 35,
                                                                   'ATK': 100,
                                                                   'DEF': 50,
                                                                   'SP.ATK': 50,
                                                                   'SP.DEF': 70,
                                                                   'SPD': 120}},
                   'Graveler': {'Name': 'Graveler',
                                                     'Type': ['Rock', 'Ground'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 55,
                                                                   'ATK': 95,
                                                                   'DEF': 115,
                                                                   'SP.ATK': 45,
                                                                   'SP.DEF': 45,
                                                                   'SPD': 35}},
                   'Machoke': {'Name': 'Machoke',
                                                     'Type': ['Fighting'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 80,
                                                                   'ATK': 100,
                                                                   'DEF': 70,
                                                                   'SP.ATK': 50,
                                                                   'SP.DEF': 60,
                                                                   'SPD': 45}},
                   'Metapod': {'Name': 'Metapod',
                                                     'Type': ['Bug'],
                                                     'Next': [10, 'Butterfree'],
                                                     'Base Stats':{'HP': 50,
                                                                   'ATK': 20,
                                                                   'DEF': 55,
                                                                   'SP.ATK': 25,
                                                                   'SP.DEF': 25,
                                                                   'SPD': 30}},
                   'Kakuna': {'Name': 'Kakuna',
                                                     'Type': ['Bug'],
                                                     'Next': [10, 'Beedrill'],
                                                     'Base Stats':{'HP': 45,
                                                                   'ATK': 25,
                                                                   'DEF': 50,
                                                                   'SP.ATK': 25,
                                                                   'SP.DEF': 25,
                                                                   'SPD': 35}},
                   'Magneton': {'Name': 'Magneton',
                                                     'Type': ['Electric'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 50,
                                                                   'ATK': 60,
                                                                   'DEF': 95,
                                                                   'SP.ATK': 120,
                                                                   'SP.DEF': 70,
                                                                   'SPD': 70}},
                   'Kadabra': {'Name': 'Kadabra',
                                                     'Type': ['Psychic'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 40,
                                                                   'ATK': 35,
                                                                   'DEF': 30,
                                                                   'SP.ATK': 120,
                                                                   'SP.DEF': 70,
                                                                   'SPD': 105}}}

Poke_Keys_Evo_3 = {'Charizard': {'Name': 'Charizard',
                                  'Type': ['Fire', 'Flying'],
                                  'Next': [],
                                  'Base Stats':{'HP': 78,
                                                'ATK': 84,
                                                'DEF': 78,
                                                'SP.ATK': 109,
                                                'SP.DEF': 85,
                                                'SPD': 100}},
                   'Blastoise': {'Name': 'Blastoise',
                                                     'Type': ['Water'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 79,
                                                                   'ATK': 83,
                                                                   'DEF': 100,
                                                                   'SP.ATK': 85,
                                                                   'SP.DEF': 105,
                                                                   'SPD': 78}},
                   'Venusaur': {'Name': 'Venusaur',
                                                     'Type': ['Grass'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 80,
                                                                   'ATK': 82,
                                                                   'DEF': 83,
                                                                   'SP.ATK': 100,
                                                                   'SP.DEF': 100,
                                                                   'SPD': 80}},
                   'Butterfree': {'Name': 'Butterfree',
                                                     'Type': ['Bug'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 60,
                                                                   'ATK': 45,
                                                                   'DEF': 50,
                                                                   'SP.ATK': 90,
                                                                   'SP.DEF': 80,
                                                                   'SPD': 70}},
                   'Beedrill': {'Name': 'Beedrill',
                                                     'Type': ['Bug'],
                                                     'Next': [],
                                                     'Base Stats':{'HP': 65,
                                                                   'ATK': 90,
                                                                   'DEF': 40,
                                                                   'SP.ATK': 45,
                                                                   'SP.DEF': 80,
                                                                   'SPD': 75}}}
