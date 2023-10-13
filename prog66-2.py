products = []

with open('products.csv', 'r', encoding='utf-8') as f:  #開檔，with最後會自動把檔案關閉
    for line in f:
        name,price = line.strip().split(',')  #讀檔，每一行去掉換行符號，再用,切割，切割完後為清單格式的資料，清單的第1筆資料放到name，清單的第2筆資料放到price
        products.append([name,price])
    print(products)

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name,price])

with open('products.csv', 'w', encoding='utf-8') as f:  #開檔，with最後會自動把檔案關閉
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')  #寫檔

    