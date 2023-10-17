import string
s = set(input())
vow = set('aeouyi')
con = set(string.ascii_lowercase) - vow
print("vowels:", len(s & vow))
print("cons:", len(s & con))

