from car_module import Car

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
        self.battery = Battery() 