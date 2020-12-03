import pygame
pygame.init()
from constants import *
from screen import create_screen, update_screen
from world import create_world, get_room
import random


def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target

#Pour faire apparaitre l'image d'acceuil du jeu

pygame.display.set_icon(jeuIcon)
screen = pygame.display.set_mode((board_width, board_height))
screen.blit(startimage, startimagerect)
pygame.display.update()
waitforkey()

def main():
    # Création du "monde" tel que nous le définissons
    world = create_world()
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    position = [0, 8]
    deplacement_x = 0
    deplacement_y = 0
    player(screen,position, ROOM_SIZE)
    inventory = []

    # Virus valeurs de début
    virus_startx = random.randrange(0, WORLD_WIDTH*ROOM_SIZE)
    virus_starty = -board_height
    virus(screen, virus_startx, virus_starty)
    virus_speed = 50

    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, position,virus_startx,virus_starty, inventory)
    clock.tick()

    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.
    while alive and running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier, par exemple).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # L'utilisateur souhaite fermer la fenêtre ou quitter par un autre moyen (menus ...).
                # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va se
                # terminer.
                running = False
            elif event.type == pygame.KEYDOWN:
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    # L'utilisateur a appuyé sur "Q", pour Quitter.
                    # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va
                    # se terminer.
                    running = False
                elif event.key == pygame.K_UP:
                    if position[1] > 0:
                        #position = [position[0], position[1] - 1]
                        deplacement_y = -1
                elif event.key == pygame.K_DOWN:
                    if position[1] < WORLD_HEIGHT - 1:
                        #position = [position[0], position[1] + 1]
                        deplacement_y = 1
                elif event.key == pygame.K_LEFT:
                    if position[0] > 0:
                        #position = [position[0] - 1, position[1]]
                        deplacement_x = -1
                elif event.key == pygame.K_RIGHT:
                    if position[0] < WORLD_WIDTH - 1:
                        #position = [position[0] + 1, position[1]]
                        deplacement_x = 1
                elif event.key == pygame.K_SPACE:
                    room = get_room(world, position[0], position[1])
                    if len(room) > 0:
                        item = room[0]
                        room, inventory = transfer_item(room, inventory, item)
            elif event.type == pygame.KEYUP:
                # Une touche du clavier a été relachée.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    deplacement_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    deplacement_y = 0
        virus_starty += virus_speed
        position[0] += deplacement_x
        position[1] += deplacement_y

        if position[0]>WORLD_WIDTH-1:
            position[0] = WORLD_WIDTH-1
        elif position[0]<0:
            position[0] = 0

        if position[1] > WORLD_HEIGHT-1:
            position[1] = WORLD_HEIGHT-1
        elif position[1] < 0:
            position[1] = 0

        if virus_starty > board_height:
            virus_starty = 0 - ROOM_SIZE
            virus_startx = random.randrange(0, board_height)
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, position,virus_startx,virus_starty, inventory)

        if position[1] < virus_starty + ROOM_SIZE:
            #print('y crossover')

            if position[0] > virus_startx and position[0] < virus_startx + ROOM_SIZE or position[0] + ROOM_SIZE > virus_startx and position[0] + ROOM_SIZE < virus_startx + ROOM_SIZE:
                #print('x crossover')
                alive = False
                mort(screen, board_width,board_height)

        if len(inventory) >= 10:
            print("you have won")
            # Le joueur a gagné !
            #victoire(screen,board_width,board_height)
            # break
        pygame.display.update()
        clock.tick(12)



if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
