from module_driver_profile import DriverProfile
class F1Driver(DriverProfile):
    def __init__ (self, ers, name, primary_game, wheel_hardware):
        """ERS mode data"""
        super().__init__(name,primary_game,wheel_hardware)
        self.ers = 400
    def ers(self, capacity):
        """capacity of ERS"""
        self.capacity = capacity
        print(f"ERS capacity of your F1 car {self.ers}kw")

    def ers_update (self, kw):
        """Update ERS mode data"""
        if kw >= self.capacity:
            self.ers = kw
        else:
            print("FIA might ban your ERS (out of regulations)")
    def increase_ers(self, kw):
        self.ers += kw

    def decrease_ers(self, kw):
        self.ers -= kw