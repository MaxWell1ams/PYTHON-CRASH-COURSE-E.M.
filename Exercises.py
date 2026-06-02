from pathlib import Path
path = Path('chapter 10 folder/simple_db1.txt')
contents = path.read_text()
lines = contents.splitlines()
print("Hello\nProvide your login and password:")
active = True
while active:
    login = input("login:\n")
    password = input("password:\n")
    print("loggining....")
    if login and password in lines:
        print("welcome back")
    else:
        print("oh you new one bro")
        path.write_text(login)
        path.write_text(password)
    quit = input("wanna quit or relogin?(quit/relogin)")
    if quit == 'quit':
        active = False