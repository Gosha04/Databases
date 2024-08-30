'''
ERROR HANDLING
- allows us to anticipate potential errors due to unexpected input 
and respond appropriately in code
- very common to get uneexpected input from files or from user input
'''

# user error handling to verigy the type of user input 
# user_input = input('Enter a number: ')
# try: 
#     # this code runs and may cause an error
#     user_input = int(user_input)
# except:
#     # runs if an Error ocurs above in the try block
#     print("You didn't enter a number")
# else:
#     # runs if no Error occurs and try ran successfully
#     print('Thanks for following instructions')
# finally:
#     # runs no matter what, after the try and except finish
#     print(f"You entered {user_input}")

# putting our user input inside a loop
# and continuing to prompt for more input until
# they give us the correct type of input

# while True:
#     user_input = input('Enter a number: ')
#     try: 
#     # this code runs and may cause an error
#         user_input = int(user_input)
#         break
#     except:
#     # runs if an Error ocurs above in the try block
# #         print("Invalid input, please try again")

# fruits = ['apple','pear', 'banana', 'orange']
# selection = input('Enter which number fruit you would like: ')
# try:
#     selection = int(selection)
#     selected_fruit = fruits[selection]
# except ValueError:
#     print('You did not enter a number')
# except IndexError:
#     print("Your fruit doesn't exist")
# except:
#     print('Something went wrong')
# else: 
#     print(f"You selected {selected_fruit}")

min_tempo = int(input("Please input the minimum tempo, default is 60: "))
