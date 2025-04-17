import mysql.connector
import os
from dotenv import load_dotenv
from Rides import Rides

load_dotenv()
#connect to database 
mydb = mysql.connector.connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USERNAME'),
    password = os.getenv('MYSQL_PASSWORD'),
    auth_plugin = 'mysql_native_password'
    )
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("USE rideShare")

class Rider:
    #creates rider object
    def __init__(self, riderID, name):
        self.name = name
        #prevents duplicate IDs 
        if riderID is not None:
            self.riderID = riderID
        else:
            mycursor.execute("SELECT MAX(riderID) FROM rider")
            result = mycursor.fetchone()
            max_id = result[0] if result[0] is not None else -1 # Just in case, shouldn't need that last bit
            self.riderID = max_id + 1
            #inserts rider into table
            mycursor.execute("INSERT INTO driver (riderID, Name) VALUES (%s, %s)", (self.riderID, self.name))
            mydb.commit()
            print(f"Congrats new user, your ID is: {self.riderID}.\nDon't worry about a password, our network and data security is magical. Literally.")

    #function to get locations of pick up and drop off
    def inputLocations(self):
        self.startSpot = input("Please provide your current location: ")
        self.endSpot = input("Please provide your destination: ")

   #clears locations from rider 
    def clearLocations(self):
        self.startSpot = None
        self.endSpot = None
    #Getter for the ride of the rider
    def getRide(self):
        mycursor.execute("SELECT MAX(rideID) FROM ride")
        result = mycursor.fetchone()
        maxRide = result[0] if result[0] is not None else 0 # Just in case, shouldn't need that last bit
        rideID = maxRide + 1

        mycursor.execute("SELECT driverID FROM driver ORDER BY RAND() LIMIT 1;")
        driverResult = mycursor.fetchone()
        driverID = driverResult[0]
        print("Here is your ride info: \n" + Rides(rideID, self.riderID, driverID, self.startSpot, self.endSpot, completed= False))
    #prints rides of rider 
    def viewRides(self):
        mycursor.execute("SELECT * FROM rides WHERE riderID = %s", (self.riderID,))
        rides = mycursor.fetchall()
        for ride in rides:
            print(ride)
            
    #prompts a rating to add to the driver after 
    def endDriveRateDriver(self):
        print(mycursor.execute("SELECT * FROM rides WHERE riderID = %s ORDER BY rideID DESC LIMIT 1", (self.riderID,)))
        rideCheck = input("Is all the information presented true? \n y/n" )

        #prevents incorrect input 
        while True:
            if rideCheck not in ('y', 'n'):
                print("Invalid input. Please enter 'y' or 'n'")
                continue
            break

        #prompts correct ID
        if rideCheck == 'n':
            newRideID = input("We're sorry. Could you please provide us a correct ID: ")
            lastRide = newRideID
        else:
            result = mycursor.fetchone()
            lastRide = result[0] if result[0] is not None else 0

        #prompts user ot enter rating for driver
        while True:
            self.driveRating = input("How was your drive? Rate 1-5")
            if self.driveRating not in (1,2,3,4,5):
                print("Invalid Input. Please use a number 1 through 5")
                continue
            break

        #commits changes to DB
        mycursor.execute("""
                        UPDATE rides
                        SET driveRating = %s, Completed = 1
                        WHERE rideID = %s
                        """, (self.driveRating, lastRide))
        mydb.commit()

    
        
