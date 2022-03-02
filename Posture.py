class Posture():
    def __init__(self, nom, angles):        #angles est un dictionnaire d'angles
        self.__nom = nom
        self.__phi13 = angles("phi13")
        self.__theta13 = angles("theta13")
        ...

    def algorithmes_possibles(self):

        def verification_poignets(self):
            return (self.__phi6a5a.estDefini() and self.__theta6a5a.estDefini()
                    and self.__phi6b5b.estDefini())

        def verification_bras_superieurs(self):
            return (self.__phi2a3.estDefini() and self.__phi2b3.estDefini()
                    and self.__theta2a3.estDefini() and self.__phi4a2a.estDefini()
                    and self.__theta4a2a.estDefini() and self.__psi4a2a.estDefini()
                    and self.__phi4b2b.estDefini() and self.__theta4b2b.estDefini()
                    and self.__psi4b2b.estDefini())

        def verification_bras_inferieurs(self):
            return (self.__theta5a4a.estDefini() and self.__theta5b4b.estDefini())
        
        def verification_tronc(self):
            return (self.__phi7a3.estDefini() and self.__theta7a3.estDefini()
                    and self.__psi7a3.estDefini() and self.__phi7b3.estDefini()
                    and self.__theta7b3.estDefini() and self.__psi7b3.estDefini())

        def verification_nuque(self):
            return (self.__phi13.estDefini() and self.__theta13.estDefini()
                    and self.__psi13.estDefini())

        def verification_jambes(self):
            return (self.__phi8a7a.estDefini() and self.__theta8a7a.estDefini()
                    and self.__psi8a7a.estDefini() and self.__phi8b7b.estDefini()
                    and self.__theta8b7b.estDefini() and self.__psi8b7b.estDefini()
                    and self.__theta9a8a.estDefini() and self.__psi9a8a.estDefini()
                    and self.__theta9b8b.estDefini() and self.__psi9b8b.estDefini())

        def verification_pieds(self):
            return (self.__phi10a9a.estDefini() and self.__theta10a9a.estDefini()
                    and self.__psi10a9a.estDefini() and self.__phi10b9b.estDefini()
                    and self.__theta10b9b.estDefini() and self.__psi10b9b.estDefini())

        def verification_REBA(self):
            return (verification_poignets(self) and verification_bras_inferieurs(self)
                    and verification_bras_superieurs(self) and verification_tronc(self)
                    and self.__psi13.estDefini())

        def verification_RULA(self):
            return (verification_poignets(self) and verification_bras_inferieurs(self)
                    and verification_bras_superieurs(self) and verification_nuque(self))

    return (verification_REBA(self), verification_RULA(self))
