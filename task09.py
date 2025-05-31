# Belgilarni qayerdan boshlab qidirishni aniqlang find() metodiga start pozitsiyasi bilan ishlang.

text = input("Matn kiriting: ")
word = input("Matn ichidan bir so'z yozing: ")
num = int(input("Raqam kiriting: "))

index = text.find(word, num)

print(index)