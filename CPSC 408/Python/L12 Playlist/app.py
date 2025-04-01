#imports
from helper import helper
from db_operations import db_operations

#global variable
db_ops = db_operations("playlist.db")

#function
def startScreen():
    print("Welcome to your playlist")
    #db_ops.create_songs_table()
    #db_ops.populate_songs_table("songs.csv")

def options():
    print('''Select from the following menu options:
    1. Find songs by artist
    2. Find songs by genre
    3. Find songs by feature
    4. Exit
    ''')
    return helper.get_choice([1,2,3,4])

#get a list of all artists, let the user pick one, and print out all song names by that artist
def searchByArtist():
    #get a list of all artists
    query = '''
    SELECT DISTINCT Artist
    FROM songs;
    '''
    print("Artists in playlist")
    artists = db_ops.single_attribute(query)

    #let user pick one
    choices = {}
    for i in range(len(artists)):
        choices[i] = artists[i]
        print(i, artists[i])
    index = helper.get_choice(choices.keys())

    #user can ask to see 1, 5, or all songs
    #TODO Change to all numbers
    print("How many songs do you want returned for", choices[index]+"?")
    print("Enter 1, 5, or 0 for all options")
    num = helper.get_choice([1,5,0])

    #show all results
    query = '''
    SELECT DISTINCT Name
    FROM songs 
    WHERE Artist = :artist 
    ORDER BY RANDOM()
    '''
    dictionary = {"artist":choices[index]}
    if num != 0:
        query += "LIMIT :lim"
        dictionary["lim"] = num
    results = db_ops.single_attribute_params(query, dictionary)
    helper.pretty_print(results)

def searchByFeature():
    features = ['Danceability', 'Liveness', 'Loudness', 'Energy', 'Acousticness']

    #print and have them pick one
    choices = {}
    for i in range(len(features)):
        choices[i] = features[i]
        print(1, features[i])
    index = helper.get_choice(choices.keys())

    #user can ask to see 1, 5, or all songs
    #TODO Change to all numbers
    print("How many songs do you want returned for", choices[index]+"?")
    print("Enter 1, 5, or 0 for all options")
    num = helper.get_choice([1,5,0])

    #print our results
    query = "SELECT DISTINCT Name FROM SONGS ORDER BY " + choices[index] + " DESC"
    dictionary = {}
    if num != 0:
        query += "LIMIT :lim"
        dictionary["lim"] = num
    
    results = db_ops.single_attribute_params(query, dictionary)
    helper.pretty_print(results)



def searchByGenre():
     #get a list of all artists
    query = '''
    SELECT DISTINCT Genre
    FROM songs;
    '''
    print("Genres in playlist")
    genres = db_ops.single_attribute(query)

    #let user pick one
    choices = {}
    for i in range(len(genres)):
        choices[i] = genres[i]
        print(i, genres[i])
    index = helper.get_choice(choices.keys())

    #user can ask to see 1, 5, or all songs
    #TODO Change to all numbers
    print("How many songs do you want returned for", choices[index]+"?")
    print("Enter 1, 5, or 0 for all options")
    num = helper.get_choice([1,5,0])

    #show all results
    query = '''
    SELECT DISTINCT Name
    FROM songs 
    WHERE Genre = :genre 
    ORDER BY RANDOM()
    '''
    dictionary = {"genre":choices[index]}
    if num != 0:
        query += "LIMIT :lim"
        dictionary["lim"] = num
    results = db_ops.single_attribute_params(query, dictionary)
    helper.pretty_print(results)

#main method
startScreen()
while True:
    user_choice = options()
    match user_choice:
        case 1:
            searchByArtist()
        case 2: 
            searchByGenre()
        case 3:
            searchByFeature()
        case 4:
            print("Goodbye!")
            break

db_ops.destructor()

