# catbox.py
#
# Entry point for the Catbox app. Designed for Raspberry Pi 4 running Ubuntu or
# similar Linux distro. Ideally the system should be configured to run this
# script on boot, be connected to the internet, and have system sleep disabled.
#
# Event Emitters ...
#
# Modules (located) ...
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

import time
from threading import Thread

from pymitter import EventEmitter

from gui import launch_gui
from modules import modules_list
from modules.base_module import BaseModule

emitter = EventEmitter()

def load_n_launch_modules(emitter):
    time.sleep(3)
    print_code = BaseModule.codes['print']
    emitter.emit(print_code, 'registering meowdules ฅ(ﾐ⌣ᆽ⌣`ﾐ)∫')
    for module in modules_list:
        module.register(emitter)

    emitter.emit(print_code, 'launching meowdules')
    for module in modules_list:
        Thread(target=module.launch).start()
    
    emitter.emit(print_code, 'loaded and launched =^~^=')
Thread(target=load_n_launch_modules, args=(emitter,)).start()

launch_gui(emitter)