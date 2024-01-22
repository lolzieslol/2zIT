'''


'''
import pygame
from classes import Ball as BallClass
# Initializing pygame
pygame.init()

# Creating a window to "draw" our content
WINDOW_WIDTH = 500 #pixels
WINDOW_HEIGHT = 500 #pixels
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

brus = pygame.image.load('brus.png') 

# makes a Ball-object
theBall : BallClass = BallClass(radius=20, windowObject=window,x=250, y=250, speed=0.1)


# repeat until the window is closed
continuing : bool = True
while continuing:
    # Checks if the user has closed the window every time any user input happens
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuing = False

    # Colors the background blue
    window.fill((10, 129, 210))

    
    # Draws and moves the ball
    theBall.DrawSelf()
    
    theBall.blit(brus,(50,50))

    # Updates all visual content
    pygame.display.flip() #update

# Quits pygame
pygame.quit()