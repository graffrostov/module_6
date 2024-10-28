# ------------------------------------------------------------------------------------------------------
class Vehicle():

# разрешённые цвета указаны в нижнем регистре.
    __COLOR_VARIANTS =['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner:str, model:str, colors:str, engine_power:int):
        self.owner = owner
        self.__model = model
        self.__colors = colors.lower()
        self.__engine_power = engine_power

    def __str__(self):
        return self.__model

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__colors}'

    def get_owner(self):
        return f'Владелец: {self.owner}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())

        # Можно заменить на метод get_owner
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):

        # список __COLOR_VARIANTS содержит цвета в нижнем регистре
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__colors = new_color.lower()

        else:
            print(f'Нельзя сменить цвет на {new_color}')
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
class Sedan(Vehicle):

    def __init__(self, owner:str, model:str, colors:str, engine_power:int):
        Vehicle.__init__(self, owner, model, colors, engine_power)
        self.__PASSENGERS_LIMIT = 5
# ------------------------------------------------------------------------------------------------------



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
# vehicle1.colors = 'White'
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()