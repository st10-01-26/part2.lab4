from typing import Union
from math import pi

if __name__ == "__main__":
    # Write your solution here
    TYPES_OF_STAIRS = ["straight", "quarter_turn", "half_turner", "circular"]
    class Stair:
        """
        Класс описывает модель лестницы
        """
        def __init__(self, number_of_steps: int, height_of_steps: Union[int, float], width: Union[int, float]):
            """
            Создание и подготовка к работе объекта "Лестница"

            :param number_of_steps: Количество ступеней
            :param height_of_steps: Высота ступеней
            :param width: Ширина лестницы

            Примеры:
            >>> stair = Stair(15, 200, 1000)  # инициализация экземпляра класса
            """
            self.number_of_steps = number_of_steps
            self.height_of_steps = height_of_steps
            self.width = width

        def __str__(self) -> str:
            return f'Лестница с количеством ступененей "{self.number_of_steps}", высота ступеней "{self.height_of_steps}", ширина лестницы "{self.width}"'

        def __repr__(self) -> str:
            return f'Stair(number_of_steps={self.number_of_steps}, height_of_steps={self.height_of_steps},width={self.width})'

        def init_height_of_floor(self) -> Union[int, float]:
            """
            Функция, которая вычисляет высоту этажа

            :return: Высота этажа

            Примеры:
            >>> stair = Stair(15, 200, 1000)
            >>> stair.init_height_of_floor(stair)
            """
            return self.height_of_steps * self.number_of_steps

        def calculate_square(self, type: str, width_of_steps: Union[int, float], width_of_land=None) -> Union[int, float]:
            """
            Функция, которая вычисляет площадь лестницы (корректно выполняется для всех типов лестниц, кроме винтовых)

            :param type: Тип лестницы
            :param width_of_steps: Ширина ступеней
            :param width_of_land: Ширина площадки

            :return: Площадь лестницы

            Примеры:
            >>> stair = Stair(15, 200, 1000)
            >>> stair.calculate_square(stair, "straight", 40, 1000)
            """
            if type not in TYPES_OF_STAIRS:
                raise ValueError(f"Введите тип лестниц из существующих: {TYPES_OF_STAIRS}")
            if type == "circular":
                raise ValueError("Для винтовых лестниц используйте тип данных Circular_Stair и функцию для расчета площади для данного типа лестниц")
            self.width_of_steps = width_of_steps
            if width_of_land == None:
                self.width_of_land = width_of_steps
            else:
                self.width_of_land = width_of_land
            square = width_of_steps * self.number_of_steps * self.width
            return square

        def calculate_width_of_stairway(self, number_of_stairways: int):
            """
            Функция, которая вычисляет ширину одного лестничного марша

            :param number_of_stairways: Количнство лестничных маршей

            :return: Ширина одного лестничного марша

            Примеры:
            >>> stair = Stair(15, 200, 1000)
            >>> stair.calculate_width_of_stairway(stair, 2)
            """
            self.number_of_stairways = number_of_stairways
            return self.width / self.number_of_stairways

    class Circular_Stair(Stair):
        def __init__(self, number_of_steps: int, height_of_steps: Union[int, float], width: Union[int, float], corner: int):
            """
            Создание и подготовка к работе объекта "Винтовая лестница"

            :param number_of_steps: Количество ступеней
            :param height_of_steps: Высота ступеней
            :param width: Ширина лестницы
            :param corner: Угол поворота лестницы

            Примеры:
            >>> stair = Circular_Stair(15, 200, 1000, 360)  # инициализация экземпляра класса
            """
            super().__init__(number_of_steps, height_of_steps, width)
            self.corner = corner

        def __str__(self) -> str:
            return f'Винтовая лестница с количеством ступененей "{self.number_of_steps}", высота ступеней "{self.height_of_steps}", ширина лестницы "{self.width}", угол поворота "{self.corner}"'

        def __repr__(self) -> str:
            return f'Stair(number_of_steps={self.number_of_steps}, height_of_steps={self.height_of_steps},width={self.width})'


        def init_height_of_floor(self):
            """
            Функция, которая вычисляет высоту этажа

            :return: Высота этажа

            Примеры:
            >>> stair = Circular_Stair(15, 200, 1000, 360)
            >>> stair.init_height_of_floor(stair)
            """
            super().init_height_of_floor()

        def calculate_square(self) -> Union[int, float]:
            """
            Функция, которая вычисляет площадь лестницы

            :return: Площадь лестницы

            Примеры:
            >>> stair = Circular_Stair(15, 200, 1000, 360)
            >>> stair.calculate_square(stair)
            """
            return pi * (self.width ** 2)
    pass
