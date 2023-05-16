my_tuple = (1, 2, 3, 4, 4, 5, 4)
search_num = int(input("Введите число для поиска: "))
count = my_tuple.count(search_num)
print(f"Число {search_num} встречается в кортеже {count} раз(а)")