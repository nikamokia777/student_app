import json
import random


def load_users():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    return users


def save_users(users):
    with open("./users.json", "w") as file:
        json.dump(users, file, indent=4)


def generate_id(users):
    while True:
        new_id = str(random.randint(100000, 999999))
        unique = True
        for user in users:
            if user["id"] == new_id:
                unique = False
                break
        if unique:
            return new_id


def sign_up():
    users = load_users()
    name = input("Enter your name: ")
    password = input("Create your password: ")
    user_id = generate_id(users)
    new_user = {
        "id": user_id,
        "name": name,
        "password": password,
        "gel": 0,
        "usd": 0,
        "eur": 0,
    }
    users.append(new_user)
    save_users(users)
    print("\nAccount created successfully!")
    print(f"Your ID is {user_id}")


def sign_in():
    users = load_users()
    user_id = input("Enter your ID: ")
    user_password = input("Enter your password: ")

   
    for user in users:
        if user["id"] == user_id:
            if user["password"] == user_password:
                print("Login successful!")
                return user
            else:
                print("Incorrect password!")
                return None

    print("User ID not found!")
    return None


def check_balance(user):
    print(f"GEL: {user['gel']}")
    print(f"USD: {user['usd']}")
    print(f"EUR: {user['eur']}")


def deposit(user):
    users = load_users()

    print("\n1. GEL")
    print("2. USD")
    print("3. EUR")

    choice = input("Choose currency: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid number input!")
        return

    if amount <= 0:
        print("Invalid amount!")
        return

    for u in users:
        if u["id"] == user["id"]:
            if choice == "1":
                u["gel"] += amount
            elif choice == "2":
                u["usd"] += amount
            elif choice == "3":
                u["eur"] += amount
            else:
                print("Invalid choice!")
                return

            save_users(users)
            user.update(u)  
            print("Deposit completed successfully!")
            return


def withdraw(user):
    users = load_users()
    print("\n1. GEL")
    print("2. USD")
    print("3. EUR")

    choice = input("Choose currency: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid number input!")
        return

    if amount <= 0:
        print("Invalid amount!")
        return

    for u in users:
        if u["id"] == user["id"]:
            
            if choice == "1":
                if u["gel"] < amount:
                    print("Insufficient balance in GEL!")
                    return
                u["gel"] -= amount
            elif choice == "2":
                if u["usd"] < amount:
                    print("Insufficient balance in USD!")
                    return
                u["usd"] -= amount
            elif choice == "3":
                if u["eur"] < amount:
                    print("Insufficient balance in EUR!")
                    return
                u["eur"] -= amount
            else:
                print("Invalid action!")
                return

            save_users(users)
            user.update(u)  
            print("Withdrawal completed successfully!")
            return


def atm_menu(user):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Log Out")

        choice = input("Choose: ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit(user)
        elif choice == "3":
            withdraw(user)
        elif choice == "4":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n===== ATM =====")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            user = sign_in()
            if user:
                atm_menu(user)
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()