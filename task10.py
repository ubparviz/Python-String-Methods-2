# Topilmagan so‘zlar uchun -1 natija berilishini tushuning 
# find() orqali mavjud bo‘lmagan so‘zni qidiring.

text = input("Matn kiriting: ")
word = input("Matn ichida bo'lmagan so'z yozing: ")

index = text.find(word)

print(index)