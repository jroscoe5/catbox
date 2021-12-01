# motion_sensor
#  
# Catbox module for detecting motion.
# Works with an HC-SR501 Infrared PIR Motion Sensor attached to a Raspberry Pi.
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

from time import sleep

from modules.base_module import BaseModule


class MotionSensorModule(BaseModule):
    """
    """
    def __init__(self) -> None:
        super().__init__()

    def register(self, emitter) -> None:
        super().register(emitter)

    def launch(self) -> None:
        """
        """
        super().launch()
