import pygame, sys, os
from pygame.locals import *

#SETUP CONST
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 40

#INIT
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('MyGestureApp')

#VARIABLES
pos_to_draw = []

while True:
    for event in pygame.event.get():
        #QUIT IN CASE OF PRESSING RED X IN WINDOW OR ESC
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        
        #CHECK CURRENT POSITION OF MOUSE CURSOR
        pos = list(pygame.mouse.get_pos())

        if event.type == MOUSEBUTTONDOWN:
            pos_to_draw.append(pos)

        if event.type == MOUSEBUTTONUP:
            pos_to_draw.clear()
        print(pos_to_draw)
    pygame.display.update()
    mainClock.tick(FPS)
