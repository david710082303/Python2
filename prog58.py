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

new = [d for d in data if len(d)<100]
print('一共有', len(new), '筆留言長度小於100')

good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言包含good')

print('--------------------------------------------------------------')
print(new[0].strip())
print('--------------------------------------------------------------')
print(new[1].strip())
print('--------------------------------------------------------------')
print(new[2].strip())
print('--------------------------------------------------------------')
print(good[0].strip())
print('--------------------------------------------------------------')
print(good[1].strip())
print('--------------------------------------------------------------')
print(good[2].strip())