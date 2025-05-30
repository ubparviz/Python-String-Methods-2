# Narxlar ro‘yxatini matnda ko‘rsatish. 
# Mahsulot nomi va narxini matnga joylashtiring.

item = input("Mahsulotni kiriting: ")
price = float(input("Narxini kiriting: "))

massage = "{item} mahsuloti narxi ${price}".format(item=item, price=price)

print(massage)