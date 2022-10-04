#создать список длины n, значения формируются по формуле 3к+1, где к принимает значения от 1 до n вкл

n = int(input())
my_list = []
for k in range(1, n + 1):
    my_list.append(3*k + 1) 
print(my_list)
