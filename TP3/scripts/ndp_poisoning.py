from scapy.all import *

attack_mac=""
victim_mac=""
victim_ipv6=""
attack_ipv6=""

packetv6=(Ether(dst='victim_mac', src='attack_mac') / IPv6(src='attack_ipv6', dst='victim_ipv6'))

try:
    while True:
        send(packetv6)
        time.sleep(1)
except KeyboardInterrupt:
    quit()