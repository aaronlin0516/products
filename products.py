#記帳程式專案(+二維清單)
import os #operating system 作業系統
#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue							#如果符合"商品,價格"就跳到下一迴，以下條件跳過，繼續下一迴處理
				name, price = line.strip().split(',')	#先把多餘的符號清除(strip)再用','切割(split)
				products.append([name,price])
	return products
#寫入檔案
def user_input(products):
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
	return products
#印出小清單
def print_products(products):
	for p in products:   
		print(p[0], '的價格是', p[1])
#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:		#打開檔案寫入products.csv ","可以做分格區分
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') 	#用+合併必須為字串

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #isfile檢查檔案
		print('yeah!找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案.....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
