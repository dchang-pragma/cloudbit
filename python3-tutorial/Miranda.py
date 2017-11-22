class Rabbit:
    """A simple example class"""
    genus='Oryctolagus'
    specie='cuniculus'
    #tricks=[] #class variable
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color #instance variable
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)



bunny1 = Rabbit('Mocha', 'Holland Lop', 'chestnut')
bunny2 = Rabbit('Tofu', 'Netherlands Dwarf', 'white')
bunny3 = Rabbit('Sesame', 'Netherlands Dwarf', 'black')
# bunny4 = Rabbit('Fluffy')
# bunny5 = Rabbit('Ray')
# bunny6 = Rabbit('Brownie')
# bunny1.breed = 'Holland Lop'

bunny1.add_trick('play cute')

bunny2.add_trick('growl gu gu')


print ('name of bunny 1 is', bunny1.name, '.','he can', bunny1.tricks[0])
#print (bunny2.tricks)
#print(bunny3.name)
#print(bunny1.breed)

print(bunny1.name, bunny1.breed)




#print("Miranda Tofu and Mocha is cute")
# chang
# rabbit1="Mocha"
# rabbit2="Mochi"
# rabbit="Miranda"
# rabbit1ageInMonths=6
# rabbit2ageInMonths=18

# print("i have two rabbits")
# print("first one is called",rabbit2)
# print("second one is called",rabbit)
# print(rabbit1+rabbit2)
# print("first rabbit age in months is",rabbit1ageInMonths)
# print("second rabbit age in months is",rabbit2ageInMonths)
# print("their total age in months is",rabbit1ageInMonths+rabbit2ageInMonths)
# print(rabbit1ageInMonths,rabbit2ageInMonths)