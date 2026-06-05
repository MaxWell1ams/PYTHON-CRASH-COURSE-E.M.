from pathlib import Path
import json
path = Path('chapter 10 folder/json_db.json')
print("Welcome to JSONDB")
contents = path.read_text()
logins = json.loads(contents)
active = True
while active:
    login = input("put your login:\n")
    if login in logins:
        print(f"Welcome to the system {login.upper()}")
    else:
        name = input("Dont see you in the system\nLet me know your name:\n")
        last_name = input("\nLet me know your last name:\n")
        login = f"{name}{last_name}"
        logins.append(login)
        contents = json.dumps(logins)
        with open(path, 'w') as f:
            f.write(f"{contents}\n")
    next = input("next?:\n")
    if next == 'no':
        active = False