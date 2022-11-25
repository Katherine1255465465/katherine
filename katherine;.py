class geo:
    def __init__(self):
        self.a = input("como te llamas :")
        self.b = float(input("dame tu altura:"))
        self.c = float(input ("dame tu peso"))
    def datos (self):
        print (f"nombre:", self.a)
        print (f"altura :", self.b)
        print (f"peso:", self.c)
    #def imprimir(self):
        
x = geo()
x.datos()
#x.imprimir()
    
