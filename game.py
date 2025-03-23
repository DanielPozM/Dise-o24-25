from laberynth import Laberynth
from mob import Mob
from room import Room
from door import Door
from north import North
from south import South
from east import East
from west import West
from orientation import Orientation
from aggro import Aggro
from lazy import Lazy
from wall import Wall
from bomb import Bomb
from bomb_wall import BombWall
from being import Character


class Game:
    def __init__(self):
        self.laberynth = Laberynth()
        self.mobs = []
        self.character = None
        self.mob_threads = {}

    def add_mob(self, mob):
        mob.game = self
        self.mobs.append(mob)

    def launchMob(self, mob):
        import threading
        thread = threading.Thread(target=mob.act)
        if mob not in self.mob_threads:
            self.mob_threads[mob] = []
        self.mob_threads[mob].append(thread)
        thread.start()

    def terminateMob(self, mob):
        if mob in self.mob_threads:
            for thread in self.mob_threads[mob]:
                mob.vidas = 0

    def launchMobs(self):
        for mob in self.mobs:
            self.launchMob(mob)

    def terminateMobs(self):
        for mob in self.mobs:
            self.terminateMob(mob)

    def add_character(self, name):
        self.character = Character(10, 1, None, self, name)
        self.laberynth.enter(self.character)

    def open_doors(self):
        def openDoors(obj):
            if obj.isDoor():
                obj.opening()

        self.laberynth.run(openDoors)

    def close_doors(self):
        def closeDoors(obj):
            if obj.isDoor():
                obj.close()

        self.laberynth.run(closeDoors)

    def init_game(self):
        # what will make the game actually work
        pass

    def createLaberynth2RoomFM(self, creator):
        laberynth = creator.create_laberynth()
        room1 = creator.create_room(1)
        room2 = creator.create_room(2)
        door = creator.create_door(room1, room2)
        room1.addElementToOrientation(door, North())
        room2.addElementToOrientation(door, South())
        laberynth.addRoom(room1)
        laberynth.addRoom(room2)
        return laberynth

    def createLaberynth2BombRoom(self, creator):
        laberynth = creator.create_laberynth()
        room1 = creator.create_room(1)
        room2 = creator.create_room(2)
        door = creator.create_door(room1, room2)
        room1.addElementToOrientation(door, North())
        room2.addElementToOrientation(door, South())

        wall1 = creator.create_wall()
        bomb1 = creator.create_bomb(wall1)
        room1.addElementToOrientation(bomb1, East())

        wall2 = creator.create_wall()
        bomb2 = creator.create_bomb(wall2)
        room2.addElementToOrientation(bomb2, West())

        laberynth.addRoom(room1)
        laberynth.addRoom(room2)
        return laberynth

    def getRoom(self, num):
        return self.laberynth.getRoom(num)

    def createLaberynth4Room(self, creator):
        laberynth = creator.create_laberynth()

        room1 = creator.create_room(1)
        room2 = creator.create_room(2)
        room3 = creator.create_room(3)
        room4 = creator.create_room(4)

        door12 = creator.create_door(room1, room2)
        door13 = creator.create_door(room1, room3)
        door24 = creator.create_door(room2, room4)
        door34 = creator.create_door(room3, room4)

        room1.addElementToOrientation(door12, South())
        room1.addElementToOrientation(door13, East())
        room3.addElementToOrientation(door13, West())
        room3.addElementToOrientation(door34, South())
        room2.addElementToOrientation(door12, North())
        room2.addElementToOrientation(door24, East())
        room4.addElementToOrientation(door34, North())
        room4.addElementToOrientation(door24, West())

        mob1 = creator.create_mob(5, 10, room1, creator.create_mode_aggro())
        self.add_mob(mob1)
        mob3 = creator.create_mob(5, 10, room3, creator.create_mode_aggro())
        self.add_mob(mob3)
        mob2 = creator.create_mob(5, 1, room2, creator.create_mode_lazy())
        self.add_mob(mob2)
        mob4 = creator.create_mob(5, 1, room4, creator.create_mode_lazy())
        self.add_mob(mob4)

        room1.mob = mob1
        room2.mob = mob2
        room3.mob = mob3
        room4.mob = mob4

        laberynth.addRoom(room1)
        laberynth.addRoom(room2)
        laberynth.addRoom(room3)
        laberynth.addRoom(room4)

        return laberynth