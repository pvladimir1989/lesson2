"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def ask_user():

    dct = dict([('Как дела?', 'Хорошо!'), ('Что делаешь?', 'Программирую'), ('Когда ложишься спать?', 'Рано'),
                ('Ты поел?', 'да')])
    # inp=input("Введите вопрос")
    while True:
        try:
            inp = input(" Введите вопрос")
            if inp in dct:
                print(dct.get(inp))
                break
        except KeyboardInterrupt:
            print(' Пока')
            break
if __name__ == "__main__":
    ask_user()
