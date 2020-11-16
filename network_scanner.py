#!/usr/bin/env python

import scapy.all as scapy
import argparse

# get flag arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="target IP / IP range")
    options = parser.parse_args()
    return options

# ping scan
def ping_scan(ip):
    scapy.arping(ip)
    
# scan and store in a list of dictionary
def scan(ip):
    # arp_request = scapy.ARP()
    # print(arp_request.summary())  # packet summary
    # arp_request.show()  # details of packet
    # scapy.ls(scapy.ARP())   # see arguments and help
    
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # empty mac layer
    arp_request_broadcast = broadcast/arp_request   # combine class
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)   # return a tuple of two lists, wait for 1 second at most
    
    clients_list = []   # store list of dictionary
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac":element[1].hwsrc}
        client_list.append(client_dict)
        
    return clients_list
 
# print function
def print_result(results_list):
    print("IP\t\t\t\t MAC Address\n---------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
