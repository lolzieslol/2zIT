import pygame as pg
class Ball:
    def __init__(self,radius,windowObject,x,y,speed):
        
        self.radius = radius
        self.windowObject = windowObject
        
        self.speed : float= speed
        
        self.x : float = x
        self.y : float = y
        
    def DrawSelf(self):
        pg.draw.circle(self.windowObject, (255, 69, 0), (self.x, self.y), self.radius) 

    
    def MoveSelfAtAGivenSpeed(self):
        
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.windowObject.get_width()):
            self.speed = -self.speed
    
        self.x += self.speed