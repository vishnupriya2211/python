class SuperHero:
    name:str

    suit:str
    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
    
    def __str__(self):
        return self.name
    
class MinnalMurali(SuperHero):
    def __init__(self,name,suit):
        super().__init__(name,suit)

    def super_power(self):
        print("running","jumping","reflex")

MinnalMurali_instance1=MinnalMurali("minnalmurali","minnalmurali")

MinnalMurali_instance1.super_power()

print(MinnalMurali_instance1)
        