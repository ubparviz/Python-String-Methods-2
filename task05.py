# Ikki raqamdan iborat amaliy natijani formatlash 
# Matematik amalni ifodalashda formatdan foydalaning.

print("Ikkita butun sonni bir-biriga qo'shib beraman")

num1 = int(input("Birinchi raqamni yozing? "))
num2 = int(input("Ikkinchi raqamni yozing? "))
total = num1 + num2

answer = "{num1} + {num2} = {total}".format(num1=num1, num2=num2, total=total)

print(answer)