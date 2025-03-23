class MapProp:
    def __init__(self):
        self.father = None

    def run(self, func):
        func(self)

    def enter(self, Char):
        pass

    def isDoor(self):
        return False

    def __str__(self):
        return "Im a MapProp"