from scapy.all import *

#First Steps
#a=IP(ttl=10)
#print([a])
#print([a.src])
#a.dst="192.168.1.1"
#print([a])
#print([a.src])
#del(a.ttl)
#print([a])
#print([a.ttl])

#Stacking layers
#print([IP()])
#print([IP()/TCP()])
#print([Ether()/IP()/TCP()])
#print([IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"])
#print([Ether()/IP()/IP()/UDP()])
#print([IP(proto=55)/TCP()])

#print([raw(IP())])
#a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
#hexdump(a)
#b=raw(a)
#print([b])
#c=Ether(b)
#print([c])

#c.hide_defaults()
#print([c])

#Reading PCAP files
#a=rdpcap("J:/test.pcap")
#print([a])

#Generating sets of packets
#a=IP(dst="www.slashdot.org/30")
#print([a])
#print([p for p in a])
#c=TCP(dport=[80,443])
#print=([p for p in a/c])

#Sending packets
#send(IP(dst="1.2.3.4")/ICMP())
#sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface="Realtek PCIe GbE Family Controller")
#sendp("I'm travelling on Ethernet", iface="Realtek PCIe GbE Family Controller", loop=1, inter=0.2)
#sendp(rdpcap("J:/test.pcap"))
#send(IP(dst='127.0.0.1'), return_packets=True)

#Fuzzing
#send(IP(dst="target")/fuzz(UDP()/NTP(version=4)),loop=1)

#Injecting bytes
#pkt = IP(len=RawVal(b"NotAnInteger"), src="127.0.0.1")
#print(bytes(pkt))

#Send and receive packets (sr)
#p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
#print([p])
#p.show()

#sr1(IP(dst="192.168.5.1")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.slashdot.org")))

#sr(IP(dst="192.168.8.1")/TCP(dport=[21,22,23]))
#ans, unans = _
#ans.summary()

#sr(IP(dst="172.20.29.5/30")/TCP(dport=[21,22,23]),inter=0.5,retry=-2,timeout=1)

#p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
#s = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.slashdot.org")))

#wrpcap('test.pcap', s)
#wrpcap('test2.pcap', p)

