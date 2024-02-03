class Recipes():

    def __int__(self, dish, items, time):
        self.dish=dish
        self.items=items
        self.time=time

    def contents(self):
        print("The " + self.dish +" has " + str(self.items) + "\
         and takes " + str(self.time) + " min to prepare")

pizza =Recipes("Pizza", ["Cheese", "Bread", "Tomato"], 45)
pasta=Recipes("Pasta", ["penne", "sauce"], 55)

print(pasta.items)
print(pizza.items)
