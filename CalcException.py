total = 0
def calc(line):
        print(f"Read line {line}", flush=True)  # flush-вывод сразу после команды print без буферизации
        operand1, operation, operand2 = line.split(" ")  # разбиение на пробелы
        if operation == "+":
            value = int(operand1) + int(operand2)
        elif operation == "-":
            value = int(operand1) - int(operand2)
        elif operation == "*":
            value = int(operand1) * int(operand2)
        elif operation == "/":
            value = int(operand1) / int(operand2)
        elif operation == "//":
            value = int(operand1) // int(operand2)
        elif operation == "%":
            value = int(operand1) % int(operand2)
        else:
            print(f"Unknown operand {operation}")
            value = None
        print("value is ", value)
        return value


with open("calc.txt", 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            total += calc(line)
        except ZeroDivisionError as zde:
            print(f"На ноль делить запрещено! {zde}")
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f"Не хватает операндов {exc}")
            else:
                print(f"Не могу преобразовать к целому {exc}")
        except TypeError as tex:
            print(f"Ошибка типа {tex}")



print(f"Total {total}")