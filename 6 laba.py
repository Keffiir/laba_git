# 15. Написать программу для вычисления общего размера каталога и его подкаталогов.
# Вывести в текстовом файле иерархию каталогов с их размером.
import os

def get_subdirectories(directory):
    # Возвращаем список названий подкаталогов для заданого каталога
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

main_directory = '/Users/nikiforovivan/Desktop/УЧЕБА ВУЗ/Инфа/newcatalog/'
# Создаем файл info.txt в основном каталоге
info_file = open(os.path.join(main_directory, "info.txt"), "w+")
# Записываем в файл info.txt называние основного каталога и его вес
info_file.write(str(os.path.dirname(main_directory)) + " " + str(os.path.getsize(main_directory)) + " bytes" + "\n")
# В цикле for проходимся по всем названиям подкаталогов
for file in get_subdirectories(main_directory):
    # Создаем полный путь для каждого из названий подкаталогов
    current_path = os.path.join(main_directory, file)
    # Записываем в файл info_file название подкаталога и его размер
    info_file.write("  - " + file + " " + str(os.path.getsize(current_path)) + " bytes" + "\n")
