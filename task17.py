# Parol kamida 1 ta raqamdan iboratmi? 
# Ro‘yxatdan o‘tishda isdigit() orqali raqam mavjudligi tekshiriladi.

parol = input("Parol kiriting: ")

check_parol = any(map(str.isdigit, parol))

print(check_parol)