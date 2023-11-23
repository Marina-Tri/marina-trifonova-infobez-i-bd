import math

print("Площадь треугольника")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
s = a * b * 0.5
print(str(s))

print("Две старушки")
v1 = float(input("Введите V1: "))
v2 = float(input("Введите V2: "))
s = float(input("Введите S: "))
t = s / (v1 + v2)
print(round(t, 1))

print("Обратное число")
a = float(input())
if a == 0:
    print("Обратного числа не существует")
else:
    a2 = 1 / a
    print(str(a2))

print("451 градус по Фаренгейту")
f = float(input("Введите число градусов по шкале Фарегейта: "))
c = (5 / 9) * (f - 32)
print(str(c))

print("Dog age")
n = int(input("Введите кол-во собачьих лет: "))
if 0 < n < 3:
    v = n * 10.5
    print(str(v))
elif n > 2:
    v = (n - 2) * 4 + 21
    print(str(v))

print("Первая цифра после точки")
a = float(input())
if a > 0:
    x = (a % 1) // 0.1
    print(str(x))

print("Дробная часть")
a = float(input())
if a > 0:
    x = a % 1
    print(round(x, 10))

print("Наибольшее и наименьшее")
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
a3 = int(input("Введите a3: "))
a4 = int(input("Введите a4: "))
a5 = int(input("Введите a5: "))
x = max(a1, a2, a3, a4, a5)
y = min(a1, a2, a3, a4, a5)
print("Наименьшее число = " + str(y), "Наибольшее число = " + str(x), sep="\n")

print("Сортировка трёх")
a1 = int(input("Введите a1: "))
a2 = int(input("Введите a2: "))
a3 = int(input("Введите a3: "))
x = max(a1, a2, a3)
y = min(a1, a2, a3)
z = a1 + a2 + a3 - x -y
print(str(x), str(z), str(y), sep="\n")

print("Интересное число")
a = int(input("Введите трехзначное число: "))
a1 = a // 100
a2 = (a % 100) // 10
a3 = a % 10
x = max(a1, a2, a3)
y = min(a1, a2, a3)
z = a1 + a2 + a3 - x -y
if x - y == z:
    print("Число интересное")
else:
    print("Число неинтересное")

print("Абсолютная сумма")
a1 = float(input("Введите a1: "))
a2 = float(input("Введите a2: "))
a3 = float(input("Введите a3: "))
a4 = float(input("Введите a4: "))
a5 = float(input("Введите a5: "))
s = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(str(s))

print("Манхэттенское расстояние")
p1 = int(input("Введите p1: "))
p2 = int(input("Введите p2: "))
q1 = int(input("Введите q1: "))
q2 = int(input("Введите q2: "))
r = abs(p1 - q1) + abs(p2 - q2)
print(str(r))

print("Конкатенация строк")
one = '"Python is a great language!"'
two = 'said Fred'
three = "I don't ever remember having this much fun before."
print(one + ', ' + two + '. ' + '"' + three + '"')

print("What's Your Name?")
firstname = str(input("Введите имя: "))
lastname = str(input("Введите фамилию: "))
print("Hello " + firstname + " " + lastname + "! " + "You have just delved into Python")

print("Футбольная команда")
a = str(input("Введите название футбольной команды: "))
x = len(a)
print("Футбольная команда " + a + " имеет длину " + str(x) + " символов")

print("Три города")
a1 = str(input("Введите название первого города: "))
a2 = str(input("Введите название второго города: "))
a3 = str(input("Введите название третьего города: "))
if len(a1) != len(a2) and len(a2) != len(a3) and len(a1) != len(a3):
    if min(len(a1), len(a2), len(a3)) == len(a1):
        print(a1)
    elif min(len(a1), len(a2), len(a3)) == len(a2):
        print(a2)
    else:
        print(a3)
    if max(len(a1), len(a2), len(a3)) == len(a1):
        print(a1)
    elif max(len(a1), len(a2), len(a3)) == len(a2):
        print(a2)
    else:
        print(a3)

print("Арифметические строки")
a1 = len(input("Введите первую строку: "))
a2 = len(input("Введите вторую строку: "))
a3 = len(input("Введите третью строку: "))
if a1 + a2 + a3 == (min(a1, a2, a3) + max(a1, a2, a3)) / 2 * 3:
    print("YES")
else:
    print("NO")

print("Цвет настроения синий")
a = str(input("Введите строку: "))
if "синий" in a:
    print("YES")
else:
    print("NO")

print("Отдыхаем ли")
a = str(input("Введите строку: "))
if "суббота" in a or "воскресенье" in a:
    print("YES")
else:
    print("NO")

print("Корректный email")
a = str(input("Введите email: "))
if "@" and "." in a:
    print("YES")
else:
    print("NO")

print("Евклидово расстояние")
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x1: "))
y2 = float(input("Введите y2: "))
r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(str(r))

print("Площадь и длина")
r = float(input("Введите радиус окружности: "))
S = math.pi * r ** 2
L = 2 * math.pi * r
print(str(S), str(L), sep="\n")

print("Средние значения")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
ar = (a + b) / 2
ge = (a * b) ** 0.5
ga = 2 * a * b / (a + b)
kv = ((a ** 2 + b ** 2) / 2) ** 0.5
print(str(ar), str(ge), str(ga), str(kv), sep="\n")

print("Тригонометрическое выражение")
x = float(input("Введите радусную меру угла: "))
r = x * math.pi / 180
y = math.sin(r) + math.cos(r) + math.tan(r) ** 2
print(str(y))

print("Пол и потолок")
x = float(input("Введите вещественное число: "))
print(math.ceil(x) + math.floor(x))

print("Квадратное уравнение")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Нет корней")
elif d == 0:
    x = -b / (2 * a)
    print(str(x))
elif d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(str(x1), str(x2), sep="\n")

print("Правильный многоугольник")
n = int(input("Введите число сторон: "))
a = float(input("Введите длину стороны: "))
s = (n * a ** 2) / (4 * math.tan(math.pi / n))
print(str(s))