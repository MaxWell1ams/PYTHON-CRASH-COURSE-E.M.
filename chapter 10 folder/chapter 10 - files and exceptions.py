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
lines = contents
print("Hello\nProvide your login and password:")
active = True
while active:
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


### Exeptions - so its basically try, except blocks to avoid errors
try:
    print(5/0)
except ZeroDivisionError:
    print("I cann't divide by 0")

### divider with exceptions - very good sample of how to utilise it
while True:
    st_nuumber = input("first number: \n")
    if st_nuumber == 'q':
        break
    second_number = input("second number: \n")
    if second_number == 'q':
        break
    try: #here block where I trying answer but with exception
        #and the only code whih should go to try is one which likely
        #will cause error
        answer = int(st_nuumber) / int(second_number)
    except ZeroDivisionError:
        print("you are cringe!")
    except ValueError:  #trying additional except - works well
        print("you are super cringe!")
    else:
        print(answer)

#and so on for example for FileNotFoundError
from pathlib import Path
path = Path('sdds.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"yo I don't see {path}")

#in same way I use except I can use pass under it to not 
# show notification
except FileNotFoundError:
    pass


