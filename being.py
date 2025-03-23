class Being:
        def __init__(self):
            self.hp = None
            self.damage = None
            self.position = None
            self.game = None

class Character(Being):
    def __init__(self, hp, damage, game, name):
        self.name = name