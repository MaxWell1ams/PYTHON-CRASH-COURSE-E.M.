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