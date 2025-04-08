import mysql.connector
import os
from dotenv import load_dotenv
from Rides import Rides

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

class Rider:
    def __init__(self, riderID):
        if riderID is not None:
            self.riderID = riderID
        else:
            mycursor.execute("SELECT MAX(riderID) FROM rider")
            result = mycursor.fetchone()
            max_id = result[0] if result[0] is not None else 0 # Just in case, shouldn't need that last bit
            self.riderID = max_id + 1

    def inputLocations(self):
        self.startSpot = input("Please provide your current location: ")
        self.endSpot = input("Please provide your destination: ")
        
    def clearLocations(self):
        self.startSpot = None
        self.endSpot = None

    def getRide(self):
        mycursor.execute("SELECT MAX(rideID) FROM ride")
        result = mycursor.fetchone()
        maxRide = result[0] if result[0] is not None else 0 # Just in case, shouldn't need that last bit
        rideID = maxRide + 1
        driverID = None
        Rides(rideID, self.riderID, driverID, self.startSpot, self.endSpot, completed= False)

    def viewRides(self):
        mycursor.execute("SELECT * FROM rides WHERE riderID = %s", (self.riderID,))

    def endDriveRateDriver(self):
        print(mycursor.execute("SELECT rideID FROM rides WHERE riderID = %s LIMIT 1 DESC", (self.riderID,)))
        rideCheck = input("Is all the information presented true? \n y/n" )

        if rideCheck not in ('y', 'n'):
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
    
        if rideCheck == 'n':
            newRideID = input("We're sorry. Could ыоу please provide us a correct ID: ")
            lastRide = newRideID
        else:
            result = mycursor.fetchone()
            lastRide = result[0] if result[0] is not None else 0

        self.driveRating = input("How was your drive? Rate 1-5")
        if self.driveRating not in (1,5):
            raise ValueError("Invalid input. Please enter a number 1-5.")
        
        mycursor.execute("""
                        UPDATE rides
                        SET driveRating = %s, Completed = 1
                        WHERE rideID = %s
                        """, (self.driveRating, lastRide))

    
        
