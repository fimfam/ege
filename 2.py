# print("x  y  z  w")
# for x in (0,1):
#     for y in (0,1):
#         for z in (0,1):
#             for w in (0,1):
#                 f= z or (x==(y<=w))
#                 if f==0:
#                     print(x,y,z,w, sep="  ")

print("m  e  o  w")
for m in (0,1):
    for e in (0,1):
        for o in (0,1):
            for w in (0,1):
                f=(m<=e) or (o==e) and w
                if f==0:
                    print(m,e,o,w, sep="  ")