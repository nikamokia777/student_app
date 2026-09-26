def sum_numbers(times=5):
    total = 0

    for i in range(times):
        num = int(input(f"enter number: "))
        total += num

    return total


result = sum_numbers()
print("sum", result)
