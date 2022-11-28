a = 0
b = 1
vvod = int(input("введите номер последнего элемента числа фибоначчи: "))
for i in range(vvod):
    sum= a + b
    a = b
    b = sum
print("Ответ =",a)