from creator import Creator, CreatorB
from game import Game
import time

#ejemplo de uso
fm = Creator()
game = Game()
game.laberynth = game.createLaberynth2RoomFM(fm)
room1=game.getRoom(1)
room2=game.getRoom(2)
print(room1.num)
print(room2.num)

#laberinto con paredes bomba
fmb = CreatorB()
game.laberynth = game.createLaberynth2BombRoom(fmb)
room1=game.getRoom(1)
room2=game.getRoom(2)
print(room1.east.active)
print(room2.west.active)

# Crear laberinto de 4 habitaciones
fm = Creator()
game.laberynth = game.createLaberynth4Room(fm)

# Mostrar el número de cada habitación
for room in game.laberynth.child:
    print(f"Room  {room.num}")

#mostrar los bichos del juego
for mob in game.mobs:
    print(mob)
    print(f"Mob with {mob.hp} HP and {mob.damage} DAMAGE")
    print(f"Position {mob.position.num}")


# Ejemplo de uso de recorrer con print
print("\nRunning the laberynth and printing:")
game.laberynth.run(print)

#def abrirPuertas(obj):
#    if obj.esPuerta():
#        obj.abrir()
game.open_doors()

game.close_doors()

mob=game.mobs[0]
game.launchMob(mob)
time.sleep(3)
mob.hp=0