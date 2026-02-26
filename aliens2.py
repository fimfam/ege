import matplotlib.pyplot as plt




class Alien:
    total_aliens=0
    def __init__ (self,x,y,h):
        self.x_cord=x
        self.y_cord=y
        self.health=h
        Alien.total_aliens+=1

    def is_alive(self):
        return self.health>0

    def hit(self):
        self.health-=1

    def teliport(self):
        self.x_cord+=random.randrange(-100,100)
        self.y_cord+=random.randrange(-100,100)


import math
def near(ox,oy,x,y):
    dx=x-ox
    dy=y-oy
    if math.fabs(dx)>1 and math.fabs(dy)>1:
        return True


import random
al=[]
for i in range(n):
    innear=True
    x,y=0,0
    while innear:
        x = random.randrange(-xy,xy)
        y = random.randrange(-xy, xy)
        innear=False
        for a in al:
            innear=near(a.x,a.y,rx,ry)
            if innear:
                break




    while near():
        x=random.randrange(1,20)
        y=random.randrange(1,20)
        while near return True


