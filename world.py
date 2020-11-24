import random

from constants import *

def get_index(x,y):
    return y*WORLD_WIDTH+x

#def get_index(self, x, y):
#     x = x
#     y = y
#     i = y
#     j = x
# #    x = x - self.rect.left
# #    y = y - self.rect.top
# #    i = y // self.dy
# #    j = x // self.dx
#     return i, j

def create_world(width, height):
    world = []
    index=[]
    for y in range(WORLD_HEIGHT*10):
        for x in range(WORLD_WIDTH*10):
            index = get_index(x,y)
            world.insert(index,random.choices(available_items, k=2)),
            # world[index].insert(0, ("-"))
    return world

def transfer_item(source, target, item):
    for y in range (WORLD_HEIGHT*10):
        for x in range(WORLD_WIDTH*10):
            if item in source:
                source.remove(item)
                target.append(item)
            return source, target
