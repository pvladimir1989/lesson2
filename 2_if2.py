"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    a = input("row1")
    b = input("row2")

    def two_rows(a, b):
        c = "это строки"
        if isinstance(a, str) == True and isinstance(b, str) == True:
            if a == b:
                return 1
            elif a != b and len(a) > len(b):
                return 2
            elif a != b and b == "Learn":
                return 3

        else:
            return 0

    print(two_rows(a, b))


if __name__ == "__main__":
    main()
