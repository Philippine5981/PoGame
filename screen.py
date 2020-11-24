import pygame
import os

from constants import *


def create_screen(world):
    # Initialise screen
    pygame.init()
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE
    screen = pygame.display.set_mode((board_width, board_height))
    pygame.display.set_caption("End the Virus")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load('fondjeu.png')
    backgroundbox = screen.get_rect()

    # for x in range(WORLD_WIDTH):
    #     for y in range(WORLD_HEIGHT):
    #         if bool(x % 2) == bool(y % 2):
    #
    #             color = (200, 200, 200)
    #         else:
    #             color = (250, 250, 250)
    #
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

    return screen, background, backgroundbox


#def update_screen(screen, background, backgroundbox, world, player):
def update_screen(screen, background, backgroundbox, player, player_list):

    #player_x, player_y = player
    screen.blit(background, backgroundbox)
    player.update()
    player_list.draw(screen)

    # couleur (red, green, blue)
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

    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
