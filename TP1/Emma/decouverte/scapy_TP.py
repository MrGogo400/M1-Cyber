from scapy.all import *

####### ICMP #########

print('\n---- ICMP ----\n')

ping = Ether() / IP(dst='192.168.1.1') / ICMP()

# ping.show()
# sendp(ping)

# Send and receive answer of the ping
response, not_res = srp(ping)
# rep = s.srp1(ping)

print ('\n')

# Show the answer
response.show()

# Write a pcap
wrpcap('ping.pcap', response)

####### TCP ############

print('\n---- TCP ----\n')

tcp = Ether() / IP(dst='192.168.1.1') / TCP()
resp_tcp, notr = srp(tcp)
resp_tcp.show()

##############


