from modules.base_module import BaseModule
from playsound import playsound
from random import choice, randrange
from time import sleep
from .data import noises_list

class AmbientNoisesModule(BaseModule):
    """
    Plays ambient animal noises ever so often.
    """
    def __init__(self) -> None:
        super().__init__()

    def register(self, emitter) -> None:
        super().register(emitter)

    def launch(self) -> None:
        super().launch()
        while True:
            sleep(randrange(60, 180))
            playsound(choice(noises_list), block=False)
            self.emitter.emit(self.codes['play_ambient'])
