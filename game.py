import pygame
import numpy as np
from random import randint, choice
from time import sleep
from drawfunctions import draw_surface, draw_circle, draw_rect, collision

pygame.init()

###### Glossary ######
# Enemy types: default
# Player types:
# Gun types:
######################

#Game info
name = "A funny game"
marginSize = 50
marginColor = (255, 0, 0)
borderSize = 10
borderColor = (0, 255, 0)
screenWidth = 500
screenHeight = 500
boardColor = (0, 0, 255)
playerSize = 20
playerLife = 3


win = pygame.display.set_mode((marginSize*2+borderSize*2+screenWidth, marginSize*2+borderSize*2+screenHeight))
clock = pygame.time.Clock()

#Arguments for drawing border
screenArgs = {
    'marginSize': marginSize,
    'borderSize': borderSize,
    'screenWidth': screenWidth,
    'screenHeight': screenHeight,
    'marginColor': marginColor,
    'borderColor': borderColor,
    'boardColor': boardColor
}

def lose_game():
    sleep(3)

def display_menu():
    pass

def display_update(me, enemies, bullets):
    draw_surface(win, **screenArgs)

    if me.life > 0:
        me.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    for bullet in bullets:
        bullet[0].draw(win)

    pygame.display.update()

class level(object):
    def __init__(self, map, levelNum):
        self.map = map
        self.levelNum = levelNum

class enemy(object):
    def __init__(self, x, y, type, size, col, dirX, dirY, pathLoop, gunSize, gunCol, gunType, gunLoc, gunDir, gunSpin):
        self.x = x
        self.y = y
        self.type = type
        self.size = size
        self.col = col
        self.dirX = dirX
        self.dirY = dirY
        self.pathLoop = pathLoop
        self.gunSize = gunSize
        self.gunCol = gunCol
        self.gunType = gunType
        self.gunLoc = gunLoc
        self.gunDir = gunDir
        self.gunSpin = gunSpin

    def draw(self, win):
        if self.type == 'default':
            draw_circle(win, self.col, self.x, self.y, self.size)
            draw_circle(win, self.gunCol, int(self.x+np.cos(self.gunLoc*self.gunDir)*self.size), int(self.y+np.sin(self.gunLoc*self.gunDir)*self.size), self.gunSize)



class trap(object):
    def __init__(self, x, y, type, size):
        self.x = x
        self.y = y
        self.type = type
        self.size = size

    def draw(self):
        pass

class coin(object):
    def __init__(self, x, y, type, size):
        self.x = x
        self.y = y
        self.type = type
        self.size = size

    def draw(self):
        pass

class upgrade(object):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw():
        pass

class player(object):
    def __init__(self, x, y, size, col, life, gunSize, gunCol, gunType, gunLoc, gunDir, gunSpin):
        self.x = x
        self.y = y
        self.size = size
        self.col = col
        self.life = life
        self.gunSize = gunSize
        self.gunCol = gunCol
        self.gunType = gunType
        self.gunLoc = gunLoc
        self.gunDir = gunDir
        self.gunSpin = gunSpin

    def draw(self, win):

        draw_circle(win, self.col, self.x, self.y, self.size)

        if self.gunType == 'default':
            gunX = int(self.x+np.cos(self.gunLoc*self.gunDir)*self.size)
            gunY = int(self.y+np.sin(self.gunLoc*self.gunDir)*self.size)
            draw_circle(win, self.gunCol, gunX, gunY, self.gunSize)

        for i in range(self.life):
            draw_circle(win, (120, 0, 120), (i+1)*30, 20, 10)

class shot(object):
    def __init__(self, x, y, size, type, col):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        self.col = col

    def draw(self, win):
        if self.type == 'default':
            draw_circle(win, self.col, self.x, self.y, self.size)

run = True

vel = 2
eVel = 1
gunLoc = 0
gunSpin = 5
gunSize = 5
gunColor = (0, 0, 0)
gunDir = 1
shootLoop = 0
shootVal = 20
bulletSpeed = 5
pathLoop = 0
pathVal = 30
hitLoop = 0
hitVal = 100
bullets = []
enemies = []

level = 1
me = player(
        marginSize + borderSize + screenWidth//2, marginSize + borderSize + screenHeight//2, playerSize, (155, 155, 0), playerLife,
        gunSize, gunColor, 'default', gunLoc, gunDir, gunSpin
        )

