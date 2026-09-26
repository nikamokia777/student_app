with open('persons.txt', 'r') as file, \
     open('under_50.txt', 'w') as under_50, \
     open('over_50.txt', 'w') as over_50:

    for line in file:
        parts = line.strip().split(',')

        age = int(parts[1])

        if age < 50:
            under_50.write(line)

        elif age > 50:
            over_50.write(line)