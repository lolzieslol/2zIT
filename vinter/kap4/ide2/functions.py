import classes
import pygame

def detectCollisions(object1,object2):

    
    x1 = object1.x
    y1 = object1.y
    if  issubclass(type(object1),classes.Ball):
        w1 = object1.radius
        h1 = object1.radius
    elif type(object1) == pygame.rect.Rect: 
        w1 = object1.w
        h1 = object1.h
    else:
        print("error")
        print(type(object1))
    
    x2 = object2.x
    y2 = object1.y
    
    if issubclass(type(object2),classes.Ball):
        w2 = object2.radius
        h2 = object2.radius
    elif type(object2) == pygame.rect.Rect: 
        w2 = object2.w
        h2 = object2.h
    else:
        print("error")
    

    if x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2:
        return False

    elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2:
        return True

    elif x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
        return True

    elif x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2:
        return True

    else:
        return False

def crash(object1):
    ''' Turns around, speed is changed to the opposite direction'''
    object1.speed_x = - object1.speed_x
    object1.speed_y = - object1.speed_y