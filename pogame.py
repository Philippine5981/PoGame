import pygame

from constants import *
from screen import create_screen, update_screen
from world import *
import sys     # let  python use your file system

pygame.init()



def drawtext(text, font, surface, x, y):     #to display text on the screen
    textobj = font.render(text, 1, 'white')
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 4):
            img = pygame.image.load('bonhomme' + str(i) + '.png')
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 2*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 2*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

class Etage(pygame.sprite.Sprite):
    def __init__(self, posx, posy, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('plateforme.png').convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

def waitforkey():
    while True :                                        #to wait for user to start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:     #to terminate if the user presses the escape key
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return


screen = pygame.display.set_mode((WORLD_WIDTH*ROOM_SIZE, WORLD_HEIGHT*ROOM_SIZE))
screen.blit(startimage, startimagerect)
pygame.display.update()
waitforkey()


def main():
    # Création du "monde" tel que nous le définissons
    world = create_world(WORLD_WIDTH,WORLD_HEIGHT)
    # Création des surfaces de dessin
    screen,background, backgroundbox = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur

    player=Player()
    player.rect.x=0
    player.rect.y= 520
    player_list=pygame.sprite.Group()
    player_list.add(player)
    steps=10
    #player= player()
    #player.rect.x = 0
    #player.rect.y = 0
    #player_list = pygame.sprite.Group()
    #player_list.add(player)


    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background,backgroundbox, player, player_list)
    #update_screen(screen, background,backgroundbox, world, player_list)

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
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    # L'utilisateur a appuyé sur "Q", pour Quitter.
                    # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va
                    # se terminer.
                    running = False

            #Pour que le joueur puisse se déplacer avec les fleches
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        main = False
                elif event.key == pygame.K_LEFT:
                    if player.rect.x > 0:
                        player.control(-steps, 0)
                elif event.key == pygame.K_RIGHT:
                    if player.rect.x < WORLD_WIDTH * ROOM_SIZE - 10:
                        player.control(steps, 0)
                elif event.key == pygame.K_UP:
                    if player.rect.y > 0:
                        player.control(0, -steps)
                elif event.key == pygame.K_DOWN:
                    if player.rect.y < WORLD_HEIGHT * ROOM_SIZE - 10:
                        player.control(0, steps)

                #Pour ramasser objet ou enlever de l'inventaire
                elif event.key == pygame.K_x:
                    if not world[index]:
                        print("No object found")
                    else:
                        print("You have taken ", {world[index][0]}, "from the ground")
                        transfer_item(world[index], inventory, world[index][0])
                        print("ground:", world[index], "inventory: ", inventory)
                elif event.key == pygame.K_w:
                    if not inventory:
                        print("You have nothing in your inventory")
                    else:
                        print("You've put ", {inventory[0]}, "down")
                        transfer_item(inventory, world[index],inventory[0])
                        print("ground:", world[index], "inventory:", inventory)


#                if event.key == pygame.K_x:
#                    if len(inventaire) < 6:
#                        inventaire.append("someItem")
#                    else:
#                        print("No inventory space")

#                if event.key == pygame.K_w:
#                    inventaire.pop()
#                if event.key == pygame.K_c:
#                    print(inventaire)


            #Pour que le joueur s'arrete au bon endroit
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if player.rect.x > 0:
                        player.control(steps, 0)
                        index = get_index(player.rect.x, player.rect.y)
                        print("sol:", world[index], "inventaire :", inventory)
                if event.key == pygame.K_RIGHT:
                    if player.rect.x < WORLD_WIDTH * ROOM_SIZE - 10:
                        player.control(-steps, 0)
                        index = get_index(player.rect.x, player.rect.y)
                        print("sol:", world[index], "inventaire :", inventory)
                if event.key == pygame.K_UP:
                    if player.rect.y > 0:
                        player.control(0, steps)
                        index = get_index(player.rect.x, player.rect.y)
                        print("sol:", world[index], "inventaire :", inventory)
                if event.key == pygame.K_DOWN:
                    if player.rect.y < WORLD_HEIGHT * ROOM_SIZE - 10:
                        player.control(0, -steps)
                        index = get_index(player.rect.x, player.rect.y)
                        print("sol:", world[index], "inventaire :", inventory)

#ce que j'ai fait comme dans le cours: (mais j'ai voulu tenter de mieux pouvoir faire avancer mon
#joueur et de maniere plus naturelle avec 3 images comme vous pouvez le voir au dessus)
                # elif event.key == pygame.K_UP:
                #     if player[1] > 0:
                #         player = (player[0], player[1] - 1)
                # elif event.key == pygame.K_DOWN:
                #     if player[1] < WORLD_HEIGHT - 1:
                #         player = (player[0], player[1] + 1)
                # elif event.key == pygame.K_RIGHT:
                #     if player[0] < WORLD_WIDTH - 1:
                #         player = (player[0] + 1, player[1])
                # elif event.key == pygame.K_LEFT:
                #     if player[0] > 0:
                #         player = (player[0] - 1, player[1])

        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background,backgroundbox, player, player_list)
        #update_screen(screen, background,backgroundbox, world, player_list)

        clock.tick(fps)


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
