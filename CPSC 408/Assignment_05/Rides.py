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
    def __init__(self, rideID, riderID, driverID, startSpot, endSpot, completed, driveRating):
        self.rideID = rideID
        self.riderID = riderID
        self.driverID = driverID
        self.startSpot = startSpot
        self.endSpot = endSpot
        self.completed = completed
        self.driveRating = driveRating

    def addLocationsDB (self):
        mycursor.execute(" UPDATE TABLE rider SET startSpot = %s, endSpot = %s ", (self.startSpot, self.endSpot))