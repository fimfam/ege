#20196
# from functools import *
#
# @lru_cache(3000)
# def f(n):
#     if n<110:
#         return n
#     else:
#         return n+f(n-1)
#
# for i in range(2025):
#     f(i)
#
# print(f(2025)-f(2021))


# 19707
# from functools import*
# @lru_cache()
# def f(n):
#     if n<3:
#         return(n*4)
#     if n>=3 and n%2!=0:
#         return(n*2)
#     else:
#         return(5*f(n-2)+n**2)
#
# c=0
# for n in range(1000):
#     if f(n)%2==0 and 100<=f(n)<=1000:
#         c=c+1
# print(c)

#25399
# from functools import *
# @lru_cache()
# def f(n):
#     if n>=128:
#         return f(n-5)+1092
#     else:
#         return 5*g(n-7)+29
#
#
# @lru_cache()
# def g(n):
#     if n>303728:
#         return n-15
#     else:
#         return g(n+8)/2-109
#
# for n in range(400000,1,-1):
#     g(n)
#
#
# print(f(2049))


# from functools import*
# from sys import*
# setrecursionlimit(1000)
# @lru_cache()
# def g(n):
#     if n<25:
#         return n
#     return (n-5)*g(n-6)
# print((g(60000)-315*g(59994))//g(59988))

# from functools import*
# from sys import*
# setrecursionlimit(100000)
# @lru_cache()
# def g(n):
#     if n<=6:
#         return 5**n
#     return g(n-3)+2
# print(g(50000)+g(150000))

# from functools import*
# from sys import*
# setrecursionlimit(10000)
# @lru_cache()
# def g(n):
#     if n==1:
#         return 1
#     return n*g(n-1)
# print((g(2024)-5*g(2023))//g(2022))

#25398
# from functools import*
# @lru_cache()
# def f(n):
#     if n>30:
#         return f(n-6)+2048
#     return 3*(g(n-5)+13)
# @lru_cache()
# def g(n):
#     if n>=221337:
#         return 2*n+50
#     return g(n+11)-48
# for i in range(221337,0,-1):
#     g(i)
# for b in range(30,5078):
#     f(b)
# print(f(5078))

#24081
# from functools import*
# @lru_cache()
# def f(n):
#     return g(n-50000)+g(n+50000)
# @lru_cache(200000)
# def g(n):
#     if n<=6:
#         return 5**n
#     return g(n-3)+2
# for i in range(6,150000):
#     g(i)
#
#print(f(100000))

#19707
from functools import*
@lru_cache()
def f(n):
    if n<3:
        return n*4
    if n>=3 and n%2!=0:
        return n*2
    else:
        return 5*f(n-2)+n**2
a=0
for i in range(0,100000):
    if 999>=f(i)>=100 and f(i)%2==0:
        a=a+1
print(a)

