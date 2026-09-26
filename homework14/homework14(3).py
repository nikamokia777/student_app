import csv

def create_students(n):
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "first_name", "last_name", "age"])
        writer.writeheader()

        for i in range(1, n + 1):
            first = input("First name: ")
            last = input("Last name: ")

            while True:
                try:
                    age = int(input("Age: "))
                    break
                except:
                    print("Enter a number!")

            writer.writerow({
                "ID": i,
                "first_name": first,
                "last_name": last,
                "age": age
            })

create_students(3)