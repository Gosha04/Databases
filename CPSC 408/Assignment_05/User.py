from Driver import Driver
from Rider import Rider

class User:
    def __init__(self, new: bool):
        self.new = new

    def setUserType(self, userType):
        self.userType = userType
    
    def getUserType(self):
        return self.userType

    def makeNewAccount(self, name):
        if self.new == True:
            self.setUserType(self, input("What type of user are you?"))
            self.name = name
        else: 
            print("User already exists.")

    def accessAccount(self):
        if self.userType == "Driver":
            Driver(None) 