from orientation import Orientation

class South(Orientation):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, element, container):
        container.south = element

    def run(self, func, container):
        if container.south is not None:
            func(container.south)

    def __str__(self):
        return "I'm South"