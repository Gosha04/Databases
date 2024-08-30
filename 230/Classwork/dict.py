import random
# 10-24-23
'''
Dictionaries
- associative data structure
- map keys to values

Rules
- cannot have duplicate keys
- keys must be immutable
    (String, tuples, ints, etc)
- values can be whatever
- designed to be one way lookup
    key -> value
possible to go the other way but less efficient
'''
# # creating a dictionary
# # empty_dict = {}
# # # create a dict with initial value
# # state_capitals = {
# #     'TX': 'Austin',
# #     'NY': 'Albany',
# #     'CA': 'Sacramento'
# #     }
# # print(state_capitals)
# # # add an entry
# # state_capitals['MI'] = 'Lansing'
# # print(state_capitals)

# # # updating a value for a given key
# # state_capitals['TX'] = 'Marfa'
# # print(state_capitals)

# # # loop through dictionaries
# # # if you just loop through the dictionary object,
# # # your loop variable will be the keys by default 
# # for _ in state_capitals:
# #     print (_)

# # for _ in state_capitals.values():
# #     print(_)

# # for _ in state_capitals.items():
# #     print(_)

# # for key, val in state_capitals.items():
# #     print(f"The capital of {key} is {val}.")

# player = {
#     'John': {
#     'type': "Wizard",
#     'level': 3,
#     'health': '90'
# },
# 'Julia': {
#     'type': 'Giant',
#     'level': 27,
#     'health': 95
# },
# 'Larry': {
#     'type': 'Warrior',
#     'level': 1,
#     'health': 15
# }
# }

# larry_stats = player['Larry']
# # print(larry_stats)

pokedex = {
    'pikachu': {
        'type': 'electric',
        'moves': {
            'QA' : random.randint(7, 14),
            'Thunderbolt': random.randint(9, 12)
        },
    },
    'charmander': {
        'type': 'fire',
        'moves': {
            'Ember' : random.randint(8, 15),
            'Inferno': random.randint(10, 11)
        },
    }
}



player = 100
enemy = 100

for _ in pokedex:
    print (_)
select = input('Which Pokemon do you want to use? ')
unit = random.choice([pokedex.keys()])
print (f"You will be facing {enemy_unit}!!!")
while player >= 0 or enemy >= 0:
    for _ in pokedex[select]:
        print (_)
    attack = input('Which move would you like to use? ')
    enemy -= attack
    defend = random.choice(pokedex[unit.value()])
