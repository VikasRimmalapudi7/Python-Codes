class superlist(list):
    def __len__(self):
         return 1000
superlist1=superlist()
print(superlist1.__len__())
n=int(input("enter limit"))
for i in range(n):
    superlist1.append(i)
    print(superlist1[i])

    # here the list is super class and superlist is the subclass,now we are creating object of the class and appending the numbbeers and printing them