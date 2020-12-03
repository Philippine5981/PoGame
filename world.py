import random
from constants import *


def create_world():
    world = []
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if random.randint(0, 9) == 0 and (x, y) != (0, 0):
                world.append(["cookie"])
            else:
                world.append([])

    return world


def get_index(x, y):
    return y * WORLD_WIDTH + x


def get_room(world, x, y):
    index = get_index(x, y)
    return world[index]
