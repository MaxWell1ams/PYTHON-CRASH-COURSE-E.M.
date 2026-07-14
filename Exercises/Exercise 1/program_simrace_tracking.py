from pathlib import Path
from module_driver_profile import DriverProfile
from module_F1_Driver import F1Driver
import json
path = Path('PYTHON-CRASH-COURSE-E.M./Exercises/Exercise 1/telemetry_db.json')
print("Welcome to SimRace Tracking Telemetry DB\n")
contents = path.read_text()
logins = json.loads(contents) 
active = True
while active:
    login = input("Let me know your name:\n")
    if login in logins:
        print(f"Welcome to the SimRace Tracking Telemetry {login.upper()}\n")
        #YOUR DATA
        print("Let me know for the record what trak you drove today and what your lap time in seconds?:\nPut 'q' to quit")
        track = input("Track name:\n")
        lap_time = input("Lap time in seconds:\n")
        print(f"Your primary game is {primary_game}, hardware {wheel_hardware}, track time {track}, lap time {lap_time}")
    else:
        name = input("I dont see your data\nLet me know your name:\n")
        primary_game = input("Let me know your primary game:\n")
        wheel_hardware = input("What wheel hardware you use?(moza, logitech, fnatec..)\n")
        login = f"{name}{primary_game}{wheel_hardware}"
        print(f"Your login is:\n{name}{primary_game}{wheel_hardware}")
        logins.append(login) 
        contents = json.dumps(logins)
        with open(path, 'w') as f:
            f.write(f"{contents}\n")
    if input == 'q':
        active = False



        