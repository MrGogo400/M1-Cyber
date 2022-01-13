enable
conf t
interface ethernet 0/1
switchport mode access
switchport port-security
switchport port-security violation restrict
switchport port-security maximum 1
switchport port-security mac-address sticky
exit
interface ethernet 0/2
switchport mode access
switchport port-security
switchport port-security violation restrict
switchport port-security maximum 1
switchport port-security mac-address sticky
exit
interface ethernet 0/3
switchport mode access
switchport port-security
switchport port-security violation restrict
switchport port-security maximum 1
switchport port-security mac-address sticky
exit
exit

enable
conf t
interface ethernet 0/1
switchport mode access
switchport access vlan 1
switchport port-security
switchport port-security maximum 1
switchport port-security violation restrict
exit
interface ethernet 0/2
switchport mode access
switchport access vlan 1
switchport port-security
switchport port-security maximum 1
switchport port-security violation restrict
exit
interface ethernet 0/3
switchport mode access
switchport access vlan 1
switchport port-security
switchport port-security maximum 1
switchport port-security violation restrict
exit
exit