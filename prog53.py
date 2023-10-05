data = []

with open('prog53.txt', 'r') as f:
    for line in f:
        print(line)
        data.append(line.strip())

print(data)