'''
10-26-23
Sets
- unordered collection of unique items 
- there is no order/position or key/value associations
- sets cannot hold duplicates
- every item in the set must be immutable
- { item, item, item, ... }
'''
# create and empty set
empty_set = set()

# create a popoulated set
item_set = {'item1', 'item2', 'item3'}

# sets can contain different types 
mixed_set = {True, False, 'pear'}
print(mixed_set)

# add and remove
item_set.add('item4')
item_set.remove('item1')
print(item_set)

# remove a random item from set
random_item = item_set.pop()
print (random_item)
print (item_set)

# set comparisons
user_netflix = {'joshvaysman', 'grandma', 'anon123'}
user_hulu = {'theBachelor', 'grandma', 'woo789'}
user_disney = {'grandma', 'grandpa'}

# users who are ONLY in the netflix set
print (user_netflix - user_disney - user_hulu)
# users who are ONLY in hulu set
print (user_hulu - user_disney - user_netflix)
# user who are ONLY in all 3
print(user_netflix.intersection(user_hulu,user_disney))
# all users who have an account on any platform
print(user_netflix.union(user_hulu, user_disney))

# check if item is in set
if 'grandpa' in user_disney:
    print("He has an account")
else:
    print('He does not have an account')