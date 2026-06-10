#first function
#basically from 1st paragraph function for me is block of code
#which I can store in separate file to call in code or programm (like AI calls tool)

def greeting():  #def - defining a function making smth() the name of a function
    "Greeting" #body of the function starts after :
    #"greeting " - just a comment which tells what function does
    print("Hello") #actual work which function will do
greeting() #calling function

#trying use input with function, addign parameter and adding argument
def hello(user):  #parameter in ()
    """greeting with formating"""
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

#practicing using functions pos and key args and input
def order_tshirt(color, size, text, comment=None):  #I left comment='' - its will be optional argument
    #so None is empty value I can use instead of '' - so if none = false
    #and if I will input smth to comments its wil be = True
    if comment:  #I also tried if comment != '' also works
        print(f"Your order:\n {color} t-shirt\n with size: {size}\n and text: {text}\nand comment:{comment}")
    else:
        print(f"Your order:\n {color} t-shirt\n with size: {size}\n and text: {text}")
order_active = True
while order_active:
        color = input("What's your preferd color?:\n  ")
        size = input("What's your prefered size of t-shirt?:\n  ")
        text = input ("What's your wanted text to be printed on t-shirt?:\n  ")
        comment = input("Drop your comment below:\n")
        order_tshirt(color, size, text, comment)
        next_order = input("Do you want order one more? (yes/no):\n ")
        if next_order == 'no':
            print("Bye, looking forward for your next visit!")
            order_active = False

#RETURN VALUES - example
def t_shirt(sizee, colorr):
    #full_tshirt = f"{sizee} {colorr}" # in the same way I can return list or dictionary
    full_tshirt = {'size':sizee, 'color':colorr}
    return full_tshirt
orderrr = t_shirt('xl','white')
print(orderrr)

#practicing using lists and functions
messages = ['sup','yo','hi','oi']
sent_messagess = []
def show_messages(messages):
    for message in messages:
        print(f"your message: {message}")
show_messages(messages)
while messages:
    current_messages = messages.pop() # to prevent list from modifying 1st list I can use just append
    # without pop or function_name(list_name[:]) to copy list
    sent_messagess.append(current_messages)
    
print(messages)
print(sent_messagess)

# Arbitrary Argument - it's when I have asteriks before parameter name
# for example def borsh(*toppings) - when I hav it input I add to this function
# will be written to list topping and for example I can call this list and
# list willl contain what I inputed

def borsh(volume, *toppings): #if I will add regular parameter for regular argument
    # the arbitrary pararameter should be placed last like def sss(sdds, sdds, *dssdd)
    # so it's for LISTS - arbitrary with 1 asteriks
    print(f"Making a {volume} borsh with: ")
    for topping in toppings:
        print(topping)
def client_profile(first, last, **user_info):  #kwargs (for dictionaries)
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
order_active = True
while order_active:
    profile = input("What's your first and last name?:\n")
    user_profile = client_profile(profile)
    ingradients = input("Put your ingradient:\n")
    volume = input("What borsh volume you like?(S/M/L/XL):\n")
    borsh(volume, ingradients)
    print(f"Order for {user_profile} will be soon")
    next_order = input("Do you want order one more? (yes/no):\n ")
    if next_order == 'no':
        print("Bye, looking forward for your next visit!")
        order_active = False
# for dictionaries I can use double asteriks
# def ss(sdsd, sdds, **dsdsd)
# also usually people use args* and **kwargs as nameplates
#but after playing with import version this one above start braking with same reason imported did

#### MODULES and IMPORT
#so I created separate files with funbctions - so called modules
# now I can import em and that it
import module_borsh
import module_client_profile
#but I can create 1 file with all modules and import em in another way
from modules import borsh, client_profile #and in this case seems like I dont need to put dot
#before function dependent argument
#AND I can also utilise asteriks to call all the functions from module
from modules import *
order_active = True
while order_active:
    profile = input("What's your first and last name?:\n").split() #utilised split to have 2 values when writing input
    user_profile = client_profile(*profile) #so I called it to feed 1 and last name cuz without * it would not work
    #and when I use import program behave differently - I need do additional logic
    ingradients = input("Put your ingradient:\n")
    volume = input("What borsh volume you like?(S/M/L/XL):\n")
    borsh(volume, ingradients)
    print(f"Order for {user_profile} will be soon")
    next_order = input("Do you want order one more? (yes/no):\n ")
    if next_order == 'no':
        print("Bye, looking forward for your next visit!")
        order_active = False
### !!!!!!!!!!!!!NEEEEEEEED TO PRACTICE MORE!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# I can use aliases to import function and rename it if needed to not mistake my program
from modules import borsh as bh
bh('xl','garlick')

#and if I import just module I can also short it
import module_borsh as mb
mb.borsh
#AND I can also utilise asteriks to call all the functions from module
from modules import *