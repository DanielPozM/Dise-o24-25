from map_prop import MapProp

class Container(MapProp):
    def __init__(self):
        super().__init__()
        self.child = []
        self.orientation = []

    def add_child(self, child):
        child.father = self
        self.child.append(child)

    def remove_child(self, child):
        self.child.remove(child)

    def addOrientation(self, orientation):
        self.orientation.append(orientation)

    def removeOrientation(self, orientation):
        self.orientation.remove(orientation)

    def addElementToOrientation(self, element, orientation):
        orientation.add(element, self)

    def run(self, func):
        func(self)
        for child in self.child:
            child.run(func)
        for orientation in self.orientation:
            orientation.run(func, self)