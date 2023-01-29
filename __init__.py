class player:
    #def __init__(self,name,num):
       # self.name=name
      #  self.num=num
    @classmethod
    def runnin(self,num1,num2):
        return num1+num2
    @staticmethod
    def stat(num3,num4):
        return num3+num4
#player1=player("vikas","j4")

print(player.runnin(2,3))    
    
