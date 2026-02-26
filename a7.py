import random


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



a1=Alien(2,6,10)
a2=Alien(3,8,3)
while a2.is_alive()==True:
    a2.hit()
print(a2.health)
print(a1.health)

a1.teliport()
print(a1.x_cord,a1.y_cord)
print(Alien.total_aliens)


