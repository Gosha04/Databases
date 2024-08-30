'''
Conditionals
09-19-2023
'''
# Print out a menu to the user asking if they want an inspirational quit,
# song lyric, or affirmation. Based on their choice, print out the appropriate response

# print ("""
# ~*~ Menu ~*~
# 1 - Quote
# 2 - Song
# 3 - Affirmation
#  """)

# choice = int(input("Select an Option (1/2/3): "))

# if choice == 1:
#     print("We're So Back")
# elif choice == 2:
#     print("Never gonna give you up")
# elif choice == 3:
#     print("Never back down, never what??? Never give up!")
# else:
#     print("Pick an actual option jackass")

'''
MODULES
- think of them as expansion packs for python
- you import them and then you can use a bunch of exciting functions
- some modules you can donwload from the internet and install
(spotify, googlemaps, sklearn)
'''
# Typically we import modules first at the top of our files

import math, random

# generate random numbers with randint() method
# pass in 2 params - lower and upper bound
# MIN = 1
# MAX = 100
# random_num = random.randint(MIN, MAX)
# print(f"Computer Generated ~ |{random_num}| ~")

# groundhog day program
# 30% odds that groundhog will see his shadow
# 70% odds that groundhog will not see his shadow

groundhog = random.randint(1, 10)

if groundhog >= 7:
    print("Groundhog hasn't seen his shadow")
else:
    print("Groundhog has seen his shadow")

print(f"~ |{groundhog}| ~")