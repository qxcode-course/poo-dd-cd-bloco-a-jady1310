class Calculadora:
    def __init__(self, batteryMax:int):
        self.batteryMax=batteryMax
        self.battery=0
        self.display=0.00
    def __str__(self):
        return (f"display = {self.display:.2f}, battery = {self.battery}")
    def charge (self, value:int):
        self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
    def sum(self, a, b):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.display=a+b
            self.battery -=1
    def division(self, num:int, den:int):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        elif den ==0:
            print("fail: divisao por zero")
            self.battery -=1
        else:
            self.display= num/den
            self.battery -=1
def main():
    calculadora = Calculadora (0)
    while True:
        line=input()
        args:list[str]=line.split(" ")
        print(f"${line}")

        match args[0]:
            case "init":
                calculadora.batteryMax = int(args[1])
                calculadora.battery = 0
                calculadora.display = 0.00
            case "show":
                print(calculadora)
            case "charge":
                calculadora.charge(int(args[1]))
            case "sum":
                calculadora.sum(int(args[1]), int(args[2]))
            case "div":
                calculadora.division(int(args[1]), int(args[2]))
            case "end":
                break
            case _:
                print("comando invalido")
main()



