import json

def add_person(count):
    with open("persons.json", "r") as file:
        people = json.load(file)

    last_id = people[-1]["id"]

    for i in range(count):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        people.append({
            "id": last_id + 1,
            "name": name,
            "age": age
        })

        last_id += 1

    with open("persons.json", "w") as file:
        json.dump(people, file, indent=4)

add_person(2)