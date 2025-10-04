class Animal:
    def __init__(self, species: str, sound:str):
        self.species = species
        self.sound = sound
        self.age = 0

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

    
    def ageBy(self, increment: int):
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age=4
        
        # if self.age >= 4:
        #     print(f"warning:{self.species} morreu")
            
        # self.age += increment
        # if self.age >= 4:
        #     self.age = 4
        #     print(f"warning:{self.species} morreu")

    def makeSound(self):
        if self.age ==0:
            return '---'
        if self.age ==4:
            return "RIP"
        return self.sound
def main():
    animal= Animal (" ", " ")
    while True:
        line: str=input()
        args:list[str] = line.split (" ")
        print(f"${line}")

        if args[0] == "end":
            break
        elif args[0] == "init":
            animal.species = args[1]
            animal.sound = args[2]
            # animal = Animal(species, sound)
        elif args[0]== "show":
            print(animal)
        elif args[0] == "grow":
            increment = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            print(animal.makeSound())
        else:
            print("Comando invalido")
main()



