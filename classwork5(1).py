try:
    age = int(input("შეიყვანეთ ასაკი: "))

    if age < 0:
        raise Exception("ასაკი უარყოფითი ვერ იქნება!")

except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი!")

except Exception as e:
    print(e)

else:
    if age < 18:
        print("არასრულწლოვანი")
    else:
        print("სრულწლოვანი")