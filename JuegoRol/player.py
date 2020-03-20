import personajes as p

 
class Player(p.Personajes):
    def __init__(self,name,typ,power):
            p.Personajes.__init__(self,name,typ,100,10,2,power)
            
            
if __name__ =='__main__':
    Player()