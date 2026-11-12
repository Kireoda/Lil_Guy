from gpiozero import MotionSensor, Button
from signal import pause

class LilGuySensors:
    def __init__(self):
        # PIR motion sensor
        self.motion_sensor = MotionSensor(17)

        # Touch sensors
        self.touch_sensor_1 = Button(22)
        self.touch_sensor_2 = Button(24)

        # Light sensor digital output
        self.light_sensor = Button(27)

        # Register sensor events
        self.motion_sensor.when_motion = self._motion_detected
        self.motion_sensor.when_no_motion = self._motion_stopped

        self.touch_sensor_1.when_pressed = self._touch_1
        self.touch_sensor_2.when_pressed = self._touch_2

        self.light_sensor.when_pressed = self._light_detected
        self.light_sensor.when_released = self._dark_detected

    def _motion_detected(self):
        print("MOVEMENT")

    def _motion_stopped(self):
        print("NO movement")

    def _touch_1(self):
        print("Touch sensor 1 TOUCHED")

    def _touch_2(self):
        print("Touch sensor 2 TOUCHED")

    def _light_detected(self):
        print("LIGHT")

    def _dark_detected(self):
        print("DARKNESS")

    def start(self):
        print("Sensors runningggg")
        pause()


if __name__ == "__main__":
    sensors = LilGuySensors()
    sensors.start()
