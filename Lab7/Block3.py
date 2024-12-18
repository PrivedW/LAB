import os

def list_directory(path):
    try:
        if not os.path.exists(path):
            print(f"Директория {path} не существует.")
            return

        files_and_dirs = os.listdir(path)
        if not files_and_dirs:
            print(f"Директория {path} пуста.")
        else:
            print(f"Содержимое директории {path}:")
            for item in files_and_dirs:
                print(item)
    except Exception as e:
        print(f"Ошибка: {e}")

def create_file(path, name):
    try:
        full_path = os.path.join(path, name)
        if os.path.exists(full_path):
            print(f"Файл {full_path} уже существует.")
        else:
            with open(full_path, 'w') as f:
                f.write('')  
            print(f"Файл {full_path} создан.")
    except Exception as e:
        print(f"Ошибка: {e}")

def create_directory(path, name):
    try:
        full_path = os.path.join(path, name)
        if os.path.exists(full_path):
            print(f"Папка {full_path} уже существует.")
        else:
            os.makedirs(full_path)
            print(f"Папка {full_path} создана.")
    except Exception as e:
        print(f"Ошибка: {e}")

def delete_file(path, name):
    try:
        full_path = os.path.join(path, name)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            os.remove(full_path)
            print(f"Файл {full_path} удалён.")
        else:
            print(f"Файл {full_path} не существует.")
    except Exception as e:
        print(f"Ошибка: {e}")

def delete_directory(path, name):
    try:
        full_path = os.path.join(path, name)
        if os.path.exists(full_path) and os.path.isdir(full_path):
            os.rmdir(full_path) 
            print(f"Папка {full_path} удалена.")
        else:
            print(f"Папка {full_path} не существует или не пуста.")
    except Exception as e:
        print(f"Ошибка: {e}")



while True:
    print("Доступные команды:")
    print("1. Раскрыть директорию (Введите 'list путь_к_директори')")
    print("2. Создать файл (Введите 'create_file путь_к_директории имя_файла')")
    print("3. Создать папку (Введите 'create_directory путь_к_директории имя_папки')")
    print("4. Удалить файл (Введите 'delete_file путь_к_директории имя_файла')")
    print("5. Удалить папку (Введите 'delete_directory путь_к_директории имя_папки')")
    print("6. Выйти (Введите 'exit')")
    
    command = input("Введите команду: ").strip().lower()
    if command.startswith('list'):
        parts = command.split()
        if len(parts) == 2:
            list_directory(parts[1])
        else:
            print("Некорректная команда. Используйте 'list путь_к_директории'.")

    elif command.startswith('create_file'):
        parts = command.split()
        if len(parts) == 3:
            path, name = parts[1], parts[2]
            create_file(path, name)
        else:
            print("Некорректная команда. Используйте 'create_file путь_к_директории имя_файла'.")

    elif command.startswith('create_directory'):
        parts = command.split()
        if len(parts) == 3:
            path, name = parts[1], parts[2]
            create_directory(path, name)
        else:
            print("Некорректная команда. Используйте 'create_directory путь_к_директории имя_папки'.")

    elif command.startswith('delete_file'):
        parts = command.split()
        if len(parts) == 3:
            path, name = parts[1], parts[2]
            delete_file(path, name)
        else:
            print("Некорректная команда. Используйте 'delete_file путь_к_директории имя_файла'.")

    elif command.startswith('delete_directory'):
        parts = command.split()
        if len(parts) == 3:
            path, name = parts[1], parts[2]
            delete_directory(path, name)
        else:
            print("Некорректная команда. Используйте 'delete_directory путь_к_директории имя_папки'.")

    elif command == 'exit':
        print("Выход из программы.")
        break

    else:
        print("Неизвестная команда.")


