from user_view import *
from datawork import *
while True:
    user = choice()
    match user:
        case 1:
            data_user = get_data_user()
            write_data(data_user)
        case 2:
            print(''.join(read_data()))
        case 3:
            list = read_data()
            str = user_serch()
            search(list, str)
        case 4:
            list = read_data()
            str = user_serch()
            search(list, str)
            change_data = input("Введите полные данные в котором хотите сделать изменение:\n ")
            change(change_data)
        case 5:
            list = read_data()
            str = user_serch()
            search(list, str)
            delete_data = input("Введите полные данные которые хотите удалить:\n ")
            delete(delete_data)

        case 6: break