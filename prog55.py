data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print(len(data))

#for line in data:
    #print(data)
print(data[0].strip())
print('--------------------------------------------------------------')
print(data[1].strip())
print('--------------------------------------------------------------')
print(data[2].strip())
print('--------------------------------------------------------------')
print(data[3].strip())
print('--------------------------------------------------------------')
print(data[4].strip())