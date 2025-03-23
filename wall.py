from map_prop import MapProp

class Wall(MapProp):
    def __init__(self):
        super().__init__()

    def enter(self,Char):
        print("Bonking a wall")

    def __str__(self):
        return "I'm a wall"