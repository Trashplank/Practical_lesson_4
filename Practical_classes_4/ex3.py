#Вычисление факториала без сторонних библиотек!
num = int(input("Число: "))
array = []
fact = 1

#Цикл 
for i in range(num):
    fact *= (i + 1)

#Вывод
print(fact)

