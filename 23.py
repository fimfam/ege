def(m,n):
    if m==n:
        return 1
    if m<n:
        return 0
    if m%6==0:
        return 0
    return f(m-1,n)+f(m//3,n)+(m//4,n)

