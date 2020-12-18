#inventaire de nos définitions
import pygame
import time

# Constantes Nécessaire
clock = pygame.time.Clock()
WORLD_WIDTH = 16
WORLD_HEIGHT = 12
ROOM_SIZE = 54
board_width= WORLD_WIDTH*ROOM_SIZE
board_height=WORLD_HEIGHT*ROOM_SIZE

# CodeCouleurs en RGB
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red= (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)

blue = (0,0,255)
yellow = (250, 180, 40)

#Pour mettre une image
def load_image(imagename):
    return pygame.image.load(imagename)

# Banque d'images
player_image = load_image('Bonhomme1.png')
virus_image= load_image('virus.png')
virus_gameover = load_image('virusgo.png')
mask_image = load_image('masque.png')
gel_image = load_image('gelhydro.png')
gants_image = load_image('gants.png')
vaccin_image = load_image('vaccin.png')
batiment_image = load_image('batiment.png')
sol_image = load_image('sol.png')



#Pour chaque texte que j'affiche
def texte_obj(texte, font, color):
    texteSurface = font.render(texte, True, color)
    return texteSurface, texteSurface.get_rect()

#Afficher message pour la mort et la victoire (dont les fonctions sont plus bas)
def afficher_message(texte, color, screen,screenwidth, screenheight, size):
    texteGrand = pygame.font.Font('freesansbold.ttf', size)
    texteSurface, texteRectangle = texte_obj(texte, texteGrand, color)
    texteRectangle.center = ((screenwidth/2), (screenheight/2)) 
    screen.blit(texteSurface, texteRectangle)

    pygame.display.update()
    time.sleep(2)

#Pour compter les points gaganés - les points changent en fonction des éléments attrapés
def score(compter, screen):
    font = pygame.font.Font('freesansbold.ttf',15)
    textemasque = font.render("Score: "+str((compter).count("masque")*10+(compter).count("gel")*25+(compter).count("gants")*50+(compter).count("vaccin")*500), True, black)
    screen.blit(textemasque,(54/4,54/4))

#Pour l'image de start
def waitforkey():
    while True :                           #Pour attendre que l'utilisateur commence
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:     #pour terminer quand le joueur appuie sur 'quit'
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return

def player(screen,position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(player_image,(position_screen))

def virus(screen,virusx, virusy, width, height):
    screen.blit(virus_image,(virusx*width,virusy*height, width, height))
    #pygame.draw.rect(screen, color, [virusx*width, virusy*height, width, height])

def batiment(batiment_image, screen, batimentx, batimenty):
    screen.blit(batiment_image,(batimentx,batimenty))

def sol(screen, solx, soly):
    screen.blit(sol_image, (solx, (soly*ROOM_SIZE), ROOM_SIZE, ROOM_SIZE))

def masque(screen, position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(mask_image,(position_screen))

def gel(screen, position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(gel_image,(position_screen))

def gants(screen, position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(gants_image,(position_screen))

def vaccin(screen, position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(vaccin_image,(position_screen))

def victoire(screen, screenwidth, screenheight, size, compter):
    afficher_message('Bravo tu as vaincu le virus!',green, screen, screenwidth, screenheight, size)

def mort(screen, screenwidth, screenheight):
    screen.blit(virus_gameover,(screenwidth/4,screenheight/4,400,302))
    afficher_message('GAME OVER',red, screen, screenwidth, screenheight-25, 50)
    afficher_message('Tu as été contaminé!',white, screen, screenwidth, screenheight+40,21)    