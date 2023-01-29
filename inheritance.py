class war:
    def warstarts(self):
        print("war started")
class knight(war):
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(f'{self.name} attacking with a power of {self.power}')
class archer(knight):
    def __init__(self, name,num):
        self.name=name
        self.num=num
    def attack(self):
        print(f'{self.name} has left with  {self.num} arrows' )
knight1=knight("ned stark",100)
archer1=archer("robbstark",23)
archer1.warstarts()
knight1.attack()
archer1.attack()
print(isinstance(archer,object))