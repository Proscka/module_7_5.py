import os
from datetime import datetime

directory="."

module_7_5py = os.getcwd()
files_in_dir = os.listdir(module_7_5py)
print(os.getcwd())

for file_name in files_in_dir:
    if os.path.isfile(file_name):
        file_path = os.path.join(module_7_5py,file_name)
        mtime = os.path.getctime(file_name)
        mtime = datetime.fromtimestamp(mtime)
        file_size = os.path.getsize(file_name)
        parent_dir = os.path.dirname(module_7_5py)


        print(f"Обнаружен файл:{file_name},Путь:{file_path}, Размер:{file_size} байт, Время изменения:{mtime}"
              f"Родительская директория:{parent_dir}")

