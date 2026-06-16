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
for n in range(1,130):
    r=bin(n)[:1]
    if r.count("11")==1:
        r=r+"0"
        r=r.replace(r[:1],"10")
    else:
        r=r+"1"
        r=r.replace(r[:1],"11")
    m=1
    if int(r,2)<=1500 and int(r,2)>m:
        m=r
        print(n)


