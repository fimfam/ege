#23759
#t=2
# def f(n,h):
#     if n<=30:
#         if h%2==t%2:
#             return 1
#         else:
#             return 0
#     if h>t:
#         return 0
#     if h%2==t%2:
#         return f(n-5,h+1) and f(n-3,h+1) and f(n//4,h+1)
#     else:
#         return f(n-5,h+1) or f(n-3,h+1) or f(n//4,h+1)
#
# for s in range(31,1000):
#     if f(s,0)==1:
#         print(s)
#         break

# t=2
# def f(n,h):
#     if n<=30:
#         if h%2==t%2:
#             return 1
#         else:
#             return 0
#     if h>t:
#         return 0
#     if h%2==t%2:
#         return f(n-5,h+1) and f(n-3,h+1) and f(n//4,h+1)
#     else:
#         return f(n-5,h+1) or f(n-3,h+1) or f(n//4,h+1)
# z=[]
# for s in range(31,1000):
#     if f(s,0)==1:
#         z.append(s)
# t=4
# for s in range(31,1000):
#     if f(s,0)==1 and s not in z:
#         print(s)


# t=2
# def f(n1,n2,h):
#     if n1+n2>=175:
#         if h%2==t%2:
#             return 1
#         else:
#             return 0
#     if h>t:
#         return 0
#     if h%2==t%2:
#         return f(n1+1,n2,h+1) and f(n1,n2+1,h+1) and f(n1*3,n2,h+1) and f(n1,n2*3,h+1)
#     else:
#          return f(n1+1,n2,h+1) or f(n1,n2+1,h+1) or f(n1*3,n2,h+1) or f(n1,n2*3,h+1)
#
# z=[]
# for s in range(1,154):
#     if f(19,s,0)==1:
#         z.append(s)
# t=4
# for s in range(1,154):
#     if f(19,s,0)==1 and s not in z:
#         print(s)
#

t=2
def f(n1,n2,h):
    if n1*n2>=455:
        if h%2==t%2:
            return 1
        else:
            return 0
    if h>t:
        return 0
    if h%2==t%2:
        return f(n1+1,n2,h+1) and f(n1,n2+1,h+1) and f(n1*2,n2,h+1) and f(n1,n2*2,h+1)
    else:
         return f(n1+1,n2,h+1) or f(n1,n2+1,h+1) or f(n1*2,n2,h+1) or f(n1,n2*2,h+1)

z=[]
for s in range(1,154):
    if f(19,s,0)==1:
        z.append(s)
t=4
for s in range(1,154):
    if f(19,s,0)==1 and s not in z:
        print(s)

