data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('讀取完了，總共有', len(data), '筆資料')

for d in data:
    sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len / len(data))

print('--------------------------------------------------------------')
print(data[0].strip())
print('--------------------------------------------------------------')
print(data[1].strip())
print('--------------------------------------------------------------')
print(data[2].strip())
print('--------------------------------------------------------------')
print(data[3].strip())
print('--------------------------------------------------------------')
print(data[4].strip())