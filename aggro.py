import time
from mode import Mode

class Aggro(Mode):
    def __init__(self):
        super().__init__()

    def sleep(self, mob):
        print("Aggro: Currently sleeping...")
        time.sleep(1)

    def walk(self, mob):
        print("Aggro: Menacingly walking...")

    def attack(self, mob):
        print("Aggro: ¡My name is Mob Mobtoya, you killed my father, prepare to die!")

    def __str__(self):
        return "-aggro"