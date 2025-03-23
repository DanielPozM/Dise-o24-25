from orientation import Orientation

class North(Orientation):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, element, container):
        container.north = element

    def run(self, func, container):
        if container.north is not None:
            func(container.north)

    def __str__(self):
        return "I'm North"