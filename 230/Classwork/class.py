'''
Typically one class per file 
Followed by a short description

Song
This class represents a song on a music streaming platform
'''
import random
# class Song:
#     '''
#     Constructor
#     This is a method that creates an instance of our object
#     It gets run automatically by python when we create 
#     a Song object somewhere else in our code

#     all of the methods that are surrounded by double __
#     have some sort of expected functionality with python

#     self is a required parameter of every method in the class 
#     constructor also takes in other attributes
#     '''
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#         self.n_streams = 0

#     '''
#     String Method
#     This will tell python how to print out Song objects
#     '''
#     def __str__(self):
#         return f'{self.title} by {self.artist} \nNumber of Streams: {self.n_streams}'
    
#     def play(self):
#         self.n_streams += 1

# if __name__ == "__main__":
#     single_ladies = Song("Single Ladies", "Beyonce")
#     dsb = Song("Don't Stop Believing","Journey")

#     single_ladies.play()
#     print(single_ladies)
#     print(dsb)

class NFL:

    def __init__(self, name, conference, division):
        self.conference = conference
        self.division = division
        self.name = name
        self.fans = 0 
    def __str__(self):
        return f"{self.name} is a team in the {self.conference} and {self.division} \nIt currently has {self.fans} fans"
    
    def pop(self):
        if self.fans <= 0:
            self.fans = 0
            self.fans = self.fans + random.randint(1, 10000)
        else:
            self.fans = self.fans + random.randint(-1000, 5000)

if __name__ == "__main__":
    rams = NFL("Rams", "NFC", "West")
    rams.pop()
    print(rams)
    