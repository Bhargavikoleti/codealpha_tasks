import re

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    text
)

with open("emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Emails extracted successfully!")