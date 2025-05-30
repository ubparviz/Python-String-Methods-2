# Topilmagan so‘zlar uchun -1 natija berilishini tushuning 
# find() orqali mavjud bo‘lmagan so‘zni qidiring.

text = input("Matn kiriting: ")
sub_text = input("Matn ichida bo'lmagan so'z yozing: ")

index_text = text.find(sub_text)

print(index_text)