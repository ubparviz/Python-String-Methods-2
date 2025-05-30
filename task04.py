# Hafta kuni va dars soatini yozish 
# Kun va soatni formatda chiqarish.

day = input("Qaysi kun?: ")
time = input("Qaysi vaqt?: ")

message = "Bugun {day} kuni, dars soat {time} da.".format(day=day, time=time)

print(message)