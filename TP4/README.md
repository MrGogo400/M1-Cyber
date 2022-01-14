# Manipulation des sockets réseaux à l'aide de python

Hugo Marques & Emma Durand.

# Conception d’un outil de diagnostique réseau :

## Fonctionnalités du client : 

* [client.py](scripts/client.py)

* Peut envoyer des paquets TCP ou UDP.
* Peut renseigner l'addresse IP, le port et le protocole.
* Reçoi un message d'accceuil de la part du serveur.
* Un shell s'ouvrira après la connexion établie.

## Fonctionnalité du serveur :

* [server.py](scripts/server.py)

* Peut écouter sur des ports TCP ou UDP.
* Peut spécifier l'addresse IP, le port ou le protocole.
* Peut envoyer un message personnalisé au client.
* Peut choisir le shell du client.
* Peut logger les connexions. 
