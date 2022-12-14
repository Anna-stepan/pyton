# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
namber = input('Nam:')
sum = 0
for i in namber:
    if i != '.':
        sum += int(i)
print(f'Sum of nams: {sum}')


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
import math
n = int(input('Nam:'))
multiplications = [math.factorial(i) for i in range(1, n+1)]
print(f'List of multiplications: {multiplications}')


#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
n = int(input('Nam:'))
multiplications = [(1+1/i)**i for i in range(1, n+1)]
print(f'List of multiplications: {multiplications}')
print(f'Sum of list: {sum(multiplications)}')


#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции 
# в консоли)
with open('file.txt', 'r') as f:
    positions = f.read().split('\n')
positions = list(map(int, positions))
n = int(input())
list_gen = [i for i in range(-n, n+1)]
multi = 1
for pos in positions:
    multi *= list_gen[pos]
print(positions)
print(list_gen)
print(multi)
