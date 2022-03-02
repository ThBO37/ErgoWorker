class Angle():
    def __init__(self, nom, valeur):
        self.__nom = nom
        self.__estDefini = (type(valeur)==float)
        if self.estDefini:
            self.__valeur = valeur
        else:
            self.__valeur = None

    def estDefini(self):
        return self.__estDefini
