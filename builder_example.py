from director import Director
from laberynth_builder import LaberynthBuilder
from laberynth import Laberynth
from room import Room
from door import Door
import time

director = Director()

filename = "./laberynth/lab2Hab.json"

data = director.readFile(filename)
if data:
    print("Data from JSON file:")
    print(data)
else:
    print("Failed to read data from JSON file.")

game = director.proccess(filename)
game = director.getGame()

# Ejemplo de uso de recorrer con print
print("\nRecorriendo el laberinto e imprimiendo:")
game.laberynth.run(print)

#mostrar los bichos del juego
for mob in game.mobs:
    print(mob)
    print(f"Bicho con {mob.hp} vidas y {mob.damage} de poder")
    print(f"Posición {mob.position.num}")

game.open_doors()
game.launchMobs()
time.sleep(3)
game.terminateMobs()