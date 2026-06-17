# def f(m,n):
#     if m==n:
#         return 1
#     if m<n:
#         return 0
#     if m%6==0:
#         return 0
#     return f(m-1,n)+f(m//3,n)+f(m//4,n)
#
# print(f(100,33)*f(33,1))

#28764
# def f(m,n):
#     if m==n:
#         return 1
#     if m>n:
#         return 0
#     if m==7:
#         return 0
#     return f(m+1,n)+f(m+3,n)+f(m*2,n)
# print(f(2,15)*f(15,25))

#27314
# def f(m,n):
#     if m==n:
#         return 1
#     if m>n:
#         return 0
#     if m==28:
#         return 0
#     if m==36:
#         return 0
#     return f(m+1,n)+f(m+5,n)+f(m*3,n)
# print(f(2,18)*f(18,49)+f(2,30)*f(30,49)-f(2,18)*f(18,30)*f(30,49))

#27310
def f(m,n):
    if m==n:
        return 1
    if m<n:
        return 0
    return f(m-3,n)+f(m-4,n)+f(m//2,n)
print(f(78,30)*f(30,2)+f(78,42)*f(42,2)-f(78,42)*f(42,30)*f(30,2))