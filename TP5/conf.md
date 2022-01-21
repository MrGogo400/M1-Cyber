SW1
```
enable
conf t
vlan 46
name DSI
exit
vlan 100
name SRV_TECH
exit
vlan 103
name SRV_MGMT
exit
vlan 61
name PRINT
exit
vlan 62
name CAM
exit
vlan 63
name VOIP
exit
int port-channel 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 46,61,62,63,100,103
exit
int port-channel 5
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 46,61,62,63,100,103
exit
int e1/1
switchport mode access
switchport access vlan 61
exit
exit
```

SW2
```
enable
conf t
vlan 61
name PRINT
exit
vlan 101
name SRV_COMM
exit
vlan 110
name INVITES
exit
int port-channel 1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 61,101,110
exit
int port-channel 2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 61,101,110
exit
int e1/1
switchport mode access
switchport access vlan 61
exit
exit
```

SW3
```
enable
conf t
vlan 42
name PROD
exit
vlan 41
name BE
exit
vlan 62
name CAM
exit
vlan 63
name VOIP
exit
int port-channel 2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 41,42,62,63
exit
int port-channel 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 41,42,62,63
exit
exit
```

SW4
```
enable
conf t
vlan 42
name PROD
exit
vlan 41
name BE
exit
vlan 44
name RH
exit
vlan 45
name DIR
exit
vlan 43
name CPTA
exit
vlan 61
name PRINT
exit
int port-channel 3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 41,42,43,44,45,61
exit
int port-channel 4
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 41,42,43,44,45,61
exit
exit
```

SW5
```
enable
conf t
vlan 62
name CAM
exit
vlan 63
name VOIP
exit
vlan 102
name SRV_BE
exit
int port-channel 4
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 62,63,102
exit
int port-channel 5
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan add 62,63,102
exit
int e1/0
switchport mode access
switchport access vlan 62
exit
exit
```  