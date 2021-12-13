# toggle_button
#  
# Catbox module for a toggleable button.
# Hardware consists of some sort of arcade cabinet button with sparse 
# documentation.
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

from time import sleep

import RPi.GPIO as gpio
from modules.base_module import BaseModule


class ToggleButtonModule(BaseModule):
    """
    """
    def __init__(self) -> None:
        super().__init__()
        self.pir = 7
        self.button_on = False
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.pir, gpio.IN)

    def register(self, emitter) -> None:
        super().register(emitter)

    def launch(self) -> None:
        """
        """
        super().launch()
        sleep(5)
        gpio.add_event_detect(7,gpio.FALLING, callback=self._toggle_button)
        while True:
            sleep(10)

    def _toggle_button(self, channel):
        if self.button_on:
            self.emitter.emit(self.codes['button_off'])
        else:
            self.emitter.emit(self.codes['button_on'])
        self.button_on = not self.button_on