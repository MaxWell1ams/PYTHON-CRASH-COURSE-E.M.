from car_module import Car
from ev_module import EV

my_new_car = Car('corvette','gt3','2026')
print(my_new_car.get_descripiton())
my_new_car.odometer_read = 23
my_new_car.update_odometer(13)
my_new_car.read_odometer()
my_new_car.increase_odometer(100)
my_new_car.read_odometer()

my_leaf = EV('nissan','leaf','2024')
print(my_leaf.get_descripiton())
my_leaf.battery.battery_info() 