'''
Game where you move a Ball with WASD. You get points by moving your ball to the enemy ball

things you can do:
- move with WASD
- end game with ESC or by hitting the x

getting points:
if the two balls overlap you get points

rules:
- the ball can't move outside the window

classes:
- player ball: can be moved with keys
- enemy ball

sources:
Aschehoug Univers, IT 2, 4A Spill og animasjoner med PyGame, https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/4-grafisk-brukergrensesnitt/4a-spill-og-animasjoner-med-pygame/bevegelse-styrt-av-tastaturet
stackExchange https://gamedev.stackexchange.com/questions/101720/collision-detection-with-pygame

'''
import pygame
from pygame.locals import K_ESCAPE
from classes import PlayerBall as PlayerBallClasss
from classes import EnemyBall as EnemyBallClass
import functions as f

# Initializing pygame
pygame.init()

clock = pygame.time.Clock()

# Creating a window to "draw" the content
WINDOW_WIDTH = 500 #pixels
WINDOW_HEIGHT = 500 #pixels
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

brus = pygame.image.load('brus.png') 

font = pygame.font.SysFont("Arial", 24)

# makes Ball-objects
theBall : PlayerBallClasss = PlayerBallClasss(radius=20, windowObject=window,x=250, y=250, speed_x=3, speed_y=3)
enemyBall : EnemyBallClass = EnemyBallClass(radius=20, windowObject=window,x=50, y=50, speed_x=3, speed_y=3)


scoreSTR = "0"
    
# repeat until the window is closed
continuing : bool = True
while continuing:
    
    pressed_keys = pygame.key.get_pressed()
    
    # Checks if the user has closed the window every time any user input happens
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuing = False
        if pressed_keys[K_ESCAPE]:
            continuing = False

        
    # Colors the background blue
    window.fill((10, 129, 210))

    # Puts the coordinates of both balls on the screen
    coordinateSTR = f"Player: {theBall.x, theBall.y}, Enemy: {enemyBall.x, enemyBall.y}"
    coordinatesWritten = font.render(coordinateSTR, True, (50, 50, 50))
    window.blit(coordinatesWritten, (150, 20))
    
    
   
    # if scoreSTR == "0":
    #     print(a.x,a.y,a.w,a.h)
    
    # Shows the score, which is increased any time the player's ball and enemy have the same position
    if f.detectCollisions(theBall, enemyBall):
        # theBall.x,theBall.y,theBall.radius,theBall.radius,enemyBall.x,enemyBall.y,enemyBall.radius,enemyBall.radius
        scoreSTR = int(scoreSTR) + 1
        scoreSTR = str(scoreSTR)
    scoreWritten = font.render(scoreSTR, True, (50, 50, 50))
    window.blit(scoreWritten, (400, 60))
    
    #TODO: #5 gjøre at fienden kan kræsje i brusflasken
    
    
    
    # Draws the balls
    theBall.DrawSelf()   
    enemyBall.DrawSelf()
    
    a = window.blit(brus,(218,180))
    if f.detectCollisions(a,enemyBall):
        # a.x,a.y,a.w,a.h,enemyBall.x,enemyBall.y,enemyBall.radius,enemyBall.radius
        print("hi")
        f.crash(enemyBall)
        
    
    # pygame.Surface.blit(theBall,brus)
    #TODO: #3 få ballen til å se ut som en brusflaske
    enemyBall.MoveSelfAtConstantSpeed(["x","y"])
    # The playerball is moved by the user with WASD
    theBall.MoveControlled(pressed_keys)

    # Updates all visual content
    pygame.display.flip() #update
    
    # Makes time consistant regardless of computer and background tasks
    clock.tick(60)

# Quits pygame
pygame.quit()