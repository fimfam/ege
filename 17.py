# with open("C:/Users/Dasha/Downloads/17_24200.txt") as f:
#     l=f.readlines()
#     l=list(map(int,l))
# print(l[3])
# n=0
# for i in l:
#     if i%2==0:
#         n=n+1
# print(n)
# d=0
# m=-100000000000000000
# for i in range(len(l)-1):
#     if (abs(l[i])>=1000 and abs(l[i])%1000<100) or (abs(l[i+1])>=1000 and abs(l[i+1])%1000<100):
#         if l[i]*l[i+1]%n==0:
#             d=d+1
#             m=max(m,l[i]+l[i+1])
# print(d,m)


# with open("C:/Users/1/Downloads/17_27301.txt") as f:
#     l=f.readlines()
#     l=list(map(int,l))
# print(l[1])
#
# p=[]
# for i in l:
#     if str(abs(i))[:2]=="45":
#         p.append(i)
# print(max(p))
# d=0
# w=[]
# for i in range(len(l)-3):
#     if (l[i]<0)+(l[i+1]<0)+(l[i+2]<0)==1:
#         if l[i]+l[i+1]+l[i+2]>=max(p):
#             d=d+1
#             if str(abs(l[i]+l[i+1]+l[i+2]))[-2:]=="45":
#                 w.append(l[i]+l[i+1]+l[i+2])
# print(d,min(w))



# with open("C:/Users/1/Downloads/17_27629.txt") as f:
#     l=f.readlines()
#     l=list(map(int,l))
# p=[]
# for i in l:
#     if abs(i)>999 and abs(i)<10000:
#         if str(i)[-2:]=="43":
#             p.append(i)
# print(max(p))
# d=0
# r=[]
# for i in range(len(l)-1):
#     if 999<abs(l[i])<10000 or 999<abs(l[i+1])<10000:
#         if (l[i]+l[i+1])**2<(max(p))**2:
#             d=d+1
#             r.append((l[i]+l[i+1])**2)
#
# print(d,max(r))
#

with open("C:/Users/1/Downloads/17_28762.txt") as f:
    l=f.readlines()
    l=list(map(int,l))
print(l[:5])
p=[]
for i in l:
    if i%23==0:
        p.append(i)


