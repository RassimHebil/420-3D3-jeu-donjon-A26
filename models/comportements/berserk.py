from models.comportement import Comportement
from actions.action_attaque_double import ActionAttaqueDouble
from actions.action_attaque import ActionAttaque


class ComportementBerserk(Comportement):
    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return ActionAttaqueDouble
        else:
            return ActionAttaque