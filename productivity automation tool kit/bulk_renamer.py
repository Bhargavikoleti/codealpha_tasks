import os

path = input("Enter folder path: ")

prefix = input("Enter prefix name: ")

count = 1

for file in os.listdir(path):

    old_name = os.path.join(path, file)

    extension = os.path.splitext(file)[1]

    new_name = os.path.join(
        path,
        f"{prefix}_{count}{extension}"
    )

    os.rename(old_name, new_name)

    count += 1

print("Files renamed successfully!")