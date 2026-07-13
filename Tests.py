from pathlib import Path
import json
path = Path('PYTHON-CRASH-COURSE-E.M./chapter 10 folder/json_db.json')
print("Welcome to JSONDB")
active = True
while active:
    contents = path.read_text()
    logins = json.loads(contents) #damn I was frustrated
# so if my json file will be empty loads() will not work so I needed to add []
# to the file to make my rogramm work
    login = input("put your login:\n")
    if login in logins:
        print(f"Welcome to the system {login.upper()}")
    else:
        name = input("Dont see you in the system\nLet me know your name:\n")
        last_name = input("\nLet me know your last name:\n")
        login = f"{name}{last_name}"
        print(f"Your login is {login}")
        logins.append(login) #here I using append cuz open(path, 'a') will add new list and
        # loads will not able to read it, so I adding new data in python and overwrite 
        # it already updated
        contents = json.dumps(logins)
        with open(path, 'w') as f:
            f.write(f"{contents}\n")
    next = input("next?:\n")
    if next == 'no':
        active = False