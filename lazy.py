import time
from mode import Mode

class Lazy(Mode):
    def __init__(self):
        super().__init__()

    def sleep(self, mob):
        print("Lazy: Zzzzz...")
        time.sleep(3)

    def walk(self, mob):
        print("Lazy: Barely walking...")

    def attack(self, mob):
        print("Lazy: Fake attacking...")

    def __str__(self):
        return "-lazy"