from orientation import Orientation

class West(Orientation):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, element, container):
        container.west = element

    def run(self, func, container):
        if container.west is not None:
            func(container.west)

    def __str__(self):
        return "I'm West"