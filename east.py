from orientation import Orientation

class East(Orientation):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, element, container):
        container.east = element

    def run(self, func, container):
        if container.east is not None:
            func(container.east)

    def __str__(self):
        return "I'm East"