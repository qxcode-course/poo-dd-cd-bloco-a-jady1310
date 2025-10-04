class Carro:
    def __init__(self, Pass:int, gas:int, km:int):
        self.Pass=Pass
        self.gas=gas
        self.km=km
        self.PassMax=2
        self.gasMax=100
    
    def __str__(self):
        return (f"pass: {self.Pass}, gas: {self.gas}, km: {self.km}")
    
    def enter(self):
        self.Pass +=1
        if self.Pass > self.PassMax:
            print("fail: limite de pessoas atingido")
            self.Pass -=1
    def leave(self):
        self.Pass -=1
        if self.Pass < 0:
            print("fail: nao ha ninguem no carro")
            self.Pass +=1
    def drive(self, distance:int):
        if self.Pass == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas ==0:
            print("fail: tanque vazio")
        elif distance > self.gas:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas=0
        else:
            self.km += distance
            self.gas -= distance
    def fuel(self, increment:int):
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax

def main():
    carro = Carro(0,0,0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print(f"${line}")

        match args[0]:
            case "end":
                break
            case "show":
                print(carro)
            case "enter":
                carro.enter()
            case "leave":
                carro.leave()
            case "drive":
                carro.drive(int(args[1]))
            case "fuel":
                carro.fuel(int(args[1]))
            case _:
                print("comando invalido")
main()

