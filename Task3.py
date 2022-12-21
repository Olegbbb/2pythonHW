from random import randint
amount = int(input("Введите количество элементов списка: "))
my_list = []
for i in range(amount):
    a = input("Введите элемент списка: ")
    my_list.append(a)
print(f"Первоначальный массив: {my_list}")
for i in range(len(my_list)):
    j = randint(0, amount - 1)
    a = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = a
print(f"Конечный массив: {my_list}")



