class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


def person_serializer(person: Person):
    return f"Name: {person.name}, Age: {person.age}"


def person_deserialize(text):
    name_part, age_part = text.split(',')
    name = name_part.split(':', 1)[1].strip()
    age = int(age_part.split(':', 1)[1].strip())
    return Person(name, age)


p1 = Person("Otar", 35)

with open('persons.txt', 'w') as file:
    file.write(person_serializer(p1))

with open('persons.txt', 'r') as file:
    data = file.readline()

new_person = person_deserialize(data)

print(new_person)