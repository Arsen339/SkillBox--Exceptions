# TODO
# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенной пользователем
# Обернуть код и обработать исключительные ситуации для для произвольных входных параметров
# - ValueError - невозможность преобразовать к числу
# - IndexError - Выход за границы списка
# - Остальные исключения
# - Для каждого типа исключений написать на консоль соотв. сообщения

while True:
    try:
        BRUCE_WILLIS = 42
        input_data = input("Если хочешь что-то сделать, сделай это сам ")
        leeloo = int(input_data[4])
        result = BRUCE_WILLIS * leeloo
        print(f"Leeloo Dallas! Multi-pass # {result}!")
    except ValueError as ve:
        print(f"Невозможно преобразовать к целому числу! Ошибка:{ve}")
    except IndexError as ie:
        print(f"Длина массива составляет меньше 5 элементов! Ошибка:{ie}")
    except BaseException as be:
        # BaseException - обработка всех исключений, для вывода на консоль
        print(f"Ошибка: {be}")
