#(22433)
# for A in range(1,256):
#     f=1
#     for x in range(1,256):
#         Fu=((x&117)!=0 and (x&91)==0) <= (not ((x&A)==0))
#         if Fu==False:
#             f=0
#     if f==1:
#         print(A)

# (20584)
# for A in range(1,800):
#     f=1
#     for x in range(1,512):
#         Fu=(((405%x)==0) <= ((81%x)==0)) or (A-x>162)
#         if Fu==False:
#             f=0
#     if f==1:
#         print(A)

# (23374)
# for A in range(1,800):
#     f=1
#     for x in range(1,800):
#         for y in range(1,800):
#             Fu=(x<A) and (y<3*A) or (2*x+y>128)
#             if Fu==False:
#                 f=0
#     if f==1:
#         print(A)

# (19899)
# for A in range(1,800):
#     f=1
#     for x in range(1,800):
#         Fu=(A+2*x>400-A) and (A%100+120%A)>140
#         if Fu==False:
#             f=0
#     if f==1:
#         print(A)

for A in range(1,1000):
    f=1
    for x in range(1,1000):
        Fu=(x%25==0)<=((not(x%A==0))<=(not(x%60==0)))
        if Fu==False:
            f=0
    if f==1:
        print(A)
