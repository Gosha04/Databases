'''
Functions
'''

# DEFINING FUNCTIONS
# we just specify what the function does and how it should be used
# does not get executed until called

# this is a function named "generate greeting"
# it has one parameter called "name" that should be a string
# returns one output that should be a string
def generate_greeting (name): #method signature
    '''
    This method accepts the name of a user and gives
    a greeting back using their name.

    Params 
    --------
    - name : str
    
    Returns 
    --------
    - str : the greeting with the name
    '''
    return "Howdy, " + name
# print (generate_greeting ("Josh"))

# Parameter DEFAULTS
# you can have as many parameters as you want
# and you can also set defualt values for params
# if an argumetn for that param is not passed in, the default value is used
# any params with defaults should be listed at the end of the signature
def generate_greeting (name, greeting= "Howdy", punctuation = "!"):
    return greeting + ", " + name + punctuation

# call with 2 arguments
# print (generate_greeting(str(input()), str(input())), str(input()))
# if we do not pass in an argument for greeting the default will be used
# print (generate_greeting("Miss"))

# TODO: Build on this code to ask the user for input
# for each value (the name and the greeting)
# then call the function and pass in those values as arguments
# BONUS: add an extra parameter for punctuation and modify
# your function to add that punctuation to the end

'''
2023-09-14
'''

def motherlode(initial_money):
    return initial_money * 100

# runs these on import to make sure file works ^^

# only runs this from import
if __name__ == "main":
    print (motherlode(20))