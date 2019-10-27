import random
from random import randint
import pygame as pg
from Tile_script import Tile

bluebox_img = pg.image.load("C:/Users/Nilushie/Desktop/BOX/img/blue_box.png")
greenbox_img = pg.image.load("C:/Users/Nilushie/Desktop/BOX/img/green_box.png")
ashbox_img = pg.image.load("C:/Users/Nilushie/Desktop/BOX/img/ash_box.png")

def drawbluebox(x, y):
    display.blit(bluebox_img, (x * W, y * W))

def drawgreenbox(x, y):
    display.blit(greenbox_img, (x * W, y * W))

def moveR(Tile):
    if Tile.x==8:
        print("Boundary reached")
    else:
        x1 = Tile.x
        print(x1)
        x1 += 1
        Tile.x = x1
        y1 = Tile.y
        display.blit(greenbox_img, (x1 * W, y1 * W))
        grid[x1][y1].item = True
        grid[x1-1][y1-1].item=False
        display.blit(ashbox_img, (x1 * W, y1 * W))



W=40
Boxes=5
Tile()


display_width=360
display_height=360
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue= (0,0,255)




pg.init()
display=pg.display.set_mode((display_width,display_height))
pg.display.set_caption("Box")
clock = pg.time.Clock()




crashed=False
display.fill(white)
grid=[[Tile() for n in range(9)] for n in range(9)]
random.seed(20)
x = randint(0, 8)
y = randint(0, 8)


drawgreenbox(x,y)
grid[x][y].item = True
grid[x][y].player=True
grid[x][y].x=x
grid[x][y].y=y

'''for n in range(Boxes):
    drawn=False
    while drawn==False:
        x = randint(0, 8)
        y = randint(0, 8)
        if grid[x][y].item==False:
            drawbluebox(x,y)
            grid[x][y].item = True
            grid[x][y].player = False
            grid[x][y].box = True
            grid[x][y].x = x
            grid[x][y].y = y
            drawn=True
            print(111)'''







actions=[1,2,3,4]
state=grid


for i in range(9):
    for j in range(9):
        if grid[i][j].player==True:
            print(i,j)






while not crashed:
    '''drawbluebox(0, 0)'''
    pg.display.update()
    clock.tick(10)

pg.quit()
quit()

'''    drawbluebox(x,y)
    drawgreenbox(x+320, y)
    pg.display.update()
    clock.tick(60)'''