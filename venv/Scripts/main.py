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
grid=[[0 for n in range(9)] for n in range(9)]

def gameloop():
    crashed=False
    display.fill(white)



    x1=8
    y1=8

    random.seed(20)
    '''x = randint(0, 8)
    y = randint(0, 8)'''
    x=4
    y=4
    dx=0
    dy=0
    reward = 0
    while not crashed:

        for event in pg.event.get():
            if event.type==pg.QUIT:
                crashed=True
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_LEFT:
                    dx=-1
                    action=0
                elif event.key==pg.K_RIGHT:
                    dx=1
                    action = 1
                elif event.key==pg.K_UP:
                    dy=-1
                    action = 2
                elif event.key==pg.K_DOWN:
                    dy=1
                    action = 3

                grid[x][y]=0
                x = x + dx
                y = y + dy

                if x==9:
                    print("limit reached")
                    x = x - dx
                elif y==9:
                    print("limit reached")
                    y=y-dy
                elif y==-1:
                    print("limit reached")
                    y=y-dy
                elif x==-1:
                    print("limit reached")
                    x=x-dx
                dx=0
                dy=0
                if grid[x][y]==2:
                    grid[x][y] = 1
                    reward=1
                    crashed=True
                else:
                    reward=0


                print(x,y)

        display.fill(white)
        drawbluebox(x1, y1)
        grid[x1][y1]=2
        drawgreenbox(x, y)
        '''print(event)'''

        pg.display.update()
        clock.tick(10)

    return

reward=gameloop()
print(reward)
pg.quit()
quit()

