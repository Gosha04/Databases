import mysql.connector
import os
from dotenv import load_dotenv

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

class Rides:
    def __init__(self, rideID, riderID, driverID, startSpot, endSpot, completed, driveRating = None):
        self.rideID = rideID
        self.riderID = riderID
        self.driverID = driverID
        self.startSpot = startSpot
        self.endSpot = endSpot
        self.completed = completed
        self.driveRating = driveRating

        if driverID == None:
            driverID = input("Be the app for testing purposes and input the ID of a Driver that exists")

        mycursor.execute(""" UPDATE rides
                        SET rideID = %s, riderID = %s, driverID = %s,  startSpot = %s, endSpot = %s""",
                        (self.rideID, self.riderID, self.driverID, self.startSpot, self.endSpot))
        
    def __str__(self):
        return f"RideID: {self.rideID}, RiderID: {self.riderID}, DriverID: {self.driverID},
            From: {self.startSpot} → To: {self.endSpot}, Completed: {self.completed}"
