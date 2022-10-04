#напишите программу, в которой пользователь будет задавать две строки, программа-определять кол-во вхождений
#одной строки в другую
line_1 = input()
line_2 = input()
print(line_1.count(line_2))
#line_1.count(line_2, 3) - поиск с 3его индекса начиная, не с начала
#line_1.count(line_2, 3, 5) - поиск с 3его индекса до 5ый 
#line_1.replace(line_2, line_3) - замена в line_1 элемента line_2 на line_3
#line_1.replace(line_2, " ") - замена в line_1 элемента line_2 на пробел
#line_1.replace(line_2, "") - удаление в line_1 элемента line_2 
# методы count , replace не меняют исходного слова, только выдают новое
# можно применить совместно line_1.replace(line_2, line_3).count(line_3)