# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

n = int(input('Введите номер дня недели от 1 до 7 '))

if (n == 6 or n == 7):
    print("этот день выходной")  
else:
   print("этот день не выходной")

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
#
x = int(input('Введите число х '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

if (not ((x)) or (y) or (z)) == (not ((x)) and (not (y)) and (not (z))):
    print('true')
elif (not ((x)) and (not (y)) and (not (z))):
    print('true')
else:
    print('false')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится)

x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))

if x > 0 and y > 0:
    print('Номер четверти: 1 ')
elif x < 0 and y > 0:
    print('Номер четверти: 2 ')
elif x < 0 and y < 0:
    print('Номер четверти: 3 ')
elif x > 0 and y < 0:
    print('Номер четверти: 4 ')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой 
# четверти (x и y)

a = int(input('Введите номер четверти: '))

if   a == 1: 
    print(' Координаты точки в первой четверти: x от 0 до + ∞, y от 0 до + ∞') 
elif a == 2: 
    print(' Координаты точки во второй четверти: x от 0 до - ∞, y от 0  до + ∞ ')  
elif a == 3: 
    print(' Координаты точки в третьей четверти: x от 0 до - ∞, y от 0  до - ∞ ')
elif a == 4: 
    print(' Координаты точки в четвертой четверт: x от 0 до + ∞, y от 0  до - ∞ ')
else:
    print('Ошибка')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

ax = float(input('Введите координаты точки А по оси x: '))
ay = float(input('Введите координаты точки А по оси y: '))
bx = float(input('Введите координаты точки В по оси x: '))
by = float(input('Введите координаты точки В по оси y: '))

distans = ((ax-bx)**2+(ay-by)**2)**(1/2)
print(distans)
