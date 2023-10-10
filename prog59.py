import random

range(5)  #[0, 1, 2, 3, 4]，range()：清單產生器，Python內建功能
range(3)  #[0, 1, 2]

for i in range(3):
    print(i)

for i in range(3):
    print('hi')

for i in range(100):
    r = random.randint(1, 100)
    print('這是第', i+1,'次產生隨機數：', r)
