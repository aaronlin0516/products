#記帳程式專案(+二維清單)
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price] #等同上方三行程式
	products.append([name,price]) #等同上方四行程式

print(products)

for p in products:
	print(p)