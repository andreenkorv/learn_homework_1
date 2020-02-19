"""

Домашнее задание №1

Цикл
* Создать список из десяти целых чисел.
* Вывести на экран каждое число, увеличенное на 1.
"""


def print_increment_list(num_list):
    for i in num_list:
        print(i+1)
    return 0


"""
Цикл
* Ввести с клавиатуры строку.
* Вывести эту же строку вертикально: по одному символу на строку консоли.

"""


def print_string(string):
    for i in string:
        print(i)
    return 0


"""
Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def print_medium_raiting(student):
    all_raiting = 0.0
    all_count = 0
    for dictionary in student:
        class_raiting = 0
        class_count = 0
        class_name = dictionary.get('School class')
        for i in dictionary.get('scores'):
            class_raiting += i
            class_count += 1
        class_average = float(class_raiting)/float(class_count)
        all_raiting += class_average
        all_count += 1
        print(
            f'Класс: {class_name}, cумма баллов: {class_raiting}, всего баллов: {round(class_count, 2)}, средний бал: {round(class_average, 2)}'
            )
    print(f'Средний бал по школе: {round(all_raiting / all_count , 2)}')
    return 0


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    student = [
                {'School class': '1a', 'scores': [3, 2, 1, 2, 3, 4]},
                {'School class': '2a', 'scores': [4, 5, 2, 3, 4, 2, 5]},
                {'School class': '3a', 'scores': [5, 2, 3, 3, 4, 2, 5, 4, 2]}
                ]
    print_medium_raiting(student)
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_increment_list(num_list)
    string = "Строка"
    print_string(string)


if __name__ == "__main__":
    main()
