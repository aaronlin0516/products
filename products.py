#記帳程式專案(+二維清單)
#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue							#如果符合"商品,價格"就跳到下一迴，以下條件跳過，繼續下一迴處理
		name, price = line.strip().split(',')	#先把多餘的符號清除(strip)再用','切割(split)
		products.append([name,price])
print(products)

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price] #等同上方三行程式
	products.append([name,price]) #等同上方四行程式
print(products) #印出大清單

for p in products:   #印出小清單
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:		#打開檔案寫入products.csv ","可以做分格區分
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 	#用+合併必須為字串
