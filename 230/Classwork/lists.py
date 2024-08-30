'''
10-19-23
Lists
'''

org = input("Enter the full name of an organization: ")

holder = []
lower = org.lower()
lower_list = lower.split(' ')
lower_list = [word for word in lower_list if word != 'the' or 'of']
holder = [word[0].upper() for word in lower_list]
acro = ''.join(holder)

print(acro)