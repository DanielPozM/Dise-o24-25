from container import Container

class Room(Container):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def enter(self, Char):
        print(f"Going into room  {self.num}")
        Char.position=self

    def __str__(self):
        return "I'm a room"