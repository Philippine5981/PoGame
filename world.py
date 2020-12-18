import random
from constants import *

#objet = lorsque je lance le jeu je choisis quel objet va apparaitre (dans main())
def create_world(objet):
    world = []
    for y in range (10):
        for x in range(WORLD_WIDTH):
            if random.randint(0, 10) == 0 and (x, y) != (0, 0):
                world.append([objet])
            # elif random.randint(0, 10) == 0 and (x, y) != (0, 0):
            #     world.append(["gel"])
            else:
                world.append([])
    for y in range(WORLD_HEIGHT-10):
        for x in range(WORLD_WIDTH):
            world.append([])

    return world


def get_index(x, y):
    return y * WORLD_WIDTH + x


def get_room(world, x, y):
    index = get_index(x, y)
    return world[index]
