import random
import math
from aliens import Alien

def near(ox,oy,x,y):
    dx=x-ox
    dy=y-oy
    if math.fabs(dx)>1 or math.fabs(dy)>1:
        return False
    else:
        return True




def gen_aliens(n,rx,ry,h):
    al = []
    for i in range(n):
        innear = True
        x, y = 0, 0
        while innear:
            x = random.randrange(-rx,rx)
            y = random.randrange(-ry,ry)
            innear = False
            for a in al:
                innear = near(a.x_cord,a.y_cord,x,y)
                if innear:
                    break
        al.append(Alien(x,y,h))
    return al

