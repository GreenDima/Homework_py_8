def choice():
    print(
        " 1 - Ввод данных данных\n 2 - Вывод данных\n 3 - Поиск данных\n 4 - Изменение данных\n 5 - Удаление данных\n 6 - Выход из программы"
    )
    return int(input("Выберите нужную команду: "))

def get_data_user():
    return input("Введите данные через пробел (фамилия, имя, номер телефона):\n")

def user_serch():
    return input("Введите для поиска фамилию, имя или номер телефона:\n")
