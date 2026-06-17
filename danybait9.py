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
print((4080+16))
print(2**12)
print(12*257/8)
print(386*8388608/1024/1024)



