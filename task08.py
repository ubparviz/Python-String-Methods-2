# Bir so‘z bir necha marta qatnashgan bo‘lsa, birinchi indeksni toping 
# Faqat birinchi topilgan joyni chiqaring.

text = input("Matn kiriting: ")
sub_text = input("Matn ichidan bir so'z yozing: ")

indeks = text.find(sub_text)

print(indeks)