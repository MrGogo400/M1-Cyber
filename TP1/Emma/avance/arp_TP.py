#!/usr/bin/python3.9

from scapy.all import *

def parse_arp(pck):
    """ Parse ARP requets and replies
    """
    if pck[ARP].op == 1:
        print('--- ARP Request ---')
        print(pck.summary())
        print(pck[Ether].src, 'has IP', pck[ARP].psrc)

    if pck[ARP].op == 2:
        print('-- ARP Reply --')
        print(pck.summary())

# Capturer le traffic ARP
capture = sniff(filter="arp", prn=parse_arp)
# wrpcap("capture.pcap", capture)

# --- ARP Request ---
# Ether / ARP who has 192.168.1.30 says 192.168.1.137 / Padding
# ac:f1:08:78:99:f0 has IP 192.168.1.137
# --- ARP Request ---
# Ether / ARP who has 192.168.1.30 says 192.168.1.137 / Padding
# ac:f1:08:78:99:f0 has IP 192.168.1.137

def arp_request(ip_src, ip_dst):
    """ Create ARP request
    """
    pck = Ether() / ARP(op=1, psrc=ip_src, pdst=ip_dst)
    print('--- ARP packet ---\n')
    pck.show()

    # Send the packet
    resp, send = srp(pck)

    # Show the reply
    print('\n--- Response ---\n')
    resp.show()

# Créer une requête ARP
arp_request('192.168.1.40', '192.168.1.1')
