from display import *
from draw import *
import math

screen = new_screen()

##green = [0,255,0]
##draw_line(250,250, 250+150,250+50, screen, green)

length = 240
for i in range(360):
    h = i / 60
    c = int(i % 60 * 255 / 60)
    if (0 <= h < 1):
        color = [255,c,0]
    if (1 <= h < 2):
        color = [255-c,255,0]
    if (2 <= h < 3):
        color = [0,255,c]
    if (3 <= h < 4):
        color = [0,255-c,255]
    if (4 <= h < 5):
        color = [c,0,255]
    if (5 <= h < 6):
        color = [255,0,255-c]
    dx = int(length*math.cos(math.radians(i)))
    dy = int(length*math.sin(math.radians(i)))
    draw_line(250,250, 250+dx,250+dy, screen, color)

display(screen)
save_extension(screen, 'img.png')
