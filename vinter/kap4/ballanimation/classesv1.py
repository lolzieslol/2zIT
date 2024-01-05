#main 1
import pygame as pg
class Ball:
    def __init__(self,radius,windowObject,x,y,speed):
        
        self.radius = radius
        self.windowObject = windowObject
        
        self.x : float = x
        self.y : float = y
        self.speed : float= speed
        
    def DrawSelf(self):
        pg.draw.circle(self.windowObject, (255, 69, 0), (self.x, self.y), self.radius) 

    
    def MoveSelf(self):
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.windowObject.get_width()):
            self.speed = -self.speed
    
        self.x += self.speed