class Towel:
    color: str
    size: str
    wetness: int

    def __init__(self, color: str, size: str) -> None:
        self.color = color
        self.size = size
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30

        return 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.color} {self.size} {self.wetness}"

towel = Towel("Azul", "P")
towel.show()
towel.dry(5)
towel.show()
print(towel.isDry())
towel.dry(5)
towel.show()
towel.dry(5)
towel.show()

towel.wringOut()
towel.show()

towel = Towel("Verde", "G")
print(towel.isDry())
towel.dry(30)
towel.show()
print(towel.isDry())
towel.dry(1)