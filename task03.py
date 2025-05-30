# Fayl nomi va kengaytmasini chiqarish 
# Fayl nomi va uning turini format() yordamida ko‘rsating.

file_name = input("Fayl nomi?: ")
file_extension = input("Kengaytmasi?: ")

file = "Fayl: {file_name}.{file_extension}".format(file_name=file_name, file_extension=file_extension)

print(file)