# catbox.py
#
# Entry point for the Catbox app. Designed for Raspberry Pi 4 running Ubuntu or
# similar Linux distro. Ideally the system should be configured to run this
# script on boot, be connected to the internet, and have system sleep disabled.
#
# Event Emitters ...
#
# Modules (located) ...
# The GUI module is loaded before all other modules are loaded.
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

import json

r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |   CatBox   | /
  )  |  \  `.___________|/
  `--'   `--'

  art by hjm
"""
