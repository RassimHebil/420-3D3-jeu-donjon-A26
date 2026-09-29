import random
from models.actions import action_defense
from models.comportement import Comportement
from actions.action_attaque import ActionAttaque
from actions.action_defense import ActionDefense


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> str:
        return random.choice([ActionAttaque, ActionDefense])