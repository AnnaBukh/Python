# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.
# a = int(input("enter a"))
# b = int(input("enter b"))

# c = a**2
# d = b**2 

# if c == b:
#     print("a is square of b")
# elif a == d:
#     print("b is square of a")
# else:
#     print("_______________")

n = int(input())
m = int(input())

if n == m ** 2 or m == n ** 2:
    print("Yes")
else:
    print("No")