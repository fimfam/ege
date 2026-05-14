#открытый вариант
#2
# print("x  y  z  w")
# for x in (0,1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 f=((z<=x)<=(x==y)) or not w
#                 if f==0:
#                     print(x,y,z,w,sep="  ")

#5
# def to_n (n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# for n in range(2,19):
#     r=bin(n)[2:]
#     s=r.count("1")
#     if s%2==0:
#         r=r+"0"
#         r="10"+r[2:]
#     else:
#         r=r+"1"
#         r = "11" + r[2:]
#     print(n, int(r,2))
#8
# print(int("100330",6))

#13
# print(bin(243))
# print(int('11111110',2))

#17
# with open("C:/Users/1/Downloads/17_29349.txt") as f:
#     l = f.readlines()
#     l = list(map(int, l))
# p=[]
# for i in l:
#     if i>0 and i%123==0:
#         p.append(i)
# a=min(p)
# g=0
# boo=[]
# for i in range(len(l)-1):
#     if l[i]+l[i+1]<a:
#         g=g+1
#         boo.append(l[i]+l[i+1])
# print(g)
# print(max(boo))







#23
# def f(m,n):
#     if m==n:
#         return 1
#     if m>n:
#         return 0
#     if m==14:
#         return 0
#     return f(m+1,n)+f(m*2,n)+f(m*3,n)
# print(f(2,39))

#12
# print(bin(1023))
# print(int("10000000000",2))

#16
from functools import*
from sys import *
setrecursionlimit(10000000)
@lru_cache()
def f(n):
    if n<10:
        return 1
    else:
        return (n+3)*f(n-3)
print((f(247563)//519-477*f(247560))//f(247557))
