# motion_sensor
#  
# Catbox module for detecting motion.
# Works with an HC-SR501 Infrared PIR Motion Sensor attached to a Raspberry Pi.
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

from time import sleep

import RPi.GPIO as gpio
from modules.base_module import BaseModule


class MotionSensorModule(BaseModule):
    """
    Works with HC-SR501 Infrared PIR Motion Sensor on pin 26 to detect motion.
    """
    def __init__(self) -> None:
        super().__init__()
        self.pir = 26
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.pir, gpio.IN) 

    def register(self, emitter) -> None:
        super().register(emitter)

    def launch(self) -> None:
        """
        Starts listening to motion sensor. Once motion is detected, emits event
        and then sleeps for 1 minute before resuming listening.
        """
        super().launch()
        sleep(5)
        while True:
            if gpio.input(self.pir):
                self.emitter.emit(self.codes['motion_detected'])
                sleep(60)
            sleep(0.1)
