import random
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
select = ''
attack = ''
while select not in pokedex:
    select = input('Which Pokemon do you want to use? ')
unit = random.choice(list(pokedex.keys()))
print (f"You will be facing {unit}!!!")
while player > 0 and enemy > 0:
    print(f"Your {select} HP: {player}, Enemy {unit} HP: {enemy}")
    attack =''
    while attack not in pokedex[select]['moves']:
        for move, damage in pokedex[select]['moves'].items():
            print(f"{move}: Damage {damage}")
        attack = input('Which move would you like to use? ') 
    damage = pokedex[select]['moves'][attack]
    enemy -= damage
    print(f"You dealt {damage} damage to the enemy {unit}!")
    # Enemy Turn
    enemy_moves = pokedex[select]['moves']
    enemy_attack = random.choice(list(enemy_moves.keys()))
    player -= enemy_moves[enemy_attack]
    print(f"The enemy {unit} used {enemy_attack}!")

if player <= 0:
    print (f"Your {select} fainted!")
    print ("GAME OVER")
else:
    print(f"The enemy {select} fainted. You won the battle!")

   