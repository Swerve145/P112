import os
import shutil

from_dir = "C:/Users/sahis_i/Downloads"
to_dir = "C:/Users/sahis_i/Desktop/D_files"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    print(ext)
    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Result"
        path3 = path2 + "/" + file_name

        if os.path.exists(path2):
            print("Moving..." + file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving..." + file_name)
            shutil.move(path1, path3)