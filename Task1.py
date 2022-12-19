number = input("Введите число: ")
sum = 0 
for i in number:
    if i.isdigit():
         
        sum = sum + int(i)
print(sum)