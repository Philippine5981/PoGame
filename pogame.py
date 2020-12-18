import pygame
from constants import *
from screen import create_screen, update_screen
from world import *
import random
import threading

pygame.init()

def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target

#Pour faire apparaitre l'image d'acceuil du jeu
screen = pygame.display.set_mode((board_width, board_height))

pygame.display.set_icon(jeuIcon)
screen.blit(startimage, startimagerect)
pygame.display.update()
waitforkey()

def main():
    # Lancer la musique du jeu
    pygame.mixer.init()
    pygame.mixer.music.load("ETV_TheSong.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

    # Création du "monde" tel que nous le définissons
    world = create_world("masque")
    inventory = []
    test = True #test pour savoir si plus de masque
    #On dit que les tests sont faux pour ne pas qu'il les calculent
    test2 = False #test pour savoir si plus de gel
    test3 = False #test pour savoir si plus de gants
    masque_restant = 1
    gel_restant = 1
    gants_restant = 1

    # Création des surfaces de dessin
    screen, background = create_screen()

    # Création d'une horloge
    clock = pygame.time.Clock()

    #place du sol
    solx, soly = 0, 11

    #place du batiment
    batimentx, batimenty = 0, 0
    batiment_image = load_image('batiment.png')
    decor_compteur = 0

    # Variables joueur
    position = [0, 10]
    deplacement_x = 0
    deplacement_y = 0
    player(screen,position, ROOM_SIZE)
    
    # Variables virus
    virus_startx = 18
    virus_starty = random.randrange(0, WORLD_HEIGHT-2)
    virus(screen, virus_startx, virus_starty, virus_width, virus_height)
    virus_speed = 1

    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, position,virus_startx,virus_starty, inventory,solx,soly,batiment_image,batimentx,batimenty)
    score(inventory,screen)

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
                        #Quand tu restes appuyé il monte car -1
                        deplacement_y = -1   
                elif event.key == pygame.K_LEFT:
                    if position[0] > 0:
                        #Quand tu reste appuyé il va en arrière parce que -1
                        deplacement_x = -1
                elif event.key == pygame.K_RIGHT:
                    if position[0] < WORLD_WIDTH - 1:
                        #Quand tu reste appuyé il va en avant parce que +1
                        deplacement_x = 1

            elif event.type == pygame.KEYUP:
                # Une touche du clavier a été relachée.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    deplacement_x = 0
                    #Des que la touche est lachée, il fait que descendre tout le temps 
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    deplacement_y = 1
        
        #Combien de case le virus avance toutes les secondes
        virus_startx -= virus_speed
        # Deplacement fait qu'a chaque fois que le joueur reste appuyé sur une touche il ajoute tous les déplacements faits  
        position[0] += deplacement_x
        position[1] += deplacement_y

        #Pour que le décor avance : il recule de 16 places
        batimentx -= 16

        if batimentx <=-WORLD_WIDTH* ROOM_SIZE:
            #Quand la position x du batiment n'est plus dans la taille du monde, il repart en avant sur la position x=18 pour pouvoir repartir.
            batimentx=18

        # cette partie va continuellement vérifier si le joueur est sur une case comportant un objet, si oui, il le prend automatiquement
        room = get_room(world, position[0], position[1])
        if len(room) > 0:
            item = room[0]
            room, inventory = transfer_item(room, inventory, item)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('pointsound.mp3'))

        if test == True:
            #Va regarder dans toutes les cases de world et compte le nombre d'éléments
            masque_restant = sum(x.count("masque") for x in world)
        if masque_restant == 0:
            world = create_world("gel") #Maintenant qu'ils sont créés, il peut commencer à calculer le nombre de gels
            masque_restant = 1
            test = False #Si le test est faux, il arrete de calculer le nombre de masque 
            test2 = True #Et donc on dit que le test 2 est vrai pour qu'il commence à calculer 
            virus_speed = 1 # La vitesse du virus augmente
            batiment_image = load_image('decor2.png') #Changement de fond
        
        #et ainsi de suite jusqu'au vaccin
        if test2 == True:
            gel_restant = sum(x.count("gel") for x in world)
        if gel_restant == 0:
            world = create_world("gants")
            gel_restant = 1
            test2 = False
            test3 = True
            virus_speed =2
            batiment_image = load_image('decor3.png')
        
        if test3 == True:
            gants_restant = sum(x.count("gants") for x in world)
        if gants_restant == 0:
            world[50].append("vaccin")
            gants_restant = 1
            test3 = False
            virus_speed = 2
            batiment_image = load_image('decor4.png')
        
        #Les limites du monde
        if position[0]>WORLD_WIDTH-1:
            position[0] = WORLD_WIDTH-1
        elif position[0]<0:
            position[0] =0

        if position[1] > WORLD_HEIGHT-2:
            position[1] = WORLD_HEIGHT-2
        elif position[1]<0:
            position[1] =0
    
        #Des que le virus a dépassé le monde il retourne en avant à une place random
        if virus_startx < 0:
            virus_startx = 16
            #virus_startx =12
            virus_starty = random.randrange(0, WORLD_WIDTH-2)

        #Pour la collision entre le virus et le personnage
        if position[0] == virus_startx:
            if position[1] == virus_starty :
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('gameover.mp3'))
                mort(screen, board_width,board_height)
                alive = False
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, position,virus_startx,virus_starty, inventory,solx,soly,batiment_image,batimentx,batimenty)

        #Si il attrappe le vaccin il a gagné
        if sum(x.count("vaccin") for x in inventory) == 1:
            # Le joueur a gagné !
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('winsound.mp3'))
            victoire(screen,board_width,board_height, 50, inventory)
            running = False
            # break
        pygame.display.update()
        clock.tick(12)

# game_intro(screen, board_width, board_height, main())
# main()
# pygame.quit()
# quit()

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
