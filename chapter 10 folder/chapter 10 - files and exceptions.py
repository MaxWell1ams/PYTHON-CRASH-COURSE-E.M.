from pathlib import Path 
#so I imported module from py library which
#responsible for manipulations with files
path = Path('chapter 10 folder/txtfile.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

## replace command can replace words in strings 
message = "dogs is not cats"
message.replace('dog','cat')

## now learning how to write to a file
from pathlib import Path 
content = "Python becoming my first programming language\n"
content += "I'm interested in C++\n"
content += "I know that I need also learn JS\n"
path = Path('chapter 10 folder/txtfile_write.txt')
path.write_text(content) 
#also I discovered that write_text - erasing what file had and overwrites data

#at least I can do program which will store(but overwrite) and read data in a file
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
    if password in lines:
        print("welcome back")
    else:
        print("oh you new one bro")
        path.write_text(f"{password}\n") #its cant write login,password in one run
        #so I can use only 1 value and its will be pass 
        # cuz next value will overwrite it so will use pass
    quit = input("wanna quit or relogin?(quit/relogin)")
    if quit == 'quit':
        active = False

### Exeptions - so its basically try, except blocks to avoid errors