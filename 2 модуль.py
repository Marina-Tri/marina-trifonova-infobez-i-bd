print("Самописный калькулятор")
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = str(input("Введите знак между числами: "))
if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "/":
    if y == 0:
        print("На ноль делить нельзя")
    else:
        print(x / y)
else:
    print("Ошибка вычисления")

print("Гонка спидстеров")
n = int(input("Введите скорость Зума: "))
k = int(input("Введите скорость Флэша: "))
if n > k:
    print("NO")
elif k > n:
    print("YES")
elif n == k:
    print("Don't know")

print("Вид треугольника")
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Равносторонний")
    elif a == b or b == c or a == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Такого треугольника не существует")

print("Среднее число")
a = int(input())
b = int(input())
c = int(input())
if a < b < c or a > b > c:
    print(str(b))
elif b < a < c or b > a > c:
    print(str(a))
elif a < c < b or a > c > b:
    print(str(c))
else:
    print("Ошибка")

print("Количество дней")
a = int(input("Введите порядковый номер месяца: "))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("31")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")
elif a == 2:
    print("28")
else:
    print("Ошибка")

print("Церемония взвешивания")
a = int(input("Введите вес боксера-любителя: "))
if a < 60:
    print("Легкий вес")
elif 59 < a < 64:
    print("Первый полусредний вес")
elif 63 < a < 69:
    print("Полусредний вес")

print("Цветовой микшер")
x = str(input("Введите цвет (красный, синий или желтый): "))
y = str(input("Введите другой цвет (красный, синий или желтый): "))
if (x == "красный" and y == "синий") or (x == "синий" and y == "красный"):
    print("фиолетовый")
elif (x == "красный" and y == "желтый") or (x == "желтый" and y == "красный"):
    print("оранжевый")
elif (x == "синий" and y == "желтый") or (x == "желтый" and y == "синий"):
    print("зеленый")
else:
    print("Ошибка цвета")

print("Цвета колеса рулетки")
a = int(input("Введите номер кармана: "))
if 0 <= a <= 36:
    if a == 0:
        print("зеленый")
    elif 1 <= a <= 10 or 19 <= a <= 28:
        if a % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif 11 <= a <= 18 or 29 <= a <= 36:
        if a % 2 == 0:
            print("красный")
        else:
            print("черный")
else:
    print("Ошибка ввода")

print("Пересечение отрезков")
a1 = int(input("Введите a1: "))
b1 = int(input("Введите b1: "))
a2 = int(input("Введите a2: "))
b2 = int(input("Введите b2: "))
if a1 < b1 and a2 < b2:
    if a2 > b1 or a1 > b2:
        print("пустое множество")
    elif a1 == b2:
        print(str(a1))
    elif a2 == b1:
        print(str(a2))
    else:
        if a1 > a2:
            a2 = a1
        if b1 < b2:
            b2 = b1
        print(str(a2), str(b2))
else:
    print("Ошибка")