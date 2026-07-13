from pathlib import Path
path = Path('PYTHON-CRASH-COURSE-E.M./chapter 10 folder/simple_db1.txt')
print("Hello\nProvide your login and password:")
active = True
while active:
    contents = path.read_text()
    lines = contents
    login = input("login:\n")
    password = input("password:\n")
    print("loggining....")
    if password.lower() in lines:
        print("welcome back")
    else:
        print("oh you new one bro")
        #path.write_text(f"{password}\n") --- #its cant write login,password in one run
        #so I can use only 1 value and its will be pass 
        # cuz next value will overwrite it so will use pass
        with open(path, 'a') as f: #I researched that I can utilise a - as append
            # w as write and r as read in format above
            f.write(f"{login}\n{password} \n")
    quit = input("wanna quit or relogin?(quit/relogin)")
    if quit == 'quit':
        active = False