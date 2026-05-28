#OOP finally
#creating the watchdog class
class Watchdog:
    """my first class, it's will be watchdog(anti corruption person)"""
    def __init__(self, name, age):      #function in the class is the method(everything the same about functions
        #also I need spase between def and init and for init on each side 
        #I need 2 underscores _ +_ +init+_+_ 
        #__init__
        """init probably about initializing following keys"""
        self.name = name 
        self.age = age

    def investigate(self):
        """simulating investigation"""
        print(f"{self.name} is now investigating crime")
    def oversight(self):
        """simulating oversight"""
        print(f"{self.name} is oversiting!")

my_wd = Watchdog('Max','22')
print(f"My watchdog name is {my_wd.name}")
print(f"He is {my_wd.age} y o")