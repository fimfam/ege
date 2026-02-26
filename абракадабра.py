import math
s=input()
ss=set(s)
f=len(ss)
n=math.log2(f)
n=int()+1
d={}
j=0
for a in ss:
    d[a]=j
    j=j+1
print(d)
l=[]
for c in s:
    l.append(d[c])
for i in l:
    print("{:b}".format(i))
print(l)
#print("{:b}".format(x))

