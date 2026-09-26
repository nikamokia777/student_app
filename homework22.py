import threading

def number_check(number):
    if number < 2:
        print(f"{number} is not a prime number")
        return

    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

threads = []

for num in num_list:
    thread = threading.Thread(target=number_check, args=(num,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()