'''
FILES
- allow us to persist data between program runs
- allow us to read in data to our program without having to
modify hard-coded values in our program
- file modes determine if we are reading/writing/appending to a file
- you have to specify which file mode you want when you open a file
    - r: read
    - w: write
    - a: write with append
'''

# write a program that takes in a file name
# reads every number in that files
# prints out the minimum number
nums = [] # create empty list to hold our numbers
# open up the file and read in its contents
# open(FILE_NAME, FILE_MODE) as VARIABLE_NAME_FOR_FILE_OBJECT
with open("numbers.txt", "r") as f:
    for line in f:
        # convert the string to an int
        # because file contents are always strings by default
        number = int(line)
        nums.append(number)
print(min(nums))

# # write a program that allows a user to create
# # a guest list for a party
# # then saves the names of the invited guests
# # to a file
guest_list = []
name = input("Enter a name to invite (or 'quit' to quit): ")
while name != "quit":
    # add the name to our guest list
    guest_list.append(name)
    name = input("Enter a name to invite (or 'quit' to quit): ")
print(guest_list)

# # open a connection to a file called "guests.txt"
with open("guests.txt","a") as f:
    for name in guest_list:
      # add newline character so each name is on its own line
      f.write(name + "\n") 

# read in the content from the csv
# and create a dictionary for each team
# with their wins and losses
teams = {}
with open("data.csv","r") as data:
    counter = 0
    for line in data:
      if counter != 0: # skips column name row
        # take the whole row and split on each column
        # to get a list of all data
        # strip out the hidden newline characters
        team, wins, losses = line.strip("\n").split(",")
        # team_name = data_as_list[0]
        # wins = data_as_list[1]
        # add the data to our dictionary
        teams[team] = {
           "wins": wins,
           "losses": losses
        }
      counter += 1

print(teams)
team_name = input("Enter a team to look up: ")
if team_name in teams:
   print(f"{team_name} has won {teams[team_name]['wins']} games.")
else:
   print("We do not have any stats for that team.")

      