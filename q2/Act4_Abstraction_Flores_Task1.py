from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def __init__(self, sensor_id, location, calibration_buffer):
        super().__init__(sensor_id, location)
        self.calibration_buffer = calibration_buffer 

    def get_reading(self):
        print(f"[{self.sensor_id} - {self.location}] Reading: 7.2 pH (Buffer: {self.calibration_buffer})")

class TempSensor(Sensor):
    def __init__(self, sensor_id, location):
        super().__init__(sensor_id, location)

    def get_reading(self):
        print(f"[{self.sensor_id} - {self.location}] Reading: 24.5°C")

print("--- Lab Inventory System ---")

ph_sensor = PHSensor("PH-01", "Tank A", "pH 7.0")
temp_sensor = TempSensor("TMP-04", "Incubator 2")

ph_sensor.get_reading()
temp_sensor.get_reading()

print("\n----------------------------")

