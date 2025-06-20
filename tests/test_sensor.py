import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Sensor Street", 2)
        self.entry_sensor = EntrySensor(id=1, is_active=True, car_park=self.car_park)
        self.exit_sensor = ExitSensor(id=2, is_active=True, car_park=self.car_park)

    def test_entry_sensor_detects_vehicle_and_adds_plate(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)

    def test_exit_sensor_detects_vehicle_and_removes_plate(self):
        self.entry_sensor.detect_vehicle()
        initial_plates = list(self.car_park.plates)
        self.assertEqual(len(initial_plates), 1)

        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.plates, [])


if __name__ == "__main__":
    unittest.main()

