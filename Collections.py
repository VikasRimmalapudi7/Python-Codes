import collections
c=collections.Counter('abcdabbde3klefjl') #counter
print(c)
d=collections.defaultdict(int)           #default dict it is used not to raise key error
d['1']=1
d['2']=2
print(d['3'])


o=collections.OrderedDict()            #it is used to maintaion ther order of insertion       
o['a']=1
o['b']=2
o['c']=3
o['a']='9'
print(o)
dd={'1':1,'2':2}
ee={'3':3,'4':4}
ch=collections.ChainMap(dd,ee)            #used to return list of dict's
print(ch)

student=collections.namedtuple('student',['name','age','dob'])    #named tuple is used to return tuple with respective names
n1=student('vikas','20','2002')
print(n1.name)