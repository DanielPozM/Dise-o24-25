from mode import Mode
from aggro import Aggro
from being import Being

class Mob(Being):
    def __init__(self):
        self.mode = None
        self.running = True
        self.damage = None
        self.hp = None
        self.position = None

    def act(self):
        while self.isAlive():
            self.mode.act(self)

    def initAggro(self):
        self.mode = Aggro()
        self.damage = 10
        self.hp = 5

    def initLazy(self):
        self.damage = 1
        self.hp = 5

    def isAlive(self):
        return self.hp > 0

    def __str__(self):
        return "I am an "+self.mode.__str__()+" mob"