from leaf import Leaf

class Decorator(Leaf):
    def __init__(self, em):
        super().__init__()
        self.em = em

    def __str__(self):
        return "I'm a decorator"