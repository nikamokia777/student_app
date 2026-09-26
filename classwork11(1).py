from faker import Faker
from random import randint

fake = Faker()

def generate_student(number):
    number = int(number)

    info = {
        "ID": number,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": randint(18, 81)
    }

    return info

