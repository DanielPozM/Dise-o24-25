from wall import Wall

class BombWall(Wall):
    def __init__(self):
        super().__init__()
        self.active = False

    def enter(self):
        print("Going through a bombwall")

    def __str__(self):
        return "I'm a bombwall"