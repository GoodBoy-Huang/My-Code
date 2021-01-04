import json

numbers = [2,3,5,7,11,13]
file_mame = "numbers.json"

with open(file_mame,"w") as file_project:
    json.dump(numbers,file_project)