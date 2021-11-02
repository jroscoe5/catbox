# base_module.py
#
# Interface for all Catbox modules.
#
# authors:
#   Jonathon Roscoe / @jrosoce5
#

from abc import ABC, abstractmethod

class BaseModule(ABC):
    """
    Interface for all Catbox modules.
    """
    @abstractmethod
    def __init__(self, emitter, state_manager) -> None:
        pass
    
    @abstractmethod
    def load(self) -> bool:
        pass

    @abstractmethod
    def unload(self) -> bool:
        pass
