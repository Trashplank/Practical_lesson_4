#Начальная переменная
input_person = 1
array_num = []

#Цикл
while input_person > 0:
    input_person = int(input())
    if input_person > 0:
        array_num.append(input_person)

#Вывод данных
print(sum(array_num))