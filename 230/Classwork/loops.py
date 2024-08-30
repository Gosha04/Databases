'''
Loops
'''
import random
# allow you to repeat code multiple time
# break allows us to quit loop
# continue allows us to skip to next iteration
# for and while: 2 types of loops

# WHILE LOOPS
# keep running as long as a condition is true
# infinite stuff bad

# Number Game
# num = random.randint(1, 10)
# while guess != num:
#     guess = int(input("Wrong! Guess again: "))
# print("Correct!")

# FOR LOOPS
# typically pre-determined amount of time

# max_guess = 3
# for i in range(3):
#     print (f"You have {max_guess-i} remaining")
#     guess = int(input("Number 1-10: "))
#     if guess == num:
#         print ("Correct!")
#         break
#     else: 
#         print ("Incorrect")


# NESTED LOOPS
# you can nest however many loops you want
# need to make sure your tabbing is correct
# when starting out, super helpful to write out the values of each variable on each loop iteration

seats = "LMNOP"
num_rows = 5

for row in range (num_rows):
    for letter in seats:
        print(f"{row+1}{letter}")
    print ("Next Row: ")