# import your functions from another file
# make sure both files are inthe same directory
# import every function that is defined inside the file you called back (functions.py)
from functions import *

# TESTING YOUR FUNCTION
# think of the epxected output for the given input
# run it, and see if the output is what you expect 
print (motherlode(2))
# we want to try to verify the expected result under all conditions
# "edge cases" are scenarios that are uncommon but could cause our code to break
# test when generate_greeting is used with two params
print(generate_greeting("Ma'am", "How's it goin'")) # should be "Hows is going Ma'am!"
# test when generate_greeting isused with one param