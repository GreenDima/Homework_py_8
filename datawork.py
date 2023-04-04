def write_data(data_user):
    with open("file.txt", "a") as file:
        file.write(data_user + "\n")

def all_read_data():
    with open("file.txt", "r") as file:
        print(file.read())

def read_data():
    with open("file.txt", "r") as file:
        return file.readlines()

def search(list, str):
    for value in list:
        if str in value:
            print(value)

def delete(delete_data):
    with open("file.txt", "r") as file:
        lines = file.readlines()
        with open('file.txt', 'w') as file_w:
            for line in lines:
                if line.strip('\n') != delete_data:
                    file_w.write(line)
    print("Данные удалены")

def change(change_data):
    with open("file.txt", "r") as file:
        lines = file.readlines()
        with open('file.txt', 'w') as file_w:
            for line in lines:
                if line.strip('\n') != change_data:
                    new_data = input("Введите новые данные: ")
                    change_data = new_data
    print("Данные изменены")