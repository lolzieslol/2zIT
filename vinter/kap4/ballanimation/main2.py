from classesv2 import Ball as BallClass
import pygame as pg

# Initializing pygame
pg.init()

# Creating a window to "draw" our content
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# makes 2 Ball-objects
Ball1 : BallClass = BallClass(radius=20, windowObject=window,x=250, y=250, speed_x=0.1,speed_y=0.1)
Ball2 : BallClass = BallClass(radius=20, windowObject=window,x=200, y=200, speed_x=0.2,speed_y=0.1)

# repeat until the window is closed
continuing : bool = True
while continuing:

    # Checks if the user has closed the window every time any user input happens
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuing = False

    # Colors the background light blue
    window.fill((135, 206, 235))

    # Draws and moves the balls
    Ball1.DrawSelf() #draw / makes appear onscreen
    Ball1.MoveSelfAtAGivenSpeed(["x","y"]) #move based on speed defined in __init__
    
    Ball2.DrawSelf() #draws / makes appear onscreen
    Ball2.MoveSelfAtAGivenSpeed(["x","y"]) #move based on speed defined in __init__

    # Updates all visual content
    pg.display.flip()

# Quits pygame
pg.quit()