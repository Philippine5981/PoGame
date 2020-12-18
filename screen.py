import pygame
import time
from constants import *
from world import get_room


def create_screen():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((board_width, board_height))
    pygame.display.set_caption("End the Virus")
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load('fondjeu.jpeg')

    return screen, background


def update_screen(screen, background, world, pos,virusx, virusy, inventory,solx,soly,batiment_image,batimentx,batimenty):
    #player_x, player_y = player
    screen.blit(background, (0, 0))
    #pour faire apparaitre le 1er batiment
    batiment(batiment_image,screen, batimentx, batimenty)
    #Pour faire apparaitre la 2eme image de baitment (qui va permettre de faire bouger le fond)
    batiment(batiment_image,screen, batimentx + 18 * ROOM_SIZE, batimenty)
    #Pour faire apparaitre le sol indépendemment des batiments 
    sol(screen, solx, soly)
    #faire apparaitre les virus
    virus(screen,virusx, virusy, virus_width,virus_height)
    #faire apparaitre le joueur
    player(screen,pos, ROOM_SIZE)
    #Faire apparaitre les scores
    score(inventory,screen)
    
    #Pour faire apparaitre les différents éléments (à l'aide de la fonction create_world() qui va les faire apparaitre aléatoirement)
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "masque" in get_room(world, x, y):
                xy = x,y
                masque(screen,xy, ROOM_SIZE)
            
            if "gel" in get_room(world,x,y):
                xy = x,y
                gel(screen,xy, ROOM_SIZE)
            
            if "gants" in get_room(world,x,y):
                xy = x,y
                gants(screen,xy, ROOM_SIZE)
            
            if "vaccin" in get_room(world,x,y):
                xy = x,y
                vaccin(screen,xy, ROOM_SIZE)

     

    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()

