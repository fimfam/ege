#2
# print("x  y  z  w")
# for x in (0,1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 f=(x and (not z) and (not w)) or (x and (not z) and y)
#                 if f==1:
#                     print(x,y,z,w,sep="  ")

#5
# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
#
# print(to_n(9,3))
#
# for n in range(9,130):
#     r=to_n(n,3)
#     if n%3==0:
#         r=r+r[-2]+r[-1]
#         g=int(r,3)
#     else:
#         s=r.count("1")+r.count("2")*2
#         syma=to_n(s*2,3)
#         r=r+syma
#         g=int(r,3)
#
#     if g%2!=0 and g>520:
#             print(g)

#8
# print(int("35441",6))

#12
# print(bin(2027))
# print(int("1111110101111",2))


#17
# with open("C:/Users/1/Downloads/17_28938.txt") as f:
#     l=f.readlines()
#     l=list(map(int,l))
# p=-100000000000000000000
# for i in l:
#     if i>p and str(i)[-2]==2 and str(i)[-1]==8:
#         p=i
# print(p)

#14
from string import*
s=ascii_lowercase

for x in "0123456789"+s[:13]:
    n1=f"761{x}035"
    n2=f"338{x}932"
    n=int(n1,23)+int(n2,23)
    if n%22==0:
        print(n//22)
        break





