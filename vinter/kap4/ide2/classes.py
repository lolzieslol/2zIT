import pygame as pg
from pygame.locals import (K_w,K_a,K_s,K_d)

class Ball:
    def __init__(self,radius,windowObject,x,y,speed_x,speed_y):
        self.radius = radius
        self.windowObject = windowObject
        
        self.speed_x : float= speed_x
        self.speed_y : float= speed_y
        
        self.x : float = x
        self.y : float = y
        
    def DrawSelf(self):
        '''Makes the Ball appear in the window'''
        pg.draw.circle(self.windowObject, (255, 69, 0), (self.x, self.y), self.radius) 

    
    def MoveSelfAtAGivenSpeed(self,direction : list):
        '''Moves the Ball at the speed given in initialization, in the x and/or y direction'''
        assert("x" in direction or "y" in direction)
        
        if "x" in direction:
            if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.windowObject.get_width()):
                self.speed_x = -self.speed_x
    
            self.x += self.speed_x
            
        if "y" in direction:
            if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.windowObject.get_width()):
                self.speed_y = -self.speed_y
        
            self.y += self.speed_y
            
    def move(self,key):
        '''Moves the Ball depending on which key is pressed'''
        
        if key[K_w]: #when the W key is pressed
            self.y -= self.speed_y  #moves up
        if key[K_s]: #when the S key is pressed
            self.y += self.speed_y #moves down
        if key[K_a]: #when the A key is pressed
            self.x -= self.speed_x #moves left
        if key[K_d]: #when the D key is pressed
            self.x += self.speed_x #moves right
            