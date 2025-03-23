from laberynth import Laberynth
from game import Game
from door import Door
from north import North
from south import South
from east import East
from west import West
from room import Room
from wall import Wall
from mob import Mob
from aggro import Aggro
from lazy import Lazy


class LaberynthBuilder:
    def __init__(self):
        self.laberynth = None
        self.game = None

    def buildGame(self):
        self.game = Game()
        self.game.laberynth = self.laberynth

    def buildLaberynth(self):
        self.laberynth = Laberynth()

    def buildRoom(self, num):
        room = Room(num)
        room.addOrientation(self.buildNorth())
        room.addOrientation(self.buildSouth())
        room.addOrientation(self.buildEast())
        room.addOrientation(self.buildWest())
        for each in room.orientation:
            room.addElementToOrientation(self.buildWall(), each)
        self.laberynth.addRoom(room)
        return room

    def buildWall(self):
        return Wall()

    def buildDoor(self, side1, o1, side2, o2):
        room1 = self.laberynth.getRoom(side1)
        room2 = self.laberynth.getRoom(side2)
        door = Door(room1, room2)
        objOr1 = self.getObject(o1)
        objOr2 = self.getObject(o2)
        room1.addElementToOrientation(door, objOr1)
        room2.addElementToOrientation(door, objOr2)

    def getObject(self, chain):
        obj = None
        match chain:
            case 'Norte':
                obj = self.buildNorth()
            case 'Sur':
                obj = self.buildSouth()
            case 'Este':
                obj = self.buildEast()
            case 'Oeste':
                obj = self.buildWest()
        return obj

    def buildNorth(self):
        return North()

    def buildSouth(self):
        return South()

    def buildEast(self):
        return East()

    def buildWest(self):
        return West()

    def buildMobAggro(self):
        mob = Mob()
        mob.mode = Aggro()
        mob.initAggro()
        return mob

    def buildMobLazy(self):
        mob = Mob()
        mob.mode = Lazy()
        mob.initLazy()
        return mob

    def getGame(self):
        return self.game

    def buildMob(self, mode, position):
        mob=Mob()
        if mode == 'Agresivo':
            mob = self.buildMobAggro()
        if mode == 'Perezoso':
            mob = self.buildMobLazy()
        room = self.laberynth.getRoom(position)
        room.enter(mob)
        self.game.add_mob(mob)