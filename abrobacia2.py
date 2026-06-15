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

#14
# from string import ascii_lowercase
#
# def to_n(n,b):
#     s='0123456789'+ascii_lowercase
#     rez=""
#     while n>0:
#         a=s[n%b]
#         rez=a+rez
#         n=n//b
#     return rez
#
# l=120
# print(to_n(l,11))
#
# for x in range(0,3000):
#     t=(9*11**210)+(8*11**150)-x
#     r=to_n(t,11)
#     if r.count("0")==60:
#         print(x)
#16
# from functools import*
# @lru_cache()
# def f(n):
#     return 3*g(n-3)+7
# @lru_cache()
# def g(n):
#     if n <=20:
#         return n+2
#     return g(n-3)+1
# for i in range(0,37811):
#     g(i)
# print(f(37811))

#17
# with open("C:/Users/1/Downloads/17_29971.txt") as f:
#     l=f.readlines()
#     l=list(map(int,l))
#     # for i in range(len(l)):
#     #     l[i]=int(l[i])
# print(l[:5])
# m=-100000
# for i in l:
#     if i>m and str(i)[-2:]=="33":
#         m=i
# print(m)
# p=0
# k=[]
# for i in range(len(l)-2):
#     a,b,c=l[i],l[i+1],l[i+2]
#     if ((9<abs(a)<=99)+(9<abs(b)<=99)+(9<abs(c)<=99))==2 and (a+b+c)**2<m:
#         k.append(a+b+c)
#         p=p+1
# print(p,max(k))

#19-21
t=2
def f(n,h):
    if n<=15:
        if t%2==h%2:
            return 1
        return 0
    if h>t:
        return 0
    if h%2==t%2:
        return f(n-3,h+1) and f(n-7,h+1) and f(n//4,h+1)
    return f(n-3,h+1) or f(n-7,h+1) or f(n//4,h+1)

t=2
l=[]
for s in (16,99):
    if f(s,0)==1:
        l.append(s)
t=4
k=[]
for s in range(16,99):
    if f(s,0)==1 and s not in l:
        k.append(s)
print(k)




#20
# t=1
# l=[]
# for s in range(1,99):
#     if f(s,0)==1:
#         l.append(s)
# k=[]
# t=3
# for s in range(1,99):
#     if f(s,0)==1 and s not in l:
#         k.append(s)
# print(k)

#19
# l=[]
# for s in range(60,100):
#     if f(s,0)==1:
#         l.append(s)
# print(l)



