from models.comportement import Comportement


class ComportementBerserk(Comportement):
    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return "attaque double!"
        else:
            return "attaque"