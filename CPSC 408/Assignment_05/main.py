import mysql.connector
import os
from dotenv import load_dotenv
from Driver import Driver

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

newDriver = Driver(1) 

# mycursor.execute("""
#        CREATE TABLE rides (
#             rideID INT NOT NULL PRIMARY KEY,
#             riderID INT REFERENCES rider(riderID),
#             driverID INT REFERENCES driver(driverID),
#             startSpot VARCHAR(40),
#             endSpot VARCHAR(40),
#             Completed TINYINT(1)
#         );""")

# mycursor.execute("""
#                 ALTER TABLE rider
#                 ADD CONSTRAINT lastrideID FOREIGN KEY (lastrideID) REFERENCES rides(rideID);
#                  """)



