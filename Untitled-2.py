t=int(input())
while t>0:
  s=input("enter string")  
  n=len(s)
  l=[]  
  vowels=['a','e','i','o','u']
  for i in range(n-2):
    if s[i] not in vowels:
        if s[i+1] in vowels:
            l.append(i)
  print(l)
  t-=1
