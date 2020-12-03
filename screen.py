import pygame

from constants import *
from world import get_room


def create_screen(world):
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((board_width, board_height + COOKIE_RADIUS * 4))
    pygame.display.set_caption("End the Virus")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load('fondjeu.png')
    # background.fill((255, 255, 255))

    # for x in range(WORLD_WIDTH):
    #     for y in range(WORLD_HEIGHT):
    #         if bool(x % 2) == bool(y % 2):

    #             color = (200, 200, 200)
    #         else:
    #             color = (250, 250, 250)

    #         pygame.draw.rect(
    #             background,
    #             color,
    #             [
    #                 x * ROOM_SIZE,
    #                 y * ROOM_SIZE,
    #                 ROOM_SIZE,
    #                 ROOM_SIZE,
    #             ],
    #         )

    return screen, background


def update_screen(screen, background, world, pos,virusx, virusy, inventory):
    #player_x, player_y = player
    screen.blit(background, (0, 0))
    player(screen,pos, ROOM_SIZE)
    virus(screen,virusx, virusy)
    

    # couleur (red, green, blue)
    # screen.blit(player_image, player)
    # pygame.draw.rect(
    #     screen,
    #     (224, 64, 64),
    #     [
    #         player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
    #         player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
    #         PLAYER_SIZE,
    #         PLAYER_SIZE,
    #     ],
    # )

    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "cookie" in get_room(world, x, y):
                xy = x,y
                masque(screen,xy, ROOM_SIZE)
                # pygame.draw.circle(
                #     screen,
                #     yellow,
                #     (
                #         x * ROOM_SIZE + ROOM_SIZE - COOKIE_RADIUS * 2,
                #         y * ROOM_SIZE + ROOM_SIZE - COOKIE_RADIUS * 2,
                #     ),
                #     COOKIE_RADIUS,
                # )

    x = 10
    for item in inventory:
        y = WORLD_HEIGHT * ROOM_SIZE + COOKIE_RADIUS * 2
        pygame.draw.circle(
            screen,
            (250, 180, 40),
            (x, y),
            COOKIE_RADIUS,
        )

        x += COOKIE_RADIUS * 4

    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
