def isBalanced(s):
    stack=[]
    open=['(','{','[']
    closed=[')','}',']']
    for i in s:
            if i in open:
                    stack.append(i)
            elif i in closed:
                      pos=closed.index(i)
                      if len(stack)>0 and open[pos]==stack[len(stack)-1]:
                                stack.pop()
                      else:
                              return False
    if len(stack)==0:
            return True
    else:
            return False        
s="((()))"
print(isBalanced(s))