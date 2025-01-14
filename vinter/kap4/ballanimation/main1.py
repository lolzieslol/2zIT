'''
based on:
https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/4-grafisk-brukergrensesnitt/4a-spill-og-animasjoner-med-pygame/en-enkel-animasjon

structure:
classes (file):
- ball
--methods:
-- DrawSelf
-- MoveSelfAtAGivenSpeed

functions (file):
- findDistance 

main -> one ball moving side to side
main2 -> multiple balls
'''

from classesv1 import Ball as BallClass
import pygame as pg

# Initializing pygame
pg.init()

# Creating a window to "draw" our content
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# makes a Ball-object
theBall : BallClass = BallClass(radius=20, windowObject=window,x=250, y=250, speed=0.1)

# repeat until the window is closed
continuing : bool = True
while continuing:

    # Checks if the user has closed the window every time any user input happens
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuing = False

    # Colors the background light blue
    window.fill((135, 206, 235))

    # Draws and moves the ball
    theBall.DrawSelf()
    theBall.MoveSelf()

    # Updates all visual content
    pg.display.flip()

# Quits pygame
pg.quit()