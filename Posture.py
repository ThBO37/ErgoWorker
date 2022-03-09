class Posture():
    def __init__(self, nom, angles):        #angles est un dictionnaire d'angles
        self.__nom = nom
        self.__angles = angles

    def verification_poignets(self):
        return (self.__angles("phi6a5a").estDefini() and self.__angles("theta6a5a").estDefini()
                and self.__angles("phi6b5b").estDefini())

    def verification_bras_superieurs(self):
        return (self.__angles("phi2a3").estDefini() and self.__angles("phi2b3").estDefini()
                and self.__angles("theta2a3").estDefini() and self.__angles("phi4a2a").estDefini()
                and self.__angles("theta4a2a").estDefini() and self.__angles("psi4a2a").estDefini()
                and self.__angles("phi4b2b").estDefini() and self.__angles("theta4b2b").estDefini()
                and self.__angles("psi4b2b").estDefini())

    def verification_bras_inferieurs(self):
        return (self.__angles("theta5a4a").estDefini() and self.__angles("theta5b4b").estDefini())

    def verification_tronc(self):
        return (self.__angles("phi7a3").estDefini() and self.__angles("theta7a3").estDefini()
                and self.__angles("psi7a3").estDefini() and self.__angles("phi7b3").estDefini()
                and self.__angles("theta7b3").estDefini() and self.__angles("psi7b3").estDefini())

    def verification_nuque(self):
        return (self.__angles("phi13").estDefini() and self.__angles("theta13").estDefini()
                and self.__angles("psi13").estDefini())

    def verification_jambes(self):
        return (self.__angles("phi8a7a").estDefini() and self.__angles("theta8a7a").estDefini()
                and self.__angles("psi8a7a").estDefini() and self.__angles("phi8b7b").estDefini()
                and self.__angles("theta8b7b").estDefini() and self.__angles("psi8b7b").estDefini()
                and self.__angles("theta9a8a").estDefini() and self.__angles("psi9a8a").estDefini()
                and self.__angles("theta9b8b").estDefini() and self.__angles("psi9b8b").estDefini())

    def verification_pieds(self):
        return (self.__angles("phi10a9a").estDefini() and self.__angles("theta10a9a").estDefini()
                and self.__angles("psi10a9a").estDefini() and self.__angles("phi10b9b").estDefini()
                and self.__angles("theta10b9b").estDefini() and self.__angles("psi10b9b").estDefini())

    def verification_REBA(self):
        return (verification_poignets(self) and verification_bras_inferieurs(self)
                and verification_bras_superieurs(self) and verification_tronc(self)
                and self.__angles("psi13").estDefini())

    def verification_RULA(self):
        return (verification_poignets(self) and verification_bras_inferieurs(self)
                and verification_bras_superieurs(self) and verification_nuque(self))

    def algorithmes_possibles(self):
        return (verification_REBA(self), verification_RULA(self))
