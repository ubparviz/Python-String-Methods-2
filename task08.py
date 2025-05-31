# Bir so‘z bir necha marta qatnashgan bo‘lsa, birinchi indeksni toping 
# Faqat birinchi topilgan joyni chiqaring.

text = input("Matn kiriting: ")
word = input("Matn ichidan bir so'z yozing: ")

index = text.find(word)

print(index)