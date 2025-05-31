# Fayl nomi va kengaytmasini chiqarish 
# Fayl nomi va uning turini format() yordamida ko‘rsating.

name = input("Fayl nomi?: ")
extension = input("Kengaytmasi?: ")

result = "Fayl: {name}.{extension}".format(name=name, extension=extension)

print(result)