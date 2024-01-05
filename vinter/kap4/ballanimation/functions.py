from math import sqrt 

def findDistancePythagoras(obj1, obj2):
    #the Pythagorean theorem, h**2 = k1**2 + k2**2
    
    xDistanceSquared = (obj1.x - obj2.x)**2  #calculates the line and squares it
    yDistanceSquared = (obj1.y - obj2.y)**2  #calculates the line and squares it
    Distance = sqrt( xDistanceSquared + yDistanceSquared) #finds the hypotenuse 

    return Distance