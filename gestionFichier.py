from client import Client
from ville import Ville

def afficherClients():
    fs = open("users.txt", 'r')
    clients = fs.readlines()
    print(clients)

def nombreClient():
    print("Il y à ", Client.nbrClient, "clients")

def chargerVilles():
    fs = open("villes.txt", "r")
    rows = fs.readlines()

    for villes in rows:
        if villes.strip().split("#")[0] in Ville.listeVilleDispo:
            pass
        else:
            Ville.listeVilleDispo.append(villes.strip().split("#")[0])
    fs.close()

def chargerClient():
    fs = open("users.txt", "r")
    rows = fs.readlines()

    for client in rows:
        Client.listeClients.append(client.strip().split("#")[0])

    fs.close()