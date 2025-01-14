'''
kopiert fra:
https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/4-grafisk-brukergrensesnitt/4a-spill-og-animasjoner-med-pygame/enkel-grafikk-med-pygame
'''


import pygame as pg

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
            
    # Tegner en sirkel
    pg.draw.circle(vindu, (255, 0, 0), (100, 250), 50) #farge, sentrumets kordinat, radius
    
        # Tegner et rektangel
    pg.draw.rect(vindu, (0, 255, 0), (200, 250, 70, 90))
    
        # Tegner en ellipse
    pg.draw.ellipse(vindu, (0, 0, 255), (300, 250, 90, 60))
    
        # Tegner en linje
    pg.draw.line(vindu, (200, 0, 200), (400, 100), (400, 400), 5)
    
    pg.display.flip()
    

pg.quit() #SPM: gjør denne noe i praksis? 