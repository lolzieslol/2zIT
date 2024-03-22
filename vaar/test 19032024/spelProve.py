import pygame
import sys
from spelProveKlasser import *

'''
Feilmelding på at Surface'n ikke er surface, men den er det. Finner ikke feilen.
'''

#Kilde: https://stackoverflow.com/questions/18948981/do-something-every-x-milliseconds-in-pygame
# (ikke i bruk, kommentert ut)
def main():
    pygame.init()
    # windowObject = pygame.display.set_mode((600, 400))
    
    # Creating a window to "draw" our content
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
    
    clock = pygame.time.Clock()

    player = Player(screen)

    enemy = Enemy(screen,10,10,2)
    
    THEEVENT = pygame.USEREVENT
    t = 10_000 #ms
    
    while True:
        # pygame.quit()
        # sys.exit()
        pressed_keys = pygame.key.get_pressed()

        # Checks if the user has closed the window every time any user input happens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed_keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if pressed_keys[pygame.K_SPACE]:
                player.killNearby(enemy)

        for e in pygame.event.get():
            if e.type == THEEVENT: 
                enemy = Enemy(10,23,2)

        screen.fill((0, 0, 0))
        player.move(pygame.key.get_pressed())
        player.draw()
        if not enemy.dead:
            enemy.draw()
            enemy.moveTowardsPlayer(player)
    
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()