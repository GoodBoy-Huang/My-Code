file_name = "Document/Pi.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

Pi_string = ""
for line in lines:
    Pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy:")

if birthday in Pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
