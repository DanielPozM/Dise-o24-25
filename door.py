from map_prop import MapProp

class Door(MapProp):
    def __init__(self, side1, side2):
        self.open = False
        self.side1 = side1
        self.side2 = side2

    def enter(self,Char):
        print("Going through door")
        if self.open:
            if Char.position == self.side1:
                self.side2.enter(Char)
            else:
                self.side1.enter(Char)
        else:
            print("The door is closed")

    def opening(self):
        print("Opening door")
        self.open = True

    def close(self):
        print("Closing door")
        self.open = False

    def isDoor(self):
        return True

    def __str__(self):
        return "I'm a door"