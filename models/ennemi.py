from random import random

from models.comportement import Comportement

class Ennemi:
    def __init__(self, nom: str, hp: int, attaque: int, comportement: Comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self.comportement = comportement  # objet de type Comportement
                                          #objet de type qui hérite de Comportement


    def agir(self):
        return self.comportement.agir(self)


    def recevoir_degats(self, degats):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0

    def set_comportement(self, nouveau_comportement):
        self.comportement = nouveau_comportement

    def get_comportement(self):
        return self.comportement