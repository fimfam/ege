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


class bossAlien(Alien):
    def __init__(self,x,y,h,a):
        super().__init__(x,y,h)
        self.armor=a



