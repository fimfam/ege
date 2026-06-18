#2
# print("x  y  w  z")
# for x in(0,1):
#     for y in (0, 1):
#         for w in (0, 1):
#             for z in (0, 1):
#                 f=not(x or not z) and (y<=w)
#                 if f==1:
#                     print(x,y,w,z,sep="  ")

#5
# m=1
# for n in range(1,1000):
#     r=bin(n)[2:]
#     if r.count("11")==1:
#         r=r+"0"
#         r=r[2:]
#         r="10"+r
#     else:
#         r=r+"1"
#         r=r[2:]
#         r="11"+r
#     if int(r,2)<=1500 and int(r,2)>m:
#         m=int(r,2)
#         nn=n
# print(m,nn)


#6
# from turtle import*
# tracer(0)
# k=30
# screensize(2000,2000)
# right(90)
# for i in range(8):
#     forward(15*k)
#     right(60)
#     forward(10*k)
#     right(60)
# up()
# for x in range(-22,200):
#     for y in range(-200,20):
#         goto(x*k,y*k)
#         dot(3)
#
# done()

#8
# print(int("2000331",6))
# print((4080+16))
# print(2**12)
# print(12*257/8)
# print(386*8388608/1024/1024)

# print(bin(0))
# print(int("11010",2))

#14
# from string import*
# def to_n(n,b):
#     rez=""
#     while n>0:
#         s="0123456789"+ascii_lowercase
#         a=s[n%b]
#         rez=a+rez
#         n=n//b
#     return rez
# t=2*16**2020+9*16**2021-2*4**2022+8**2023-2*2**2024-65536
# r=to_n(t,16)
# m=0
# for i in r:
#     if int(i,16)>9:
#         m=m+1
# print(m)

#16
# from functools import*
# @lru_cache()
# def f(n):
#     if n<10:
#         return 1
#     return (n+3)*f(n-3)
# for i in range(10,318759):
#     f(i)
# print((f(318765)-318762*f(318762))//f(318759))


#17
# with open("C:/Users/Dasha/Downloads/17_29798.txt") as f:
#     l=f.readlines()
#     l=list(map(int,l))
# print(l[:5])
# k=-100000
# for i in l:
#     if 1<=abs(i)/10000<10 and str(i)[-2:]=="42" and i>k:
#         k=i
# print(k)
# p=0
# zup=[]
# for i in range(len(l)-1):
#     a,b=l[i],l[i+1]
#     if (str(a)[-2:]=="42" and 1<=abs(a)/10000<10)+(str(b)[-2:]=="42" and 1<=abs(b)/10000<10)==1 and a**2+b**2>=k**2:
#         p=p+1
#         zup.append(a+b)
# print(p,max(zup))

#19-21
# def f(n,h):
#     if n>=150:
#         if h%2==t%2:
#             return 1
#         return 0
#     if h>t:
#         return 0
#     if h%2==t%2:
#         return f(n+4,h+1) and f(n+8,h+1) and f(n*3,h+1)
#     return f(n + 4, h + 1) or f(n + 8, h + 1) or f(n * 3, h + 1)
#21
# t=2
# l=[]
# for s in range(1,150):
#      if f(s,0)==1:
#          l.append(s)
# t=4
# k=[]
# for s in range(1,150):
#     if f(s,0)==1 and s not in l:
#         k.append(s)
# print(min(k))


# 20
# t=1
# l=[]
# for s in range(1,150):
#      if f(s,0)==1:
#          l.append(s)
# t=3
# k=[]
# for s in range(1,150):
#      if f(s,0)==1 and s not in l:
#          k.append(s)
# print(max(k),min(k))

# 19
# t=2
# l=[]
# for s in range(1,150):
#     if f(s,0)==1:
#         l.append(s)
# print(max(l))

#23
def f(n,m):
    if n==m:
        return 1
    if n>m:
        return 0
    return f(n-1,m)+f(n+2,m)+f(n*2,m)


