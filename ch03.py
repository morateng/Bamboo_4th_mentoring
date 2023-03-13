# list1 = [1, 2, '3', 4]
# print(list1)

# list_a = [3, 2, 1, 4]
# list_b = list_a.sort()
# print(list_a, list_b)

# a = [5, 7 ,3]
# b = [3, 9, 1]
# c = a + b
# c.sort()
# print(c)

# list_1 = ['안녕', '하세요']
# print(list_1[0][1])

country = ["korea", "japan", "china"]
capital = ["seoul", "tokyo", "beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)