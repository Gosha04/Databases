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

class Driver:
    def __init__(self, driverID):
        if driverID is not None:
            self.driverID = driverID
        else:
            mycursor.execute("SELECT MAX(driverID) FROM driver")
            result = mycursor.fetchone()
            max_id = result[0] if result[0] is not None else 0 # Just in case, shouldn't need that last bit
            self.driverID = max_id + 1

    def viewRating(self):
        mycursor.execute("SELECT Rating FROM driver WHERE driverID = %i", (self.driverID,))
        result = mycursor.fetchone()
        rating = result[0] if result[0] is not None else 0 # Same as above we can remove this later I think
        return rating
    
    def setStatus(self):
        self.status = input("Do you plan on driving? (y/n): ").strip().lower()
        if self.status not in ('y', 'n'):
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        
        if self.status == 'y':
            mycursor.execute("UPDATE TABLE driver SET Rating = True WHERE driverID = %i", (self.driverID,))
        else: 
            mycursor.execute("UPDATE TABLE driver SET Rating = False WHERE driverID = %i", (self.driverID,))

        #TODO Implement viewRides(self) but this needs a Rides class
