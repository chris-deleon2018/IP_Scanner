#!/usr/bin/env python

# Import Scapy.all but change name so do not have to use scapy.all.functionName
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/CIDR. Ex: 192.168.1.0/24")
    options = parser.parse_args()
    return options


def scan(ip):
    # Create a scapy ARP object and set the destination IP to ip arg passed
    arp_request = scapy.ARP(pdst=ip)

    # Create a scapy Ethernet object and set the MAC to the broadcast MAC
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Append an ARP and Ethernet packet and store in new variable
    arp_request_broadcast = broadcast/arp_request

    # Send Ether/ARP request and save the ARP response (the response returns two list)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())

    # Create a List of Dictionaries using IP and MAC address's of answered responses
    client_list = []
    for answer in answered_list:
        target_client = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        client_list.append(target_client)
    return client_list


def print_result(scan_results):
    # Print the Client IP & MAC address
    print("------------------------------------")
    print("IP\t\tMAC Address")
    print("------------------------------------")
    for client in scan_results:
        print(client["ip"] + "\t" + client["mac"])


options = get_arguments()
scan_results = scan(options.target)
print_result(scan_results)