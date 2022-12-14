# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_of_even(nums: list[int]) -> int:
    """Возвращает сумму элементов на нечетных позициях"""
    return sum(nums[1::2])
a = [2, 3, 5, 9, 3]
print(sum_of_even(a))



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def pair_multi(nums: list[int]) -> list[int]:
    """Возвращает список произведений пар элементов"""
    pairs = []
    interations = int(round((len(nums)+1)/2))
    print(interations)
    for i in range(interations):
       pairs.append(nums[i]*nums[-1-i]) 
    return(pairs)
nums = [2, 3, 5, 9, 3]
print(pair_multi(nums))



# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Не смогла разобраться с задачей



#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def ordinary_bin(n: int) -> str:
    """Возвращает двоичную запись числа"""
    return bin(n)[2::]

def binar(namber):
    namber_bin_manual = ''
    temp = namber
    while temp > 0:
        namber_bin_manual = str(temp%2) + namber_bin_manual
        temp = temp // 2
    return namber_bin_manual

print(ordinary_bin(3))



#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n: int):
    """Возвращает член последовательности Фибоначчи"""
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def neg_fib(n: int) -> int:
    """Возвращает член последовательности негофибоначчи"""
    return (-1)**(n+1)*fib(n)

def sequence_of_fibs(n: int) -> list[int]:
    """Возвращает последовательность Фибоначчи"""
    list1 = [neg_fib(i) for i in range(n+1)][::-1]
    list2 = [fib(i) for i in range(1, n+1)]
    return list1 + list2

n = 10
print(sequence_of_fibs(n))