# Introduction à la sécurité des protocoles réseaux 

Hugo Marques & Emma Durand.

## 1. CAM Flooding, port-stealing et mise en œuvre de contre-mesures

**Rappels théoriques**

*- Qu'appelle-t-on CAM table lorsque l'on parle d'un switch. Expliquez la technique permettant de
la corrompre.*

La **CAM Table** est une table présente sur un switch qui contient les réferencements des adresses MAC par rapport aux interfaces connectées.

La technique de **MAC Flooding** permet de remplir la **CAM Table** (atteint sa limite) ce qui dans certains cas change le comportement d'un switch pour qu'il imite un hub (concentrateur). 

Elle consiste en l'envoi d'une grande quantité de trames ethernet sur le même port avec une adresse MAC source différente, ce qui a pour effet de saturer la **CAM Table**.

*- A l’aide de scapy, écrivez un script python permettant de provoquer le débordement de la CAM.*

* [Script python](scripts/cam_flooding.py)

*- Ecrivez ensuite un second script permettant de réaliser une attaque de type port stealing.*

* [Script python](scripts/port_stealing.py)

**Mise en oeuvre de Port-Security**

*- En vous aidant du tableau 1 en annexe, mettez en œuvre les fonctionnalités Port-Security sur
votre switch.*

Infrastructure Eve-ng : 

![](img/topo_eve.PNG)

Fonctionnalités mises en place pour chaque interface : 
* `switchport port-security` : Active le port security.
* `switchport port-security violation restrict` : Lorsqu'une violation est détectée, le port arrête le trafic des adresses non authorisées et envoie un message de log.
* `switchport port-security maximum 5` : Permet de définir le nombre maximum d'adresses MAC sur l'interface.

> `switchport port-security mac address xx:xx` -> sécurisé et utile, mais avec évolution du SI, peut devenir problématique.


*- Testez le bon fonctionnement de celle-ci, votre script ne doit plus permettre le débordement de
la CAM ou le « vol de port ».*

Lorsqu'on exécute l'attaque, on remarque bien sur le switch détecte une anomalie et va empêcher le transfert des addresses mac malveillantes.

![](img/port-security.PNG)