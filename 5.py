# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
#
# for n in range(1,130):
#     r=to_n(n,3)
#     if n%3==0:
#         r=r+r[-2]+r[-1]
#     else:
#         a=n%3*3
#         c=to_n(a,3)
#         r=r+c
#     if (int(r,3))<=150:
#         print(n)
#21700

# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# l=[]
# for n in range(9,130):
#     r=to_n(n,3)
#     if n%3==0:
#         r=r+r[0]+r[1]+r[2]
#     else:
#         a=r.count("1")
#         b=r.count("2")
#         s=b*2+a
#         summa=s*5
#         g=to_n(summa,3)
#         r=r+g
#     if int(r,3)>2500:
#         l.append((int(r,3)))
# l.sort()
# print(l)
# 20951

# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# for n in range(1,130):
#     r=to_n(n,3)
#     if n % 3 == 0:
#         r=r+r[-2]+r[-1]
#     else:
#         a1=r.count("1")
#         a2=r.count("2")
#         summa=a1+a2*2
#         g=to_n(summa,3)
#         r=r+g
#     if int(r,3)>220:
#             print(int(r,3))
# 19237

# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# for n in range(1,130):
#     r=to_n(n,4)
#     if n%3==0:
#         r=r[-1]+r[1:len(r)-1]+r[0]
#         r=r+"1"
#     else:
#         ost=n%3
#         r=r+str(ost)
#     if int(r,4)<=340:
#         print(int(r,4))


# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# for n in range(1,130):
#     r=to_n(n,3)
#     if n%5==0:
#         r=r+r[-1]+r[-2]
#     else:
#         b=n%5*7
#         a=to_n(b,3)
#         r=r+a
#     if int(r,3)<=273:
#         print(n)

def to_n(n,b):
    rez=""
    while n>0:
        a=str(n%b)
        rez=a+rez
        n=n//b
    return rez
l=list()
for n in range(1,130):
    r=to_n(n,12)
    if n%4==0:
        r="A"+r+"B"
    else:
        r="1"+r+"0"
    if int(r,12)>2025:
        l.append(int(r,12))

print(min(l))