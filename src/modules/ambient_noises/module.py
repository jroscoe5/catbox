# ambient_noises
#  
# Catbox module for playing ambient animal noises. 
# Currently supports mp3 files.
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

from random import choice, randrange
from time import sleep

from modules.base_module import BaseModule
from playsound import playsound

from .data import noises_list


class AmbientNoisesModule(BaseModule):
    """
    Plays ambient animal noises at random intervals.
    """
    def __init__(self) -> None:
        super().__init__()

    def register(self, emitter) -> None:
        super().register(emitter)

    def launch(self) -> None:
        """
        Plays a random audio file every 1 to 3 minutes.
        """
        super().launch()
        while True:
            sleep(randrange(60, 180))
            sound = choice(noises_list)
            playsound(sound, block=False)
            self.emitter.emit(self.codes['play_ambient'], filename=sound)
