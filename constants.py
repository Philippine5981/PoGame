from pogameDef import *

# Quelques constantes qui nous seront utiles pour garder notre programme lisible ...
WORLD_WIDTH = 16
WORLD_HEIGHT = 12
ROOM_SIZE = 54
PLAYER_SIZE = 16
COOKIE_RADIUS = 4

# Constant à travers le code
board_width= WORLD_WIDTH*ROOM_SIZE
board_height=WORLD_HEIGHT*ROOM_SIZE

# Personnage
deplacement_x = 0
deplacement_y = 0

# Image de START
jeuIcon = load_image('jeuIcon.png')
startimage = load_image('entree.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = board_width/2
startimagerect.centery = board_height/4