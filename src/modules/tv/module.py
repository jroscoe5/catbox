# tv
#  
# Catbox module for playing online videos of birds and squirrels.
# Support for offline tv maybe in the future.
#
# Authors:
#   Jonathon Roscoe / @jroscoe5
#

from queue import Queue
from threading import Thread
from time import sleep

from chromedriver_py import binary_path
from modules.base_module import BaseModule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class TVModule(BaseModule):
    """
    Plays online bird and squirrel videos using chromedriver and selenium. 
    """
    def __init__(self) -> None:
        super().__init__()
        self.event_queue = Queue()
        self.tv_running = False

    def register(self, emitter) -> None:
        super().register(emitter)

        @emitter.on(self.codes['start_timed_tv'])
        def start_timed_tv(duration):
            self.event_queue.put(['start', duration])

        @emitter.on(self.codes['stop_tv'])
        def stop_tv():
            self.event_queue.put(['stop', None])


    def launch(self) -> None:
        super().launch()
        while True:
            event = self.event_queue.get(block=True)
            if event[0] == 'start':
                self.tv_running = True
                Thread(target=self.__launch_timed_tv, args=(event[1],), daemon=True).start()
                self.emitter.emit(self.codes['print'], 'time for some tv!')
            if event[0] == 'stop':
                self.emitter.emit(self.codes['print'], 'turning off tv!')
                self.tv_running = False

    def __launch_timed_tv(self, duration):
        """
        Navigates to a video, full screens it and then sleeps until stopped or 
        duration times out.
        """
        options = Options()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])    
        driver = webdriver.Chrome(executable_path=binary_path, options=options)
        driver.implicitly_wait(10)

        driver.get('https://play-onrepeat.com/?search=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D56359TnQGww')

        sleep(5)

        video_element = driver.find_element_by_css_selector('#widget2')

        actionChains = ActionChains(driver)
        actionChains.double_click(video_element).perform()

        sleep(5)

        video_element.click()
        
        while (duration > 0 and self.tv_running):
            sleep(1)
            duration -= 1

        driver.quit()