for _ in range(level):
    enemies.append(enemy(marginSize + borderSize + screenWidth//4, marginSize + borderSize + screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
    enemies.append(enemy(marginSize + borderSize + screenWidth - screenWidth//4, marginSize + borderSize + screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
    enemies.append(enemy(marginSize + borderSize + screenWidth//4, marginSize + borderSize + screenHeight - screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
    enemies.append(enemy(marginSize + borderSize + screenWidth - screenWidth//4, marginSize + borderSize + screenHeight - screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))


while run == True:

    clock.tick(80)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    #Create new enemies
    if len(enemies) == 0:
        level += 1
        if shootVal == 15:
            pass
        else:
            shootVal -= 5
        for _ in range(level):
            enemies.append(enemy(marginSize + borderSize + screenWidth//4, marginSize + borderSize + screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
            enemies.append(enemy(marginSize + borderSize + screenWidth - screenWidth//4, marginSize + borderSize + screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
            enemies.append(enemy(marginSize + borderSize + screenWidth//4, marginSize + borderSize + screenHeight - screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
            enemies.append(enemy(marginSize + borderSize + screenWidth - screenWidth//4, marginSize + borderSize + screenHeight - screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))

    #Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and me.x - playerSize - gunSize > marginSize + borderSize:
        me.x -= vel

    if keys[pygame.K_RIGHT] and me.x + playerSize + gunSize < marginSize + borderSize + screenWidth:
        me.x += vel

    if keys[pygame.K_UP] and me.y - playerSize - gunSize > marginSize + borderSize:
        me.y -= vel

    if keys[pygame.K_DOWN] and me.y + playerSize + gunSize < marginSize + borderSize + screenHeight:
        me.y += vel

    #Fire bullet
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletX = int(me.x+np.cos(me.gunLoc*me.gunDir)*me.size)
        bulletY = int(me.y+np.sin(me.gunLoc*me.gunDir)*me.size)
        coords = (np.cos(me.gunLoc), np.sin(me.gunLoc))
        bullets.append([shot(bulletX, bulletY, 3, 'default', (0, 0, 0)), coords])
        shootLoop = shootVal

    #Move bullets
    for bullet in bullets:
        bullet[0].x += int(bulletSpeed*bullet[1][0])
        bullet[0].y += int(bulletSpeed*bullet[1][1])

        try:
            if bullet[0].x >= borderSize + marginSize + screenWidth:
                bullets.remove(bullet)
            if bullet[0].x <= borderSize + marginSize:
                bullets.remove(bullet)
            if bullet[0].y <= borderSize + marginSize:
                bullets.remove(bullet)
            if bullet[0].y >= borderSize + marginSize + screenHeight:
                bullets.remove(bullet)

            for e in enemies:
                if collision(bullet[0].x, bullet[0].y, e.x, e.y, object1Dimensions = bullet[0].size, object2Dimensions = e.size):
                    bullets.remove(bullet)
                    enemies.remove(e)

        except ValueError:
            pass

    #Turn gun
    if me.gunLoc == 360:
        me.gunLoc = 0
    else:
        me.gunLoc += 0.005*me.gunSpin

    #Reposition enemies
    for e in enemies:

        if collision(me.x, me.y, e.x, e.y, object1Dimensions = me.size, object2Dimensions = e.size) and hitLoop == 0:
            me.life -= 1
            hitLoop = hitVal

        if e.pathLoop == 0:
            e.dirX = randint(-1, 1)
            e.dirY = randint(-1, 1)
            e.pathLoop = pathVal

        if e.x - e.size - e.gunSize - eVel > marginSize + borderSize:
            e.x += e.dirX*eVel
        else:
            e.dirX = randint(0, 1)

        if e.x + e.size + e.gunSize + eVel < marginSize + borderSize + screenWidth:
            e.x += e.dirX*eVel
        else:
            e.dirX = randint(-1, 0)

        if e.y - e.size - e.gunSize - eVel > marginSize + borderSize:
            e.y += e.dirY*eVel
        else:
            e.dirY = randint(0, 1)

        if e.y + e.size + e.gunSize + eVel < marginSize + borderSize + screenWidth:
            e.y += e.dirY*eVel
        else:
            e.dirY = randint(-1, 0)

        if e.pathLoop > 0:
            e.pathLoop -= 1

        if e.gunLoc == 360:
            e.gunLoc = 0
        else:
            e.gunLoc += 0.005*e.gunSpin

    #Decrement shoopLoop
    if shootLoop > 0:
        shootLoop -= 1

    if hitLoop > 0:
        hitLoop -= 1

    #Reset game if lost
    if me.life == 0:
        lose_game()
        vel = 2
        eVel = 1
        gunLoc = 0
        gunSpin = 5
        gunSize = 5
        gunColor = (0, 0, 0)
        gunDir = 1
        shootLoop = 0
        shootVal = 20
        bulletSpeed = 5
        pathLoop = 0
        pathVal = 30
        hitLoop = 0
        hitVal = 100
        bullets = []
        enemies = []

        level = 1
        me = player(
                marginSize + borderSize + screenWidth//2, marginSize + borderSize + screenHeight//2, playerSize, (155, 155, 0), playerLife,
                gunSize, gunColor, 'default', gunLoc, gunDir, gunSpin
                )

        for _ in range(level):
            enemies.append(enemy(marginSize + borderSize + screenWidth//4, marginSize + borderSize + screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
            enemies.append(enemy(marginSize + borderSize + screenWidth - screenWidth//4, marginSize + borderSize + screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
            enemies.append(enemy(marginSize + borderSize + screenWidth//4, marginSize + borderSize + screenHeight - screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))
            enemies.append(enemy(marginSize + borderSize + screenWidth - screenWidth//4, marginSize + borderSize + screenHeight - screenHeight//4, 'default', 10, (0, 200, 0), 0, 0, pathLoop, 2, (0, 0, 0), 'default', randint(0, 360), -1, 5))

    #Display update
    if run == True:
        display_update(me, enemies, bullets)
