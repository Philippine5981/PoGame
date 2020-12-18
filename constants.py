from pogameDef import *

# Quelques constantes qui nous seront utiles pour garder notre programme lisible ...
WORLD_WIDTH = 16
WORLD_HEIGHT = 12
ROOM_SIZE = 54
PLAYER_SIZE = 16

# CodeCouleurs en RGB
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (250, 180, 40)

# Constant à travers le code
board_width= WORLD_WIDTH*ROOM_SIZE
board_height=WORLD_HEIGHT*ROOM_SIZE

# Personnage
deplacement_x = 0
deplacement_y = 0

# Virus
virus_width = ROOM_SIZE
virus_height = ROOM_SIZE

# Placement de l'Image de START
jeuIcon = load_image('jeuIcon.png')
startimage = load_image('entree.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = board_width/2
startimagerect.centery = board_height/2