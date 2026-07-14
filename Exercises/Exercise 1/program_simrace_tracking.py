from pathlib import Path
from module_driver_profile import DriverProfile
from module_F1_Driver import F1Driver
import json
path = Path('PYTHON-CRASH-COURSE-E.M./Exercises/Exercise 1/telemetry_db.json')
print("Welcome to SimRace Tracking Telemetry DB\n")
active = True
while active:
    contents = path.read_text()
    logins = json.loads(contents) 
    login = input("Let me know your name:\n")
    if login in logins:
        print(f"Welcome to the SimRace Tracking Telemetry {login.upper()}\n")
        #YOUR DATA
        print("Let me know for the record what trak you drove today and what your lap time in seconds?:\nPut 'q' to quit")
        track = input("Track name:\n")
        lap_time = input("Lap time in seconds:\n")
        db_active = True #flagging
        while db_active:
            lap_time = input("What is your lap time?")  #prept inputs
            track = input("What is name of the track?")
            my_driver.record_lap_time(track, lap_time) #storing into db data [defined my key to which I will assign values =]
            print(f"Data we received so far: {my_driver.record_lap_time(track, lap_time)}") #checking is it works
            repeat = input("Would you like to let more data (yes/no)")
            if repeat == 'no':
                db_active = False  #stoping the loop
                print("|||||RESULT|||||")
                for name, lap in my_driver.record_lap_time(track, lap_time): # I missed this step trying to make trio nam3,ag3,prog_lang instead of pair
                    print(f"track: {name}:\ntime: {lap[0]}")
    else:
        name = input("I dont see your data\nLet me know your name:\n")
        primary_game = input("Let me know your primary game:\n")
        wheel_hardware = input("What wheel hardware you use?(moza, logitech, fnatec..)\n")
        my_driver = F1Driver(name, primary_game, wheel_hardware)
        if primary_game.lower() == "f1":
            print(f"your capacity of ers = {my_driver.ers_lvl}")
        login = f"{name}{primary_game}{wheel_hardware}"
        print(f"Your login is:\n{name, primary_game, wheel_hardware}")
        logins.append(login) 
        contents = json.dumps(logins)
        with open(path, 'w') as f:
            f.write(f"{contents}\n")
    user_choice = input("Press 'q' to quit or any key to continue: ")
    if user_choice == 'q':
        active = False



        