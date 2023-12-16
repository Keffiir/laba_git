# 15. Написать программу для вычисления общего размера каталога и его подкаталогов.
# Вывести в текстовом файле иерархию каталогов с их размером.
import shutil
import os

def get_subdirectories(directory):
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

total_size = 0
main_directory = '/Users/nikiforovivan/Desktop/УЧЕБА ВУЗ/Инфа/newcatalog/'
my_file = open(os.path.join(main_directory, "info.txt"), "w+")
for file in get_subdirectories(main_directory):
    current_path = os.path.join(main_directory, file)
    my_file.write(file + " " + str(os.path.getsize(current_path)) + "bit" + "\n")
    total_size += os.path.getsize(current_path)

print(total_size)
