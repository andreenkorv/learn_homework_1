"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_age(age=-1):
    while age < 0:
        try:
            age = int(input("Введите возраст: "))
        except ValueError:
            print("Введите простое число")
    return age

def get_job(age):
    if age < 6:
        job = "Детский сад"
    elif age < 18:
        job = "Школа"  
    elif age < 23:
        job = "ВУЗ"
    else:
        job = "Работать!"
    return job

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = get_age()
    job = get_job(age)
    print(job)
    
      
if __name__ == "__main__":
    main()

