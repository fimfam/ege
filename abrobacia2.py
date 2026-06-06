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
#8
print(int("35225",6))