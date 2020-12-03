#inventaire de nos définitions
import pygame
import time

# Constantes Nécessaire

# CodeCouleurs en RGB
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (250, 180, 40)

def load_image(imagename):
    return pygame.image.load(imagename)

def texte_obj(texte, font):
    texteSurface = font.render(texte, True, black)
    return texteSurface, texteSurface.get_rect()

def afficher_message(texte, screen,screenwidth, screenheight):
    texteGrand = pygame.font.Font('freesansbold.ttf', 20)
    texteSurface, texteRectangle = texte_obj(texte, texteGrand)
    texteRectangle.center = ((screenwidth/2), (screenheight/2)) 
    screen.blit(texteSurface, texteRectangle)

    pygame.display.update()
    time.sleep(2)

def waitforkey():
    while True :                                        #to wait for user to start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:     #to terminate if the user presses the escape key
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return

player_image = load_image('Bonhomme1.png')
virus_image= load_image('virus.png')
mask_image = load_image('masque.png')

def player(screen,position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(player_image,(position_screen))

def virus(screen,virusx, virusy):
    screen.blit(virus_image,(virusx,virusy))
    #pygame.draw.rect(screen, green, [virusx, virusy, 54, 54])



def masque(screen,position, taille):
    position_screen = [position[0]*taille,position[1]*taille]
    screen.blit(mask_image,(position_screen))

def victoire(screen, screenwidth, screenheight):
    afficher_message('Bravo tu as vaincu le virus!',screen, screenwidth, screenheight)

def mort(screen, screenwidth, screenheight):
    afficher_message('Tu as été contaminé!',screen, screenwidth, screenheight)
    
