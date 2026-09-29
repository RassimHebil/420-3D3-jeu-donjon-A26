from models.comportement import Comportement
from actions.action_attaque import ActionAttaque
from actions.action_defense import ActionDefense


class ComportementFurtif(Comportement):

    def __init__(self) -> None:
        self._tour = 0   # ← valeur initiale ?

    def agir(self, ennemi) -> str:
        self._tour += 1
        if self._tour % 2 == 0:
            return ActionAttaque
        return ActionDefense