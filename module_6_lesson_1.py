

# -----------------------------------------------------------------------------------------------------
class Animal():

    def __init__(self, name:str, alive:bool = True, fed:bool = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food:object):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

# -----------------------------------------------------------------------------------------------------
class Mammal(Animal):
    pass


class Predator(Animal):
    pass
# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------
class Plant():

    def __init__(self, name:str, edible:bool = False):
        self.name = name
        self.edible = edible

# -----------------------------------------------------------------------------------------------------
class Flower(Plant):
    pass

class Fruit(Plant):

    def __init__(self, name:str, edible:bool = True):
        Plant.__init__(self, name, edible)
# -----------------------------------------------------------------------------------------------------

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)