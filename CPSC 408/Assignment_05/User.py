import mysql.connector
import os
from dotenv import load_dotenv
from Driver import Driver
from Rider import Rider

load_dotenv()

mydb = mysql.connector.connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USERNAME'),
    password = os.getenv('MYSQL_PASSWORD'),
    auth_plugin = 'mysql_native_password'
    )
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("USE rideShare")

class User:
    def __init__(self, new: bool, userType = None):
        self.new = new
        self.userType = userType
    
    def getUserType(self):
        return self.userType

    def makeNewAccount(self, name):
        if self.new:
            while True:
                self.userType = input("What type of user are you? A (d)river or (r)ider?").strip().lower()
                if self.userType not in ('r', 'd'):
                   print("Invalid input. Please 'r' or 'd'.")
                   continue
                self.name = name
                if self.userType == 'd':
                    self.userType = "driver"
                else:
                    self.userType = "rider"

                print(f"Account created for {self.name} as a {self.userType.capitalize()}.")
                break

    def accessAccount(self):
        if self.new:
            if self.userType == 'driver':
                return Driver(None, self.name)
            else:
                return Rider(None, self.name)
        else:
            self.userID = input("Please provide your corresponding ID: ")

            if self.userType == 'driver':
                mycursor.execute("SELECT Name FROM driver WHERE driverID = %s", (self.userID,))
                nameD = mycursor.fetchone()
                self.name = nameD[0]
                while True:
                    mycursor.execute("SELECT driverID FROM driver WHERE driverID = %s", (self.userID,))
                    result = mycursor.fetchone()  
                    if result: 
                        print(f"Driver with ID {self.userID} found.")
                        return Driver(self.userID, self.name) 
                    else:
                        print("No driver found with that ID. Please try again.")
                        print("Use a proper ID. If you are a new user, use 'None'")
            else:
                mycursor.execute("SELECT Name FROM driver WHERE driverID = %s", (self.userID,))
                nameR = mycursor.fetchone()
                self.name = nameR[0]

                mycursor.execute("SELECT riderID FROM rider WHERE riderID = %s", (self.userID,))
                result = mycursor.fetchone()  
                if result: 
                    print(f"Rider with ID {self.userID} found.")
                    return Rider(self.userID, self.name) 
                else:
                    print("No rider found with that ID. Please try again.")
                    print("Use a proper ID. If you are a new user, use 'None'")
