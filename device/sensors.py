
from gpiozero import MotionSensor, Button
from signal import pause


class LilGuySensors:
    def __init__(self):
        # PIR motion sensor
        self.motion_sensor = MotionSensor(17)

        # Touch sensors
        self.touch_sensor_1 = Button(22, pull_up=False, hold_time=1)
        self.touch_sensor_2 = Button(24, pull_up=False, hold_time=1)

        # Light sensor digital output
        self.light_sensor = Button(27, pull_up=False)

        # Track long touches
        self.long_touch_1 = False
        self.long_touch_2 = False

        # Register motion events
        self.motion_sensor.when_motion = self._motion_detected
        self.motion_sensor.when_no_motion = self._motion_stopped

        # Register touch events
        self.touch_sensor_1.when_pressed = self._touch_1_pressed
        self.touch_sensor_1.when_held = self._touch_1_held
        self.touch_sensor_1.when_released = self._touch_1_released

        self.touch_sensor_2.when_pressed = self._touch_2_pressed
        self.touch_sensor_2.when_held = self._touch_2_held
        self.touch_sensor_2.when_released = self._touch_2_released

        # Register light events
        self.light_sensor.when_pressed = self._dark_detected
        self.light_sensor.when_released = self._light_detected

    def _motion_detected(self):
        print("MOVEMENT")

    def _motion_stopped(self):
        print("NO movement")

    # Touch sensor 1
    def _touch_1_pressed(self):
        self.long_touch_1 = False

    def _touch_1_held(self):
        self.long_touch_1 = True

    def _touch_1_released(self):
        if self.long_touch_1:
            print("LONG TOUCH")
        else:
            print("SHORT TOUCH")

    # Touch sensor 2
    def _touch_2_pressed(self):
        self.long_touch_2 = False

    def _touch_2_held(self):
        self.long_touch_2 = True

    def _touch_2_released(self):
        if self.long_touch_2:
            print("LONG TOUCH")
        else:
            print("SHORT TOUCH")

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
