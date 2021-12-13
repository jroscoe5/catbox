# base_module.py
#
# Base class for all Catbox modules.
#
# authors:
#   Jonathon Roscoe / @jrosoce5
#

from pymitter import EventEmitter


class BaseModule():
    """
    Base class for all Catbox modules.
    """

    # Defines a dict of all events that modules may emit and listen for. Keys  
    # are the simple names of the events, values are the string that should
    # be emitted and listened for. If an event is only emitted by a specific 
    # module, use module_name.event_name as the key. Otherwise, use 
    # system.event_name. Comment the parameters that accompany each event as
    # well as a description of when it is emitted.
    codes = {
        'print': 'system.print', # (message:str) emitted to print a notification 
        'exception': 'system.exception', # (exception:Exception) emitted when an exception occurs
        'ready': 'system.ready', # (None) emitted after all modules are launched
        'stop': 'system.stop', # (None) emitted to when/if system shuts down or sleeps
        'play_ambient': 'ambient_noises.play_ambient', # (filename:str) emitted when ambient_noises plays a sound
        'start_tv': 'tv.start_tv', # (None) emitted when starting playing cat tv
        'stop_tv': 'tv.stop_tv', # (None) emitted when stopping cat tv
        'motion_detected': 'motion_sensor.motion_detected', # (None) emitted when motion sensor registers motion
        'button_on': 'toggle_button.on', # (None) emitted when toggle button goes into on state
        'button_off': 'toggle_button.off' # (None) emitted when toggle button goes into off state
    }

    def __init__(self) -> None:
        """
        Initialize internal instance variables
        """
        pass
    
    def register(self, emitter:EventEmitter) -> None:
        """
        Stores emitter for use in launch.
        Register event handlers with emitter.

        This method is called from the main thread once for each module in the 
        order the modules are defined in modules_list.
        """
        self.emitter = emitter
        emitter.emit(self.codes['print'], f'registering {self.__class__.__name__}')

    def launch(self) -> None:
        """
        Called after all modules have been registered. This should be where the
        modules non event driven functionality is executed.
        Each module is launched in its own thread. 
        """
        self.emitter.emit(self.codes['print'], f'launching {self.__class__.__name__}')
