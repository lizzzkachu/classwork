# num1 = int(input("начало диапазона: "))
# num2 = int(input("конец диапазона: "))
# if num1>num2: num1, num2 = num2, num1
# while num1<=num2:
#     if num2%4==0:'
#         print(num1)
#         num1+=4
#     else:
#         num1+=1
#
#
#
# n=int(input())
# counter=0
# while counter<=n:
#     print(counter)
#     counter+=1
#
#
# for i in range(0 (от), 10 (до), 1 (шаг, если шаг 2-выводит четные числа)):
#     print(i, end=" ")
#
# равносильно записи
#
# i=0
# while i<10:
# print(i, end=" ")
# i+=1
import random

# все целые числа в обратном порядке
# a=int(input("начало диапазона: "))
# b=int(input("конец диапазона: "))
# if a>b: a, b = b, a
# if a%2: a+=1
# for i in range(b, a-1, 1):
#       print(i, end=(" "))


# все четные числа от a до b
# a=int(input("начало диапазона: "))
# b=int(input("конец диапазона: "))
# if a>b: a, b = b, a
# for i in range(a, b, 2):
#        print(i, end=(" "))

# сумма всех целых числел
# a=int(input("начало диапазона: "))
# b=int(input("конец диапазона: "))
# if a>b: a, b = b, a
# sum=0
# for i in range(a, b+1, 1):
#     sum+=i
# print(sum)


# число, сумма цифр этого числа, разрядность неизвестна
# n=int(input("введите число: "))
# summa=0
# while n:
#        summa+=n%10
#        n=n//10
# print(summa)


# вывести n-кол-во раз слово
# n=int(input("введите кол-во повторов: "))
# for i in range (n):
#     print("hello", end=(" "))


# n чисел, посчитать ср арфм
# n=int(input("введите кол-во чисел: "))
# sum=0
# for i in range (n):
#     sum+=int(input())
# print(sum/n)

# количество четных числел
# n=int(input("введите кол-во чисел: "))
# count=0
# for i in range (n):
#     num=int(input())
#     if num%2==0:
#         count+=1
# print(count)

# таблица умножения числа
# n=int(input("введите число: "))
# for i in range (1, 10, 1):
#     print(f' {n}*{i}={n*i}')

# угадай число
# import random
# a=random.randint(1,99)
# count=0
# flag = True
# while flag:
#     n = int(input("введите число: "))
#     if n > a:
#         print("заданное число меньше")
#     elif n < a:
#         print("заданное число больше")
#     else:
#         print("вы угадали")
#         flag = False
#     count+=1
# print("количество попыток: ", count)

# import random
# a = random.randint(1, 99)
# pr = 0
# while pr < 5:
#     n = int(input("введите число: "))
#     if n > a:
#         print("заданное число меньше")
#     elif n < a:
#         print("заданное число больше")
#     else:
#         print("вы угадали")
#         pr = 10
# if (pr==5):
#     print("вы проиграли")

import random
a=random.randint(1,99)
pr=0
flag = True
while flag:
    while pr < 5:
     n = int(input("введите число: "))
     if n > a:
         print("заданное число меньше")
     elif n < a:
         print("заданное число больше")
     else:
         print("вы угадали")
         pr = 10
if (pr==5):
    print("вы проиграли")
input("хотите сыграть снова?")
if "да":
    flag=True
else:
    flag = False
    print("игра окончена")





