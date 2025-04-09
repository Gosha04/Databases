from Driver import Driver
from Rider import Rider

class User:
    def __init__(self, new: bool):
        self.new = new
    
    def getUserType(self):
        return self.userType

    def makeNewAccount(self, name):
        if self.new == True:
            self.userType = input("What type of user are you? A (d)river or (r)ider?")
            if self.userType not in ('r', 'd'):
                raise ValueError("Invalid input. Please 'r' or 'd'.")
            self.name = name

    def accessAccount(self):
        if self.new == True:
            if self.userType == "Driver":
                Driver(None)
            else:
                Rider(None)
        else:
            self.userID = input("Please provide you corresponding ID: ")
            if self.userType == "Driver":
                Driver(self.userID)
            else:
                Rider(self.userID)