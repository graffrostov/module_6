# ---------------------------------------------------------------------------------------------------------
from math import pi, sqrt

class Figure:
    sides_count = 0


    def __init__(self, colors:tuple, *sides:int):

        # Проверяем на корректность цветов
        if (isinstance(colors, tuple)
                and len(colors)==3
                and self.__is_valid_color(*colors)):
            self.__color = list(colors)

        # Проверяем на корректность сторон
        # Если передана одна сторона, то используем её для всех
        # Иначе устанавливаем единичную сторону
        # Для существующего куба можно передать невозможные стороны-------------------------------
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        elif len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0:
            self.__sides = [sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

        # Окраска. В задании не используется
        self.filled = False


    # Возвращаем цвет
    def get_color(self):
        return self.__color

    # Возвращаем стороны фигуры
    def get_sides(self):
        return self.__sides

    # Проверяем цвет на корректность
    def __is_valid_color(self, r:int, g:int, b:int):

        valid = range(256)

        return (r in valid) and (g in valid) and (b in valid)

    # Проверяем на соответствие стороны по количеству, на целочисленность и размер.
    # Для созданного куба требуется доработка. Можно прописать неподходящие стороны------------------------
    def __is_valid_sides(self, *sides:int):

        if len(sides) != self.sides_count:
            return False

        for side_len in sides:

            if not isinstance(side_len, int) and side_len <= 0:
                return False

        return True

    # Устанавливаем новый цвет
    def set_color(self, r:int, g:int, b:int ):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Устанавливаем новые стороны
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        elif len(new_sides) == 1:
            self.__sides = [new_sides[0]] * self.sides_count

    # Возвращаем периметр
    def __len__(self):
        return sum(self.__sides)


# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
class Circle(Figure):
    sides_count = 1

    # Создаём окружность
    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)

        # Вычисляем радиус
        self.__radius = self.get_sides()[0] / pi / 2


    # Считаем площадь круга из окружности
    def get_square(self):
        return (self.get_sides()[0] ** 2) / (4* pi)
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
class Triangle(Figure):
    sides_count = 3

    # Создаём треугольник
    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)

    # Считаем площадь по формуле Герона
    def get_square(self):

        p = len(self) / 2
        a, b, c = self.get_sides()

        return sqrt(p * (p - a) * (p - b) * (p - c))
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
class Cube(Figure):
    sides_count = 12

    # Создаем куб. Есть недоработка. Если для существующего куба передать 12 разных сторон, -------------
    # то они будут прописаны.----------------------------------------------------------------------------
    # Хотя у куба все стороны должны быть равны.
    def __init__(self, colors, *sides):
        if len(sides) != 1:
            super().__init__(colors, *((1,) * self.sides_count))
        else:
            super().__init__(colors, *sides)
    # Вычисляем объём. Берем первую сторону и вычисляем по ней
    # Смотри ошибку выше, можно создать невозможную фигуру
    def get_volume(self):
        return self.get_sides()[0] ** 3
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
# ---------------------------------------------------------------------------------------------------------

# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216

# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

circle_2 = Circle((170, 200, 100), 10, 15, 6)
triangle_2 = Triangle((200, 150, 100), 10, 6)
cube_2 = Cube((200, 200, 50), 9)
cube_3 = Cube((100, 200, 100), 9, 12)
print()
print(circle_2.get_color())
print(triangle_2.get_color())
print(cube_2.get_color())
print(cube_3.get_color())

print()
print(len(circle_2))
print(len(triangle_2))
print(len(cube_2))
print(len(cube_3))

print()
print(circle_2.get_sides())
print(triangle_2.get_sides())
print(cube_2.get_sides())
print(cube_3.get_sides())

print()
print(circle_2.get_square())

print()
print(triangle_2.get_square())

print()
print(cube_2.get_volume())
print(cube_3.get_volume())

cube_2.set_sides(3)
print(cube_2.get_volume())

# Созданному кубу получается назначить невозможные стороны
cube_2.set_sides(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12)
print(cube_2.get_sides())
print(cube_2.get_volume())

cube_4 =Cube((100, 200, 100), 8, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12)
print(cube_4.get_sides())



