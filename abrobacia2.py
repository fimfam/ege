#2
# print("x  y  w  z")
# for x in (0,1):
#     for y in (0, 1):
#         for w in (0, 1):
#             for z in (0, 1):
#                 f=not((x<=w)<=(w==z)) and y
#                 if f==1:
#                     print(x,y,w,z,sep=("  "))



#5
# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# for n in range(1,130):
#     r=to_n(n,3)
#     if n%3==0:
#         r="1"+r+"02"
#     else:
#         ost=to_n((n%3)*5,3)
#         r=r+ost
#     if int(r,3)>=177:
#         print(n)
#
#8,12,13
# print(int("11111110",2))
# print(bin(180))
from string import ascii_lowercase

#14
def to_n(n,b):
    s='0123456789'+ascii_lowercase
    rez=""
    while n>0:
        a=s[n%b]
        rez=a+rez
        n=n//b
    return rez

l=120
print(to_n(l,11))

for x in range(0,3000):
    t=(9*11**210)+(8*11**150)-x
    r=to_n(t,11)
    if r.count("0")==60:
        print(x)


