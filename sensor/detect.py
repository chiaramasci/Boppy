import pygame
import envirophat
import time, sys

envirophat.leds.on()
pygame.init()
pygame.font.init()
pygame.display.set_caption('Envirophat Colour Sensor Output')
while True:
    background = envirophat.light.rgb()
    screen = pygame.display.set_mode((400,400))
    screen.fill((background))
    myfont = pygame.font.Font(None, 45)
    colour = myfont.render(str(background),1,(0,0,0))
    screen.blit(colour, (0,0))
    pygame.display.update()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
