Building configuration...

Current configuration : 1059 bytes
!
! Last configuration change at 18:07:29 EET Thu Jan 6 2022
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname Switch
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
clock timezone EET 2 0
!
!
!
!
!
!
!
!
ip cef
no ipv6 cef
!
!
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
!
interface Ethernet0/1
 switchport port-security maximum 3
 switchport port-security violation restrict
 switchport port-security mac-address 0050.0000.0100
!
interface Ethernet0/2
!
interface Ethernet0/3
 switchport mode access
 switchport port-security maximum 3
 switchport port-security violation restrict
 switchport port-security mac-address 0050.0000.0400
 switchport port-security
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
!
!
end