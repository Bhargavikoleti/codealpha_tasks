import os
import shutil
path = input("Enter folder path: ")
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        extension = file.split(".")[-1].lower()
        destination_folder = os.path.join(
            path,
            extension.upper()
        )
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
        shutil.move(
            file_path,
            os.path.join(destination_folder, file)
        )
print("Files organized successfully!")