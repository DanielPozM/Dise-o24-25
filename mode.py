class Mode:
    def __init__(self):
        pass
    def act(self, mob):
        self.sleep(mob)
        self.walk(mob)
        self.attack(mob)

    def sleep(self, mob):
        pass

    def walk(self, mob):
        pass

    def attack(self, mob):
        pass

    def __str__(self):
        return "Mode Initiated"