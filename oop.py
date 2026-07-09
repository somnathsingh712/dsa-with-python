class game:
    def __init__(self,name,genre):
        self.name="eldenring"
        self.genre="souls"

    def plateform(self,*plateforms):
        print(f"Plateforms: {plateforms}")

    def award(self,year):
        print(f"Game of the year {year}")


game1=game("EldenRing","Souls")
game1.plateform("PS5","Xbox","PC")
game1.award(2022)




game2=game("gta vi","Open-World")
game2.plateform("PS5")
game2.award(2026)

