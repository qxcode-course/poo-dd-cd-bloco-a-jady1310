class Toalha:
    def __init__ (self): #construtor
        self.color = "pink" #atributos
        self.size = "m"
        self.wetness = 0

    def __str__ (self):
        return f"color: {self.color}, tam: {self.size}, hum: {self.wetness}"


toalha = Toalha() #objetos
toalha.color = "white" #ela era rosa e ficou branca
print (toalha.color) 
print (toalha.size)
print (toalha.wetness)