import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
file_name = "person_name.json"
try:
    with open(file_name) as file_object:
        user_name = json.load(file_object)

except FileNotFoundError:
    users_name  = input("please enter your name:")
    name = users_name.split()
    for user_name in name:
        with open(file_name,"w") as file_object:
            contens = file_object
            json.dump(user_name,contens)
            print("We'll remember you when you come back, " + user_name.title() + "!")

else:
    print("Welcome back, " + user_name.title() + "!")

