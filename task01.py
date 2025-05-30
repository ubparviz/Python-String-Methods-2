# Foydalanuvchi ismi va yoshi asosida xabar chiqarish.
# format() methodidan foydalanib, matnga foydalanuvchi ma’lumotlarini joylashtiring.

name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

message = "Salom mening ismim {name} va yoshim {age} yoshda.".format(name=name, age=age)

print(message)