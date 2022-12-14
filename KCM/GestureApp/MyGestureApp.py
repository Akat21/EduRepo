import pygame, sys, os
from pygame.locals import *
import numpy as np

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
mouse_clicked = False

gesture_code = []
prev_mnem = '0'
mnem = ""
A = -1
B = -1


def DirectionRecognition(A, B, mnem):
    if A[0] > B[0]:
        mnem = "L"
    elif A[0] < B[0]:
        mnem = "R"
    
    if A[1] < B[1]:
        mnem += "D"
    elif A[1] > B[1]:
        mnem += "U"
    return mnem


while True:
    for event in pygame.event.get():
        #QUIT IN CASE OF PRESSING RED X IN WINDOW OR ESC
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        
        #CHECK CURRENT POSITION OF MOUSE CURSOR
        pos = list(pygame.mouse.get_pos())
        
        ##MANAGE MOUSEUP AND MOUSEDOWN
        if event.type == MOUSEBUTTONDOWN:
            mouse_clicked = True
            pos_to_draw.append(pos)
            if A == -1:
                A = pos
            else:
                A = B

        if event.type == MOUSEBUTTONUP:
            mouse_clicked = False
            B = pos
            
            mnem = DirectionRecognition(A, B, mnem)
            
            if mnem not in gesture_code:
                gesture_code.append(mnem)
                prev_mnem = mnem
                
            print(gesture_code)
            mnem = ""
            A, B = -1, -1
            gesture_code.clear()
            pos_to_draw.clear()
            windowSurface.fill((0,0,0))

        #DRAW LINES
        if mouse_clicked == True:
            pos_to_draw.append(pos)

        if len(pos_to_draw) > 2:
            for i in range(len(pos_to_draw)-1):
                pygame.draw.line(windowSurface, 'white', pos_to_draw[i], pos_to_draw[i+1], 1)

        # print(pos_to_draw)
    pygame.display.update()
    mainClock.tick(FPS)