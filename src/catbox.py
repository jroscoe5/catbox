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
#   Kyle Roscoe / @kroscoe45

from time import sleep
from threading import Thread

from pymitter import EventEmitter

from gui import launch_gui
from modules import modules_list
from modules.base_module import BaseModule

emitter = EventEmitter()

def load_n_launch_modules(emitter):
    sleep(3)
    print_code = BaseModule.codes['print']
    ready_code = BaseModule.codes['ready']
    emitter.emit(print_code, 'registering meowdules ฅ(ﾐ⌣ᆽ⌣`ﾐ)∫')
    for module in modules_list:
        try:
            module.register(emitter)
        except Exception as exc:
            emitter.emit(print_code, str(exc))

    emitter.emit(print_code, 'launching meowdules (ﾐ^ᆽ^ﾐ)')
    for module in modules_list:
        Thread(target=module.launch, daemon=True).start()

    sleep(1)
    emitter.emit(ready_code)

if __name__ == '__main__':
    Thread(target=load_n_launch_modules, args=(emitter,)).start()
    launch_gui(emitter)
