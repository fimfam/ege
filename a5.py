import string
l=list(string.ascii_lowercase)
def shifr(s,k):
    es=''
    for i in range(len(s)):
        if s[i].isalpha():
            n=l.index(s[i])+1
            en=(n+k)%26
            es+=l[en-1]
        else:
            es+=s[i]
        return es
print(shifr('hello world',5))

