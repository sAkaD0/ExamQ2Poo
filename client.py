from ville import Ville

class Client:
    nbrClient = 0
    listeClients = []
    def __init__(self, n, p, v):
        self.nom = n
        self.prenom = p
        self.ville = v

    def newUser(self):
        self.nom = input("Entrez le nom: ")
        self.prenom = input("Entrez le prénom: ")

        #Gestion Ville
        while 1:
            print(Ville.listeVilleDispo)
            ville = input("Choisissez votre ville: ")
            if ville in Ville.listeVilleDispo:
                self.ville = ville
                break
            else:
                print("Entrez une ville disponnible ! ")

        client = "client" + str(Client.nbrClient)
        client = Client(self.nom, self.prenom, self.ville)

        print("le client: ",  client.nom, client.prenom, client.ville, " à bien été créé")
        client = self.nom + "#" + self.prenom +"#" + self.ville

        Client.listeClients.append(client)

        Client.nbrClient += 1

        #Ecriture dans fichier
        fs = open("users.txt", "a")
        fs.write(self.nom+"#"+self.prenom+"#"+self.ville+"\n")
        fs.close()

    def deplacementClient(self):
        villeDepart = self.ville

        while 1:
            print(Ville.listeVilleDispo)
            Destination= input("Choisissez votre ville de Destination: ")
            if Destination in Ville.listeVilleDispo:
                self.ville = Destination
                villeArrive = self.ville
                break
            else:
                print("Entrez une ville disponnible ! ")

        #Appel Calcul cout




