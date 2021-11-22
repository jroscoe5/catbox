# gui.py
#
# Implements a simple GUI for the main thread to run after loading and launching
# all modules. Can listen and emit events but all gui api calls must be made
# from main thread.
#

from queue import Queue

import PySimpleGUI as sg

from modules.base_module import BaseModule

# art by hjm
LOGO = r'''
,-.       _,---._       / \
/  )    .-'       `./\_/   \
(  (   ,'            `/     /|
\  `-"             \'\    /  |
`.              ,  \ \  /    |
/`.          ,'-`---- Y     ,
(     /      ;        |    ,
|  ,-.    ,-'         |   /
|  | (   |   CatBox   |  /
)  |  \  `.___________| /
`--'   `--'

'''

def create_window():
    sg.theme('DarkAmber')
    background_color = sg.theme_background_color()
    layout = [  
        [sg.Multiline(LOGO, 
            size=(30,15),
            background_color=background_color,
            border_width=0,
            pad=((0,0), (300,0)),
            disabled=True,
            no_scrollbar=True,
            font=('Courier', 20))
        ],
        [sg.Multiline("Welcome to Catbox =^.^=\n",
            key='--output--',
            font=('Courier', 15),
            size=(80,2),
            background_color=background_color,
            border_width=0,
            autoscroll=True,
            no_scrollbar=True,
            disabled=True,
            justification='center')
        ]
    ]

    dimensions = sg.Window.get_screen_size()
    window = sg.Window('Catbox', layout, no_titlebar=True, location=(0,0), size=dimensions, element_justification='center')
    window.finalize()
    window.maximize()
    return window

def launch_gui(emitter):
    event_queue = Queue()

    @emitter.on(BaseModule.codes['print'])
    def add_to_queue(message):
        event_queue.put(message)

    window = create_window()
    while True:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break
            
        while not event_queue.empty():
            item = event_queue.get()
            window['--output--'].print(item)

