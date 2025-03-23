from game import Room, Laberynth, Wall, Door, BombWall, Bomb, Mob, Aggro, Lazy
from north import North
from south import South
from east import East
from west import West
from orientation import Orientation

class Creator:
    def create_room(self, num):
        room = Room(num)
        room.orientation.append(self.create_north())
        room.orientation.append(self.create_south())
        room.orientation.append(self.create_east())
        room.orientation.append(self.create_west())
        north_wall = self.create_wall()
        room.addElementToOrientation(north_wall, North())
        south_wall = self.create_wall()
        room.addElementToOrientation(south_wall, South())
        east_wall = self.create_wall()
        room.addElementToOrientation(east_wall, East())
        west_wall = self.create_wall()
        room.addElementToOrientation(west_wall, West())
        return room

    def create_laberynth(self):
        return Laberynth()

    def create_north(self):
        return North()

    def create_south(self):
        return South()

    def create_east(self):
        return East()

    def create_west(self):
        return West()

    def create_wall(self):
        return Wall()

    def create_door(self, side1, side2):
        return Door(side1, side2)

    def create_bomb(self, em):
        return Bomb(em)

    def create_mob(self,hp,damage,room,mode):
        mob=Mob()
        mob.hp=hp
        mob.damage=damage
        mob.position = room
        mob.mode = mode
        return mob

    def create_mode_aggro(self):
        return Aggro()

    def create_mode_lazy(self):
        return Lazy()

class CreatorB(Creator):
    def create_wall(self):
        return BombWall()