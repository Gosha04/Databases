import mysql.connector
import os
from dotenv import load_dotenv
from User import User
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

# Main App Framework
should_exit = False 
while True:
    print("Hello! Welcome to Rideshare 408, where we hope to fulfill all you transportation needs")
    userNewCheck = input("To start, could you tell us if you are a new or existing user?\n y/n ").strip.lower
    if userNewCheck not in ('y', 'n'):
        raise ValueError("Invalid input. Please enter 'y' or 'n'.")
    else:
        if userNewCheck == 'y':
            userNewCheck = True
            print("\nWelcome new user!")
            introMenuUser = User(userNewCheck)

            introMenuUser.makeNewAccount()
        else:
            userNewCheck = False
            print("\nWelcome existing user!")
            introMenuUser = User(userNewCheck)

    currUser = introMenuUser.accessAccount()

    if isinstance(currUser, Driver):
        while True:
            print("Welcome to the Driver Menu!")
            userInput = input("""
                        Menu Options:
                        1) View Rating
                        2) Set your Driving Status
                        3) View Rides
                        4) Return to main menu
                        5) Quit Application """)
            if userInput not in (1,5):
                raise ValueError("Invalid input. Please enter a number 1-5.")
            
            if userInput == 1:
                currUser.viewRating()
            elif userInput == 2:
                currUser.setStatus()
            elif userInput == 3:
                currUser.viewRides()
            elif userInput == 4:
                break
            elif userInput == 5: 
                should_exit = True # Might make sense to switch to exit lemme know
                break

            userReady = input("Are you ready to continue? \ny\n")
            if userReady not in ('y', 'n'):
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")
    else:
        while True:
            print("Welcome to the Rider Menu!")
            userInput = input("""
                        Menu Options:
                        1) Find a Driver
                        2) Verify and Rate your Last Ride
                        3) View Rides
                        4) Return to main menu
                        5) Quit Application """)
            
            if userInput not in (1,5):
                raise ValueError("Invalid input. Please enter a number 1-5.")
            
            if userInput == 1:
                currUser.inputLocations()
                currUser.getRide()
            elif userInput == 2:
                currUser.endDriveRateDriver()
            elif userInput == 3:
                currUser.viewRides()
            elif userInput == 4:
                break
            elif userInput == 5: 
                should_exit = True # Might make sense to switch to exit lemme know
                break

            userReady = input("Are you ready to continue? \ny\n")
            if userReady not in ('y', 'n'):
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")

    if should_exit == True:
        break













