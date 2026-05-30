#OOP finally
#creating the watchdog class
class Watchdog:
    """my first class, it's will be watchdog(anti corruption person)"""
    def __init__(self, name, age):      #function in the class is the method(everything the same about functions
        #also I need spase between def and init and for init on each side 
        #I need 2 underscores _ +_ +init+_+_ 
        #__init__
        """init probably about initializing following keys""" #its called attributes (not keys)
        self.name = name 
        self.age = age

    def investigate(self):
        """simulating investigation"""
        print(f"{self.name} is now investigating crime")
    def oversight(self):
        """simulating oversight"""
        print(f"{self.name} is oversiting!")
active = True
while active:
    y_name = input("your name: ")
    y_age = input("your age: ")
    h_name = input("his name: ")
    h_age = input("his age: ")

    my_wd = Watchdog(y_name,y_age)
    my_wd.investigate()
    my_wd.oversight()
    print(f"My watchdog name is {my_wd.name}")
    print(f"He is {my_wd.age} y o")

    h_wd = Watchdog(h_name,h_age)
    h_wd.investigate()
    h_wd.oversight()
    print(f"His watchdog name is {h_wd.name}")
    print(f"He is {h_wd.age} y o")

    next = input("next? yes/no:\n")
    if next == 'no':
        active = False     #so the sense of calss for now is that I can easilly add new instance
        # which will do what I defined in class

#practicing
class Restaurant:
    """defines restaurant"""
    def __init__ (self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant called {self.name} and it is has {self.cuisine} cuisine")
    def open_restaurant(self):
        print(f"The {self.name} is open")

rest1 = Restaurant('China', 'Chinese')
rest1.describe_restaurant()

rest2 = Restaurant('Ukrainer', 'Ukrainian')
rest2.describe_restaurant()

rest3 = Restaurant('Mexicana', 'Mexico')
rest3.describe_restaurant()

class User:
    """defines user"""
    def __init__ (self,first_name, last_name, login, password):
        self.first = first_name
        self.last = last_name
        self.log = login
        self.passw = password
        self.login_attempts = 0
    def read_logins(self):
        print(f"user has {self.login_attempts} login attempts")
    def increase_login_attempts(self):
        self.login_attempts += 1
    def reset_logins(self):
        self.login_attempts = 0
    def describe_user(self):
        print(f"User info:\nFirst name: {self.first}\nLast name: {self.last}\nUser login: {self.log}\nUser password: {self.passw}")
    def greeting(self):
        print(f"Hey {self.first}")

new_user = User('Max','Well','maxwell','lawelmax')
new_user.greeting()
new_user.describe_user()
new_user.increase_login_attempts()
new_user.read_logins()
new_user.increase_login_attempts()
new_user.increase_login_attempts()
new_user.read_logins()
new_user.reset_logins()
new_user.read_logins()

#here is good example of car class
class Car:
    """representing car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_read = 0
    def read_odometer(self):
        print(f"This car has {self.odometer_read} kilometers on it")
    def update_odometer(self,km):
        if km >= self.odometer_read:
            self.odometer_read = km
        else:
            print("YO MAN WTF YOU CANT ROLL BACK THAT THING DAWG")
    def increase_odometer(self, km):
        self.odometer_read += km
    def get_descripiton(self):
        long_name = f"{self.year},{self.make},{self.model}"
        return long_name.upper()
my_new_car = Car('corvette','gt3','2026')
print(my_new_car.get_descripiton())
my_new_car.odometer_read = 23
my_new_car.update_odometer(13)
my_new_car.read_odometer()
my_new_car.increase_odometer(100)
my_new_car.read_odometer()

class Battery: #practicing instances as attribute - so I will have set of data as class
    #it called composition
    #I define battery in this class
    def __init__ (self,battery_size = 40):
        self.battery_size = battery_size
    def battery_info(self):
        print(f"This car has a {self.battery_size}--kWh battery capacity")

class EV(Car):   #there is example of child class creation - so I need class name and main class name in the ()
    """EV is child class of Car class"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)  #the super() function which allows me use methods from parent class 
        #calling init method from Car class
        #and basically super() goes from parent class as Superclass and child class as Subclass
        self.battery = Battery()  #here I adding class as attribute to this EV class
my_leaf = EV('nissan','leaf','2024')
print(my_leaf.get_descripiton())
my_leaf.battery.battery_info() # and here I call ev class attribute and atribute which contains in battery class

### exploring Python standart library
from random import randint
randint(1,10) #provides random number from 1 to 10 or whatever I choose

from random import choice  #this one returns random element from list or tuple
players = ['charles','maxc','wiz','emmy']
first = choice(players)
first