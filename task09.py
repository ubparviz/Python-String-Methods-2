# Belgilarni qayerdan boshlab qidirishni aniqlang find() metodiga start pozitsiyasi bilan ishlang.

text = input("Matn kiriting: ")
sub_text = input("Matn ichidan bir so'z yozing: ")
num = int(input("Raqam kiriting: "))

indeks = text.find(sub_text, (num))

print(indeks)