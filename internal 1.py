t=int(input())
while t>0:
  s=input("enter string")  
  ll=""
  n=len(s)
  l=[]  
  vowels=['a','e','i','o','u']
  for i in range(n-1):
    if s[i] not in vowels:
        if s[i+1] in vowels:
            ll+=s[i]

            l.append(i)
  print(l)
  print(ll)
  t-=1
