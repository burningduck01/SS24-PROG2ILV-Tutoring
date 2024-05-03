import json

with open("flowers.json", "r") as file_json:
    data = json.load(file_json)

with open("flowers.txt", "w") as file_txt:
    for key, value in data.items():
        msg = f"{key}: {value}\n"
        file_txt.write(msg)