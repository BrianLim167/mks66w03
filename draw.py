from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if ( x1 < x0 ):
        (x0, x1) = (x1, x0)
        (y0, y1) = (y1, y0)
    a = y1 - y0
    b = x0 - x1
    (x,y) = (x0,y0)
    if ( 0 <= a <= -b ):
        d = 2*a + b
        while ( x <= x1 ):
            plot(screen, color, x, y)
            if ( d > 0 ):
                y += 1
                d += 2*b
            x += 1
            d += 2*a
        return
    if ( -b <= a ):
        d = a + 2*b
        while ( y <= y1 ):
            plot(screen, color, x, y)
            if ( d < 0 ):
                x += 1
                d += 2*a
            y += 1
            d += 2*b
        return
    if ( b <= a <= 0 ):
        d = 2*a - b
        while ( x <= x1 ):
            plot(screen, color, x, y)
            if ( d < 0 ):
                y -= 1
                d -= 2*b
            x += 1
            d += 2*a
        return
    if ( a <= b ):
        d = a - 2*b
        while ( y >= y1 ):
            plot(screen, color, x, y)
            if ( d > 0 ):
                x += 1
                d += 2*a
            y -= 1
            d -= 2*b
        return
