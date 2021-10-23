try:
    a = int(input('Введите два числа больше нуля '))
    b = int(input())
except:
    print('Не корректный ввод данных')
    exit()
if a<0 or b<0:
    print('Не корректный ввод данных')
    exit()
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
if a != 0:
    print(a)
else:
    print(b)