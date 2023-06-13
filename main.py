from gestionFichier import *

class Menu:

    def main(self):
        print("1. Créer un utilisateur")
        print("2. Enregistrer une ville")
        print("3. Afficher la liste des clients")
        print("4. Afficher le nombre de clients")
        print("5. Quitter")
        choix = input("Entrez votre choix: ")
        return choix

    def choixUser(self, choix):
        if choix == "1":
            chargerClient()
            client1.newUser()
        if choix == "2":
            chargerVilles()
            ville1.newCity()
        if choix  == "3":
            afficherClients()
        if choix  == "4":
            nombreClient()
        if choix  == "5":
            quit()

menu = Menu()
client1 = Client("n","p", "v")
ville1 = Ville("n","c")

while True:
    choix = menu.main()
    menu.choixUser(choix)

