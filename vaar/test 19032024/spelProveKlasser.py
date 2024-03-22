import pygame

class Creature:
    ''' A circular creature that can be drawn'''
    def __init__(self,screen,x,y,speed,color,):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = 15
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

class Player(Creature):
    ''' A moveable character'''
    def __init__(self,screen):
        super().__init__(screen,300,200,5,(240,200,90))
        
    def move(self, key):
        if key[pygame.K_w]: #when the W key is pressed
            #as long as the ball is below the top
            if not ((self.y - self.radius) <= 0):
                self.y -= self.speed #moves upwards
                
        if key[pygame.K_s]: #when the S key is pressed
            self.y += self.speed #moves downwards
            
        if key[pygame.K_a]: #when the A key is pressed
            self.x -= self.speed #moves left
                
        if key[pygame.K_d]: #when the D key is pressed
            self.x += self.speed #moves right
    
    def killNearby(self,enemy):
        # the when
        if enemy.x > 10 and enemy.y > 10:
            pass
        else:
            enemy.dead = True

class Enemy(Creature):
    ''' An enemy character'''
    def __init__(self,screen, x : int, y : int, speed : int, color=(255,255,255)):
        super().__init__(screen,x, y, speed,color)
        self.dead = False
    
    def moveTowardsPlayer(self,player):
        
        if player.x < self.x:
            self.x -= self.speed
        elif player.x > self.x:
            self.x += self.speed
        
        if player.y < self.y:
            self.y -= self.speed
        elif player.y > self.y:
            self.y += self.speed