# Quelques constantes qui nous seront utiles pour garder notre programme lisible ...
import pygame
pygame.init()

def load_image(imagename):
    return pygame.image.load(imagename)

WORLD_WIDTH = 16
WORLD_HEIGHT = 12
ROOM_SIZE = 54
PLAYER_SIZE = 16

fps = 40  #les images par secondes de notre jeu aka sa fuildité
ani = 3   #les cycles d'animation
main = True
ALPHA = (100, 188, 70) # la couleur du fond du png personnage

available_items = ["masque", "gel_hydro"]
inventory = []
font = pygame.font.SysFont(None, 48)

startimage = load_image('entree.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = WORLD_WIDTH*ROOM_SIZE/2
startimagerect.centery = WORLD_HEIGHT*ROOM_SIZE/2
