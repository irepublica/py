#!/usr/bin/env python

import subprocess
import optparse
import re

# function to take arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] pelase specify a new mac, use --help for more info.")
    else:
        return parser.parse_args()
  
# function to change mac
def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# function to get current mac 
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] could not read mac address")
       
      
### main
(options, arguments) = get_arguments()
current_mac = get_current_mac(options.interface)
print("current mac = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] mac address was successfully changed to " + str(current_mac))
else:
    print("[-] mac address did not get changed")
    



  
  

