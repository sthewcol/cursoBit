class Personajes(object):
    def __init__(self,name,typ,hp,atk,defp,power):
        self.name=name
        self.typ=typ
        self.hp=hp
        self.atk=atk
        self.defp=defp
        self.power=power
        
    def getParams(self):
        print("Name:","   ",self.name)
        print("TP:","     ",self.typ)
        print("HP:","     ",self.hp)
        print("ATK:","    ",self.atk)
        print("DEF:","    ",self.defp)
        print("POWER:","  ",self.power)
    
    def setHP(self,hp):
        self.hp=hp
        
    def getHP(self):
        return  self.hp
    
    def setATK(self,atk):
        self.atk=atk
        
    def getATK(self):
        return  self.atk
    
    def getName(self):
        print(f"Mi nombre es: {self.name}")
        
        
        
if __name__ =='__main__':
    Personajes()
