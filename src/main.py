from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

# Create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="moondalup", capacity=100, log_file=Path("moondalup.txt"))

# Write the car park configuration to a file called "moondalup_config.json"
car_park.write_config("moondalup_config.json")

# Reinitialize the car park object from the "moondalup_config.json" file
car_park = CarPark.from_config("moondalup_config.json")

# Create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)

# Create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)

# Create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

# Drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for _ in range(10):
    entry_sensor.detect_vehicle()

# Drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for _ in range(2):
    exit_sensor.detect_vehicle()

