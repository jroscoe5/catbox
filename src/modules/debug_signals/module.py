# debug_signals
#  
# Catbox module for emitting events while debugging and testing
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

from time import sleep

from modules.base_module import BaseModule


class DebugSignalsModule(BaseModule):
    """
    Emits events for debugging and testing
    """
    def __init__(self) -> None:
        super().__init__()

    def register(self, emitter) -> None:
        super().register(emitter)

    def launch(self) -> None:
        """
        Put signals and sleep delays here
        """
        super().launch()
        sleep(10)
        self.emitter.emit(self.codes['start_timed_tv'], 10 * 60)
        sleep(60)
        self.emitter.emit(self.codes['stop_tv'])
