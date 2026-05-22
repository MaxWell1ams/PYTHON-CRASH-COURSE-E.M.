#first function
#basically from 1st paragraph function for me is block of code
#which I can store in separate file to call in code or programm (like AI calls tool)

def greeting():  #def - defining a function making smth() the name of a function
    "Greeting" #body of the function starts after :
    #"greeting " - just a comment which tells what function does
    print("Hello") #actual work which function will do
greeting() #calling function

#trying use inut with function, addign parameter and adding argument
def hello(user):  #parameter in ()
    print(f"Hello {user.title()}")
online = True
while online:
    name = input("Whats your name?:\n")
    if name == 'quit':
        print("Cya")
        online = False
    else:
        hello(name) #argument positional
        hello(user = name) #argument keyword