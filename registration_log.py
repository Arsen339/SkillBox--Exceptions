# TODO
# Есть файл с протоколом регистрации пользователей на сайте registrations.txt
# Каждая строка содержит имя, емайл, Возраст, разделенные пробелом
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутствуют все 3 поля
# - поле имени содержит только буквы
# - поле имейл содержит только @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать 2 файла:
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки
#
# Для валидизации строки данных написать метод, который может выкидывать исключения:
# - Не присутствуют все 3 поля: ValueError
# - Поле имени содержит НЕ только буквы(кастомное исключение)
# - поле емайл не содержит @ и .(кастомное исключение)
# - поле возраст не является числом от 10 до 99
# Вызов метода обернуть в try-except

# Блок классов
class UserNameError(Exception):
    """Ошибка ввода имени"""
    def __init__(self, message="UserNameError!!"):
        self.message = message

    def __str__(self):
        return self.message


class MailError(Exception):
    """Ошибка ввода емайла"""
    def __init__(self, message="MailError!!"):
        self.message = message

    def __str__(self):
        return self.message

class AgeValueError(Exception):
    """Ошибка ввода возраста: возраст не число"""
    def __init__(self, message="AgeValueError!!"):
        self.message = message

    def __str__(self):
        return self.message


class AgeError(Exception):
    """Ошибка ввода возраста: возраст не попадает в рамки"""
    def __init__(self, message="AgeError!!"):
        self.message = message

    def __str__(self):
        return self.message


# Блок функций
def name_check(name_value):
    """Проверка имени"""
    for letter in name_value:
        if letter.isalpha() == 0:
            raise UserNameError

def email_check(email_value):
    """Проверка емайла"""
    if "." not in email_value or "@" not in email_value:
        raise MailError


def age_scale_check(age_value):
    """Проверка возраста"""
    if age_value < 10 or age_value > 99:
        raise AgeError


def age_value_check(age_value):
    """Проверка возраста на принадлежность к числам"""
    if not age_value.isdigit():
        raise AgeValueError


# открытие файлов
file_name = "registrations.txt"
file = open(file_name, mode='r', encoding="utf8")

error_file_name = "registrations_bad.txt"
error_file = open(error_file_name, mode="w")

correct_file_name = 'registrations_good.txt'
correct_file = open(correct_file_name, mode='w')

# основной цикл
for line in file:
    try:
        print(line, end='')
        name, email, age = line.split(" ")
        age = age[:-1]
        name_check(name)
        email_check(email)
        age_value_check(age)
        age = int(age)
        age_scale_check(age)
    except ValueError as ve:
        error_file.write(line[:-1] + ' ' + f" {ve}\n")
        print(f"Не 3 поля, тип ошибки: {ve} \n")
    except UserNameError as une:
        error_file.write(line[:-1] + ' ' + f"{une}\n")
        print(f"Имя пользователя содержит не только буквы! тип ошибки: {une}\n")
    except MailError as me:
        error_file.write(line[:-1] + ' ' + f"{me}\n")
        print(f"Ошибка! Емайл должен содержать . и @!\n")
    except AgeError as ae:
        error_file.write(line[:-1] + ' ' + f"{ae}\n")
        print(f"Возраст должен быть числом, от 10 до 99! Тип ошибки: {ae}\n")
    except AgeValueError as ave:
        error_file.write(line[:-1] + ' ' + f"{ave}\n")
        print(f"Возраст должен быть числом! Тип ошибки: {ave}\n")
    except BaseException as be:
        error_file.write(line[:-1] + ' ' + f"{be}\n")
        print(f"Ошибка! Тип ошибки: {be}\n")
    else:
        print("It is OK!\n")
        correct_file.write(line)

# закрытие файлов
file.close()
correct_file.close()
error_file.close()