from container import Container


class Laberynth(Container):
    def __init__(self):
        super().__init__()

    def enter(self, Char):
        print("Entering the Laberynth")
        room1 = self.getRoom(1)
        room1.enter(Char)

    def __str__(self):
        return "I'm a Laberynth"

    def addRoom(self, room):
        self.child.append(room)

    def getRoom(self, num):
        for room in self.child:
            if room.num == num:
                return room
        return None

    def run(self, func):
        func(self)
        for child in self.child:
            child.run(func)