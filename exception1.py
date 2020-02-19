"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
перехватывала KeyboardInterrupt, писала пользователю "Пока!"
и завершала работу при помощи оператора break
"""


dict_ask = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую",
            "Есть цель?": "Есть", "Два плюс два": 4
            }


def ask_user(dict_ask):
    user_say = ''
    while True:
        try:
            user_say = input("Введи вопрос из списка: ")
            print(f'Пользователь спросил: {user_say}')
            print(f'Программа отвечает: {dict_ask.get(user_say)}')
        except KeyboardInterrupt:
            print()
            print("Пока")
            break
    return 0


if __name__ == "__main__":
    ask_user(dict_ask)
