def f(m,n):
    if m==n:
        return 1
    if m<n:
        return 0
    if m%6==0:
        return 0
    a=f(m-1,n)+f(m//3,n)+f(m//4,n)
    print(a)
    return a
print(f(100,33)*f(33,1))

