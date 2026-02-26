def print_stars(n):
    for i in range(n):
        print('*')

#print(print_stars(1))




class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x,y)
    def norm(self):
        i=(self.x**2+self.y**2)**0.5
        return i
        print(i)


# v=Vector(1,2)
# v.norm()

def check_casel(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# print(check_casel('Hello'))
# print(check_casel('HELLO'))
# print(check_casel('hello'))

