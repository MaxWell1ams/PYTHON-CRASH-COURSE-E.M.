class DriverProfile:
    """Describes simracer-driver profile"""
    def __init__ (self,name, primary_game, wheel_hardware):
        self.name = name
        self.game = primary_game
        self.wheel = wheel_hardware

    def record_lap_time(self, track, lap_time):
        """Stores these lap times in a dictionary attribute"""
        self.lap_time = lap_time
        self.track = track