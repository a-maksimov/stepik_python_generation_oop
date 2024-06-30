def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл не найден')