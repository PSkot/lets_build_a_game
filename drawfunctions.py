#### Module for easily drawing basic pygame objects ####

#Import libraries
import pygame
import numpy as np

pygame.init()


### Drawing functions ###
def draw_surface(win, marginSize = 50, borderSize = 10, screenWidth = 500, screenHeight = 500, marginColor = (0,0,0), borderColor = (0,0,0), boardColor = (0,0,0)):
    win.fill(marginColor)
    pygame.draw.rect(win, borderColor, (marginSize, marginSize, borderSize*2 + screenWidth, borderSize*2 + screenHeight))
    pygame.draw.rect(win, boardColor, (marginSize+borderSize, marginSize + borderSize, screenWidth, screenHeight))


def draw_circle(win, col, x, y, radius):
    pygame.draw.circle(win, (col), (x, y), radius)

def draw_rect(win, col, x, y, len, wid):
    pygame.draw.rect(win, col, (x, y, len, wid))

### Collission ###
def collision(x1, y1, x2, y2, object1Type = 'circle', object2Type = 'circle', object1Dimensions = (), object2Dimensions = ()):
    if object1Type == 'circle':
        if object2Type == 'circle':
            distX = x1 - x2
            distY = y1 - y2
            distance = np.sqrt((distX*distX) + (distY * distY))
            if distance < object1Dimensions + object2Dimensions:
                return True
            else:
                return False

        if object2Type == 'rect':
            pass

    elif object1Type == 'rect':
        pass
    elif object1Type == 'foo':
        return "bar"

    else:
        return print("Please specify a valid object type for object 1")



### Display game update ###
def display_update(*args, **kwargs):
    for arg in args:
        arg

    pygame.display.update()
