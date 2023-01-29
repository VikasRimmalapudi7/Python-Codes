lis=[1,2,3,4,5,6,7]
def fun(n):
    return n%2==0
print(list(filter(fun,lis)))   
# filter is used to filter the elements we can reduce tthe functions length by using filteer method