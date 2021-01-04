import json

users_name = input("Please enter your name:")
file_names = "users_name.json"
name = users_name.split()

for user_name in name:
    with open(file_names,"w") as file_object:
        contens = file_object
        json.dump(user_name,contens)
        print("We'll remember you when you come back: " + user_name.title() + "!")