# USing Class (OOP)
class PartyAnimal:
    def __init__(self):
        self.x=0

    def party(self):
        self.x=self.x+1
        print("So far:", self.x)

an= PartyAnimal()

an.party()
an.party()
an.party()


# Using dir()
class PartyAnimal:
    def __init__(self):
        self.x=0

    def party(self):
        self.x=self.x+1
        print("So Far",self.x)

an=PartyAnimal()

print("Type:", type(an))
print("Dir:", dir(an))
print("Type:", type(an.x))
print("Type",type(an.party))
    
