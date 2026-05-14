# (2)
# print("x  y  w  z")
# for x in(0,1):
#     for y in (0,1):
#         for w in (0, 1):
#             for z in (0, 1):
#                 f=not w or ((z<=x)<=y)
#                 if f==0:
#                     print(x, y, w, z, sep="  ")


# (5)
# def to_n(n,b):
#     rez=""
#     while n>0:
#         a=str(n%b)
#         rez=a+rez
#         n=n//b
#     return rez
# s=0
# for n in range(1,300):
#     r=to_n(n,3)
#     if n%3==0:
#         r=r+r[-2]+r[-1]
#     else:
#         for i in range(len(r)+1):
#             s=s+int(r[i])
#         s=s*3
#         s=to_n(s,3)
#         r=r+s
#     if int(r)==826:
#         print(int(r))




