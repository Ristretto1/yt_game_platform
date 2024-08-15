# ФУНКЦИИ
# Проверка возраста
def validate_age(age: int) -> str:
    if age <= 0:
        return 'Ошибка: Возраст не может быть отрицательным или равен нулю'
    elif age < 14:
        return 'Ошибка: Минимальный возраст — 14 лет.'


# Проверка имени
def validate_name(name: str) -> str:
    if len(name) == 0:
        return 'Ошибка: Пустое имя.'
    elif len(name) < 3:
        return 'Ошибка: В имени должно быть минимум 3 символа.'
    elif name.count(' ') > 1:
        return 'Ошибка: Допустимое кол-во пробелов в имени - 1'


# Совет по паспорту
def advise_change_passport(age: int) -> str:
    if 16 <= age <= 17:
        return 'Нужно не забыть получить первый паспорт.'
    elif 25 <= age <= 26:
        return 'Нужно не забыть заменить паспорт.'
    elif 45 <= age <= 46:
        return 'Нужно не забыть второй раз заменить паспорт.'
    else:
        return ''


# Собственная реализация ''.strip()
def custom_strip(text: str) -> str:
    while text and text[0] == ' ':
        text = text[1:]
    while text and text[-1] == ' ':
        text = text[:-1]
    return text


def main():
    input_name = custom_strip(input('Введите Ваше имя:'))
    input_age = int(input('Введите Ваш возраст:'))

    error_age = validate_age(input_age)
    error_name = validate_name(input_name)

    if error_age or error_name:
        print(error_age or error_name)
        main()
    else:
        print(f'Привет, {input_name.title()}! Тебе {input_age} лет. {advise_change_passport(input_age)}')


main()
