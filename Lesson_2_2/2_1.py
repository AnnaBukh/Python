#напишите программу, которая принимает на вход число N и выдает последоватлеьность из N членов
# in >> 5 
# out >> 1 -3 9 -27 81 

num = int(input())


# result =  1
# for  i in range(num):
#     print(result, end=" ")
#     result *= -3
for k in range(num):
    # print(3**k*(-1)**k)
    print((-3)**k)