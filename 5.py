import os
import re


def task1():
    directory = "./test/"
    keyword = "filenames"
    matching_files = []

    # Проходим по всем директориям и файлам, совпадающие по keyword имена файлов добавляются в список
    for root, _, files in os.walk(directory):
        for file in files:
            if keyword in file:
                matching_files.append(os.path.join(root, file))

    # Выводим количество файлов в списке с указанным ключевым словом
    print(f"Number of files containing '{keyword}': {len(matching_files)}")


def task2(directory="./test/"):
    # Задаём паттерн для емейлов
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    email_addresses = []

    # Проходим по всем директориям и файлам, как и в task1()
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Открываем файл и проверяем на совпадение по паттерну email_pattern
            with open(file_path, "r") as f:
                file_content = f.read()
                matches = re.findall(email_pattern, file_content)
                email_addresses.extend(matches)

    # Выводим найденные адреса
    for email in email_addresses:
        print(email)

    # Вызываем task2() рекурсивно на все субдиректории внутри директории
    for root, dirs, _ in os.walk(directory):
        for subdir in dirs:
            subdirectory = os.path.join(root, subdir)
            task2(subdirectory)


def main():
    task1()
    task2()


if __name__ == "__main__":
    main()
