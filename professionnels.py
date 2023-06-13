from main import *

class Pro(Client):
    def __init__(self, n, p, v, pr):
        super.__init__(n, p, v)
        self.profession = pr


    def reducePrice(self):
        ville1.cout -= 1

        print("Vous avez une réduction de 1 sur votre trajet ! ")
