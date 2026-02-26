import string
s1=set(string.ascii_lowercase)
s2=set('the quick brown fox jumps over lazy dog')
print(s1==s2)
print(s1^s2)
print(s1|{' '}==s2)