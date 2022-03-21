# Followed this tutorial: https://www.edureka.co/blog/snake-game-with-pygame/

import pygame as pyg

pyg.init()

white = (255, 255, 255)
black = (0,0,0)
red = (128,0,0)

dis=pyg.display.set_mode((400,300))
pyg.display.set_caption('Snake!')

game_over=False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pyg.time.Clock()

while not game_over:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            game_over=True
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pyg.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pyg.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pyg.K_DOWN:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pyg.draw.rect(dis,black,[200,150,10,10])

    pyg.display.update()

    clock.tick(30)

pyg.quit()
quit()
