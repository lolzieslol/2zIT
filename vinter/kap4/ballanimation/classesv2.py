import pygame as pg
class Ball:
    def __init__(self,radius,windowObject,x,y,speed_x,speed_y):
        
        self.radius = radius
        self.windowObject = windowObject
        
        self.speed_x : float= speed_x
        self.speed_y : float= speed_y
        
        self.x : float = x
        self.y : float = y
        
    def DrawSelf(self):
        pg.draw.circle(self.windowObject, (255, 69, 0), (self.x, self.y), self.radius) 

    
    def MoveSelfAtAGivenSpeed(self,direction : list):
        
        assert("x" in direction or "y" in direction)
        
        if "y" in direction:
            if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.windowObject.get_width()):
                self.speed_x = -self.speed_x
    
                self.x += self.speed_x
            
        if "x" in direction:
            if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.windowObject.get_width()):
                self.speed_y = -self.speed_y
        
                self.y += self.speed_y

        #funker ikke