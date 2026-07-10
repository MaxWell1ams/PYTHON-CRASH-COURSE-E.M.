Exercise 1: Sim Racing Telemetry Tracker
Concepts tested: OOP (Classes, Inheritance), Dictionaries, File I/O (JSON), Loops, Conditional Logic.

Build a program that tracks lap times and hardware setups for different racing simulators (like F1 24 or iRacing).
The Requirements:
Create a base class called DriverProfile with attributes for name, primary_game, and wheel_hardware (e.g., Moza, Logitech G923).

Create a method inside the class called record_lap_time(track, time_in_seconds) that stores these lap times in a dictionary attribute.

Create a child class called F1Driver that inherits from DriverProfile but adds a unique attribute for ers_deployment_mode and a method to update it.

Write a script that creates an instance of your driver, adds a few lap times using a for loop, and then saves the entire driver's profile (including their nested dictionary of lap times) to a JSON file called telemetry_db.json.

Finally, write a separate block of code that reads telemetry_db.json, parses the data, and prints out the track where the driver had their fastest (minimum) lap time.