from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

(x0,y0) = (120,240)
(x1,y1) = (200,200)

draw_line(x0,y0, x1,y1, screen, color)

display(screen)
save_extension(screen, 'img.png')
