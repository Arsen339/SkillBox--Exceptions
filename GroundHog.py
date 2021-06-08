# TODO
# День сурка
# Напишите функцию one_day(), которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# - Одно из этих исключений выыбрасывается с вероятностью 1 к 13 каждый день
# Функцию оберните в бесконечный цикл, выход из которого возможен
# только после накопления кармы больше чем ENLIGHTENMENT_CARMA_LEVEL
# Исключения обработать и записать в лог

# Импортируем функцию для генерации вероятности 1 к 13 и 1 к 7
from random import randint

# Откроем файл
file_name = 'log.txt'
file = open(file_name, mode="w")

def dice():
    """dice - игральная кость, вероятность 1/13
    """
    fate = randint(1, 13)
    if fate == 13:
        return True

def one_day():
    """Возвращает число от 1 до 7"""
    return randint(1, 7)

# Создадим калссы для ошибок
class IamGodError(Exception):

    def __init__(self, message="IamGodError"):
        self.message = message

    def __str__(self):
        return self.message

class DrunkError(Exception):

    def __init__(self, message="DrunkError"):
        self.message = message

    def __str__(self):
        return self.message

class CarCrushError(Exception):

    def __init__(self, message="CarCrushError"):
        self.message = message

    def __str__(self):
        return self.message

class GluttonyError(Exception):

    def __init__(self, message="GluttonyError"):
        self.message = message

    def __str__(self):
        return self.message
class DepressionError(Exception):

    def __init__(self, message="DepressionError"):
        self.message = message

    def __str__(self):
        return self.message

class SuicideError(Exception):

    def __init__(self, message="SuicideError"):
        self.message = message

    def __str__(self):
        return self.message


# consts
ENLIGHTENMENT_CARMA_LEVEL = 100
# increments
carma = 0
day_counter = 0

# main
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    day_counter += 1
    carma += one_day()

    print(f"day: {day_counter}")
    print("Carma: ", carma)

    file.write("Day: " + str(day_counter) + "\n")
    file.write("carma: " + str(carma) + "\n")
    # Обработка исключений
    try:
        if dice():
            carma -= 1
            raise SuicideError("SuicideError")
        if dice():
            carma -= 1
            raise DepressionError("DepressionError")
        if dice():
            carma -= 1
            raise GluttonyError("GluttonyError")
        if dice():
            carma -= 1
            raise CarCrushError("CarCrushError")
        if dice():
            carma -= 1
            raise DrunkError("DrunkError")
        if dice():
            carma -= 1
            raise IamGodError("IamGodError")
    except BaseException as be:
        file.write(f"{be}" + "\n")
        print(f"Error is {be}")

print("Days: ", day_counter)

file.write("Days amount: " + str(day_counter))
file.close()