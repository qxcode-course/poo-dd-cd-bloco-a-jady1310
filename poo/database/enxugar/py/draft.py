class Toalha:
    def __init__ (self, color: str, size: str): #construtor
        self.color: str= color #atributos
        self.size: str = size 
        self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def getMaxWetness (self) -> int:
        if self .size == "P":
            return 10 
        if self .size == "M":
            return 20
        if self .size == "G":
            return 30
        return 0
    
    def wringOut (self) -> None:
        self.wetness = 0

    def isDry(self)->bool:
        return self.wetness==0

    def __str__ (self) -> str:
        return f"Cor: {self .color}, Tamanho: {self .size}, Umidade: {self .wetness}"

def main ():
    toalha = Toalha ("", "")
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        print(f"${line}")
        if args[0] == "end":
            break
        elif args[0] == "criar":
            color = args[1]
            size = args[2]
            toalha = Toalha(color, size)

        elif args[0] == "mostrar":
            print(toalha)

        elif args[0] == "seca":
            print(f"sim"if toalha.isDry() else "nao")

        elif args[0]=="torcer":
            toalha.wringOut()
        
        elif args[0]=="enxugar":
            toalha.dry(int(args[1]))
        else:
            print ("fail: comando invalido")
        
main()