a = int(input("Введите число: "))
my_list = []
sum = 0
for i in range(1, a + 1):
    my_list.append(round((1 + 1/i)**i, 2))
print(my_list)
for i in range(len(my_list)):
    sum+= my_list[i] 
print(f"Сумма элементов равна: {sum}")

