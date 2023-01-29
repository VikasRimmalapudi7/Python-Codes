class player:
    def __init__(self,name,num):
       self.name=name
       self.num=num
    
    def runnin(self,num1,num2):
        return num1+num2
    @staticmethod
    def stat(num3,num4):
        return num3+num4
player1=player("vikas","j4")

print(player1.runnin(2,3))    
print(player.stat(4,6))

    #IF we want to keep variables as private we just need to put underscore before the variable name so it shouldnt be modified....
