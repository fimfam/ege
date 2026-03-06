from string import ascii_lowercase
from functools import lru_cache

def n2():
    print('m e o w')
    for m in range(2):
        for e in range(2):
            for o in range(2):
                for w in range(2):
                    f=(m<=e) or (o==e) and w
                    if f==0:
                        print(m,e,o,w)

def to_n(n,b):
    s=''
    while n>0:
        s=str(n%b)+s
        n//=b
    return s

def n5():
    lst=[]
    for n in range(1,200):
        r=to_n(n,3)
        if n%5==0:
            r+=r[-2:]
        else:
            r+=to_n(n%5*7,3)
        r=int(r,3)
        if r<200:
            lst.append(n)
    print(sum(lst)/len(lst))

def n8():
    print(int('5443212',6)+1)

def to_d(s,b):
    r=0
    p=0
    for i in s[::-1]:
        r+=int(i,36)*b**p
        p+=1
    return r


def n14():
    s='0123456789'+ascii_lowercase
    for p in range(int('w',36)+1,100):
        n1=to_d('kot',p)+to_d('golodni',p)
        n2=to_d('meeow',p)*to_d('100',p)-20194023088
        print(n1-n2)
        if n1==n2:
            print(p, to_d('purr',p))





n14()