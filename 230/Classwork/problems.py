'''
2023-09-07
'''

# Problem 1
# num_1 = int(input())
# num_2 = int(input())

# sum = num_1 + num_2
# product = num_1 * num_2
# print(sum, '\n', product)
# # print(product)

# Problem 2
# budget = float(input())
# meal_cost = float(input())
# print ((budget//meal_cost)//4)

# Problem 3
# def tip(drink_cost):
#     tax = drink_cost * 0.08
#     print(tax)
#     return (drink_cost + tax) * 1.2
# bill = tip (10)
# print (bill)

# Problem 4
# screen_time = float(input())
# week = screen_time * 7
# month = week * 4
# year = month * 12
# print ("Week:", week, "Minutes", "\nMonth:", month, "Minutes","\nYear:", year,"Minutes")


'''
2023-09-14
'''
def a (word='hello'):
    return str(word)

def b (word='world'):
    return str(word)

def c (word_1=a(), word_2=b()):
    return word_1 + " " + word_2

print (c())

'''
Credit to Julian

def a():
    return 'hello'

def b():
    return 'world'

def c():
    return a() + b()
'''