# (19246)
# from string import *
# s=ascii_lowercase
# for x in "0123456789"+s[:15]:
#     n1="11353"+x+"12"
#     n2="135"+x+"21"
#     n=int(n1,25)+int(n2,25)
#     if n%24==0:
#         print(n//24)

# (17973)
# from string import *
# s=ascii_lowercase
# for x in "0123456789"+s[:14]:
#     n1=f"12{x}734"
#     n2=f"8{x}95{x}3"
#     n3=f"24{x}796"
#     n = int(n1, 24) + int(n2, 24) + int(n3,24)
#     if n%23==0:
#         print(n//23)

# (19261)
# for x in range(37):
#     n=5+37*5+37**2*(9+x)+37**3*(8+x)+37**4*10
#     if n%21==0:
#         print(n//21)

# (20284)
# for x in range(42):
#     n=(10+x)+ 42*27+42**2*(6+x)+42**3*6+42**4*19
#     if n%155==0:
#         print(n//155)

from string import*
s=ascii_lowercase
for x in s[6:11]:
    for y in "0123456789" + s[:int(x,36)-10]:
        n1=f"13F1{y}"
        n2=f"15{x}5{y}"
        n=int(n1,int(x,36))+int(n2,21)
        if n%32==0:
            print(n//32)
