from models.comportement import Comportement
from actions.action_defense import ActionDefense
from actions.action_attaque import ActionAttaque


class ComportementDefensif(Comportement):

    def agir(self, ennemi) -> str:
        if ennemi.hp < ennemi.hp_max * 0.5:
            return ActionDefense
        return ActionAttaque