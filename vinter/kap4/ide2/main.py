'''
Game where you move a Ball with WASD.

things you can do:
- move with WASD
- end game with ESC or by hitting the x

rules:
- the ball can't move outside the window

classes:
- player ball: can be moved with keys
- enemy ball

'''
import pygame
from pygame.locals import K_ESCAPE
from classes import PlayerBall as PlayerBallClasss
from classes import EnemyBall as EnemyBallClass
# Initializing pygame
pygame.init()

clock = pygame.time.Clock()

# Creating a window to "draw" the content
WINDOW_WIDTH = 500 #pixels
WINDOW_HEIGHT = 500 #pixels
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

brus = pygame.image.load('brus.png') 

# makes a Ball-object
theBall : PlayerBallClasss = PlayerBallClasss(radius=20, windowObject=window,x=250, y=250, speed_x=3, speed_y=3)
enemyBall : EnemyBallClass = EnemyBallClass(radius=20, windowObject=window,x=50, y=50, speed_x=3, speed_y=3)

# repeat until the window is closed
continuing : bool = True
while continuing:
    
    
    pressed_keys = pygame.key.get_pressed()
    
    # Checks if the user has closed the window every time any user input happens
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuing = False
        if pressed_keys[K_ESCAPE]:
            continuing = False

        
    # Colors the background blue
    window.fill((10, 129, 210))

    # Draws the balls
    theBall.DrawSelf()   
    enemyBall.DrawSelf()
    
    # theBall.blit(brus,(188,189))
    # pygame.Surface.blit(theBall,brus)
    #TODO: #3 få ballen til å se ut som en brusflaske
    # theBall.MoveSelfAtConstantSpeed(["x","y"])
    # The playerball is moved by the user with WASD
    theBall.MoveControlled(pressed_keys)

    # Updates all visual content
    pygame.display.flip() #update
    
    # Makes time consistant regardless of computer and background tasks
    clock.tick(60)

# Quits pygame
pygame.quit()