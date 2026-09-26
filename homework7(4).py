persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33), 
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Alex', 'White', 42),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]
while True:
    name = input("enter name ")

    if name == "stop":
        break

    name_found = False

    for person in persons:
        if person[0] == name:
            name_found = True
            break

    if not name_found:
        print("there is no such name")
        continue

    surname = input("enter surname ")

    if surname == "stop":
        break

    person_found = False

    for person in persons:
        if person[0] == name and person[1] == surname:
            print("age", person[2])
            person_found = True
            break

    if not person_found:
        print("no such surname")