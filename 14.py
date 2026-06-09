# (19246)
# from string import *
# s=ascii_lowercase
# for x in "0123456789"+s[:15]:
#     n1="11353"+x+"12"
#     n2="135"+x+"21"
#     n=int(n1,25)+int(n2,25)
#     if n%24==0:
#         print(n//24)

# (17973)
# from string import *
# s=ascii_lowercase
# for x in "0123456789"+s[:14]:
#     n1=f"12{x}734"
#     n2=f"8{x}95{x}3"
#     n3=f"24{x}796"
#     n = int(n1, 24) + int(n2, 24) + int(n3,24)
#     if n%23==0:
#         print(n//23)

# (19261)
# for x in range(37):
#     n=5+37*5+37**2*(9+x)+37**3*(8+x)+37**4*10
#     if n%21==0:
#         print(n//21)

# (20284)
# for x in range(42):
#     n=(10+x)+ 42*27+42**2*(6+x)+42**3*6+42**4*19
#     if n%155==0:
#         print(n//155)

# from string import*
# s=ascii_lowercase
# for x in s[6:11]:
#     for y in "0123456789" + s[:int(x,36)-10]:
#         n1=f"13F1{y}"
#         n2=f"15{x}5{y}"
#         n=int(n1,int(x,36))+int(n2,21)
#         if n%32==0:
#             print(n//32)
# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
#
#
# d=[]
# g=10**100
# ix=0
# for x in range(1,2030):
#     a=6**2030+6**100-x
#     p=to_n(a,6)
#     s=p.count("0")
#     if s<g:
#         g=s
#
#
#
# print(g)
#

#28935
# from string import ascii_lowercase
# for x in "0123456789"+ascii_lowercase[:13]:
#     n1="761"+x+"035"
#     n2="338"+x+"932"
#     n=int(n1,23)+int(n2,23)
#     if n%22==0:
#         print(x,n//22)


#28760
from string import ascii_lowercase
def to_n(n,b):
    s="0123456789"+ascii_lowercase
    rez=""
    while n>0:
        a=s[n%b]
        rez=a+rez
        n=n//b
    return rez

t=2*2187**567+729**566-2*243**565+81**564-2*27**563-6561
r=to_n(t,27)
p=0
for i in r:
    if int(i,27)%2==0 and int(i,27)/2>9:
        p=p+1
print(p)
