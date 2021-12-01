# modules.__init__.py
#
# Defines modules_list which is a list of all modules to be registered and 
# launched. Modules in modules_list are all launched in their own thread.
#

from modules.ambient_noises.module import AmbientNoisesModule
from modules.debug_signals.module import DebugSignalsModule
from modules.motion_sensor.module import MotionSensorModule
from modules.tv.module import TVModule

modules_list = [
    # DebugSignalsModule(),
    # AmbientNoisesModule(), # playsound dependency issues on raspberry linux
    MotionSensorModule(),
    TVModule(),
]
