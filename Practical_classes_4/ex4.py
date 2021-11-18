#ВВод
start_num = int(input("Стартовое колличество: "))
srznach = str(input("Среднесуточное увеличение: "))
days = int(input("Колличество дней для размножения: "))

#Преобразование 
srznach = (int(srznach[0] + srznach[1]) / 100) + 1




for i in range(days):
    print(str(i + 1) + " " + str(start_num))
    start_num *= srznach
    