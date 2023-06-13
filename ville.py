class Ville:
    position = 0
    listeVilleDispo = []
    def __init__(self, n, c):
        self.nom = n
        self.cout = c

    def newCity(self):
        print(Ville.listeVilleDispo)
        self.nom = input("Entrez le nom de la ville: ")
        self.cout = input("Entrez le coût: ")

        if self.nom in Ville.listeVilleDispo:
            print("La ville existe déjà !")
            print("Voici la liste des villes déjà disponnibles: ", Ville.listeVilleDispo)
        else:
            Ville.listeVilleDispo.append(self.nom)

            fs = open("villes.txt", "a")
            fs.write(self.nom + "#" + self.cout + "\n")

            fs.close()



