import json
from laberynth_builder import LaberynthBuilder


class Director:
    def __init__(self):
        self.builder = None
        self.dict = None

    def getGame(self):
        return self.builder.getGame()

    def proccess(self, file):
        self.readFile(file)
        self.initBuilder()
        self.buildLaberynth()
        self.buildGame()
        self.buildMob()

    def buildGame(self):
        self.builder.buildGame()

    def initBuilder(self):
        self.builder = LaberynthBuilder()

    def buildLaberynth(self):
        self.builder.buildLaberynth()
        for each in self.dict['laberinto']:
            self.buildRecursiveLaberynth(each, 'root')

        for each in self.dict['puertas']:
            self.builder.buildDoor(each[0], each[1], each[2], each[3])

            # recorrer la colección de puertas para fabricarlas
        for each in self.dict['puertas']:
            self.builder.buildDoor(each[0], each[1], each[2], each[3])

    def buildRecursiveLaberynth(self, each, padre):
        print(each)
        if each['tipo'] == 'habitacion':
            con = self.builder.buildRoom(each['num'])

        if each['hijos'] != None:
            for child in each['hijos']:
                self.buildRecursiveLaberynth(child, con)

    def readFile(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict = data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None

    def buildMob(self):
        for each in self.dict['bichos']:
            self.builder.buildMob(each['modo'], each['posicion'])