
# ----------------------------------------------------------------------------------------
class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

        #  Обращаемся к связанному классу, переопределяется self.sound
        super().__init__()

    def __str__(self):
        return 'Horse'

    def run(self, dx:int):
        self.x_distance += dx
        # return self.x_distance
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def __str__(self):
        return 'Eagle'

    def fly(self, dy:int):
        self.y_distance += dy
        # return self.y_distance
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
class Pegasus(Horse, Eagle):
    
    def __init__(self):
        super().__init__()
        # Eagle.__init__(self)

    def move(self, dx:int, dy:int):

        # Так тоже работает
        # super().run(dx)
        # super().fly(dy)
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
