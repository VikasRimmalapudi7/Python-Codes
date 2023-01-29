import re
pattern=re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"  )
s='vik@jj.com'
a=re.search(pattern,s)
if a:
    print("valid email")