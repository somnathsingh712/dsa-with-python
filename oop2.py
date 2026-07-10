class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=100000

    def get_desc(self):
        desc_name=f"{self.make} {self.model} {self.year}"
        return desc_name
    
    def reading(self):
        print(f"the car has run {self.odometer} miles")

    def check(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print("You cant roll back odometer")

    def increment(self,miles):
        self.odometer+=miles

newcar=car('skoda','rapid',2019)
print(newcar.get_desc())
newcar.increment(20000)
newcar.reading()