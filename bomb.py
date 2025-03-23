from decorator import Decorator

class Bomb(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.active = False

    def isBomb(self):
        return True

    def __str__(self):
        return "I'm a bomb"