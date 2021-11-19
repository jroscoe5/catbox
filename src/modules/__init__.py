# modules.__init__.py
#
# Defines modules_list which is a list of all modules to be registered and 
# launched. Modules in modules_list are 
#

from modules.ambient_noises.module import AmbientNoisesModule
from modules.gui.module import GUIModule
from modules.tv.module import TVModule

modules_list = [
    AmbientNoisesModule(),
    GUIModule(),
    TVModule(),
]