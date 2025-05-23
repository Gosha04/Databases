import mysql.connector
import os
from dotenv import load_dotenv
from User import User
from Driver import Driver
from Rider import Rider

load_dotenv()
#connect DB
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
#prompts users 
while True:
    print("Hello! Welcome to Rideshare 408, where we hope to fulfill all your transportation needs.")
    userNewCheck = input("To start, could you tell us if you are a new user?\n y/n ").strip().lower()

    if userNewCheck not in ('y', 'n'):
        print("Invalid input. Please enter 'y' or 'n'.")
        continue  
    else:
        if userNewCheck == 'y':
            userNewCheck = True
            userName = input("\nWelcome new user!\nWhat's your name?")
            introMenuUser = User(userNewCheck)
            introMenuUser.makeNewAccount(userName)
        else:
            userNewCheck = False
            print("\nWelcome existing user!")
            #prompts user for type, Rider or Driver
            while True:
                userType = input("What type of user are you? A (d)river or (r)ider?").strip().lower()
                if userType not in ('r', 'd'):
                   print("Invalid input. Please 'r' or 'd'.")
                   continue
                break
            if userType == 'r':
                userType = 'rider'
            else:
                userType = 'driver'

            introMenuUser = User(userNewCheck, userType)

    currUser = introMenuUser.accessAccount()

    # Driver Menu 
    
    if isinstance(currUser, Driver):
        while True:
            #options printed for driver 
            print("Welcome to the Driver Menu!")
            userInput = int(input("""
                        Menu Options:
                        1) View Rating
                        2) Set your Driving Status
                        3) View Rides
                        4) Return to main menu
                        5) Quit Application """))
            #calls for inputted numbers 
            if userInput == 1:
                currUser.viewRating()
            elif userInput == 2:
                currUser.setStatus()
            elif userInput == 3:
                currUser.viewRides()
            elif userInput == 4:
                break  
            elif userInput == 5:
                should_exit = True
                break  
            else:
                print("\nPlease use valid options")
                continue

            userReady = input("Are you ready to continue?")

    # Rider menu
    
    elif isinstance(currUser, Rider):
        while True:
            #rider info 
            print("Welcome to the Rider Menu!")
            userInput = int(input("""
                        Menu Options:
                        1) Find a Driver
                        2) Verify and Rate your Last Ride
                        3) View Rides
                        4) Return to main menu
                        5) Quit Application """))
            #calls for inputted numbers 
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
                should_exit = True
                break  
            else:
                print("\nPlease use valid options")
                continue

            userReady = input("Ready to continue? (y/n): ").strip().lower()
#exit message
    if should_exit:
        print("Goodbye!")
        break 
