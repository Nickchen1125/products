import os
# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='UTF-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name , price = line.strip().split(',')
			products.append([name,price])
			
	return products

# 輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name,price])
	print(products)
	return products # 因為有append
# 印出購買紀錄
def print_products(products): # function為一封包內部需輸入參數
	for p in products:
		print(p[0], '的價格是', p[1])
# 寫入資料
def write_file(filename,products):
	with open(filename, 'w', encounding='UTF-8') as f: 
		f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
	
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('已找到檔案')
		products = read_file(filename) #有return,function的結果就可存下來
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv',products)
main()