x=10
y=11
while y!=0:
    carry=x&y
    x=x^y
    y=carry<<1
print(x)