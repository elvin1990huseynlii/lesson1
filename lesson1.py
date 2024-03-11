# # 1. Listin bütün elementləri cəmini(hasilini) hesablayın

# numbers = (3,4,6,7,2,55,23,4,6)
# total = 0 

# for number in numbers:
#     total += number

#     print(total)



# # 2. Verilən list elementlərini sağdan sola çap edin

# numbers = (4, 7, 5, 22, 87, 43)
# x = numbers[::-1]

# print(x)


# # 3. İki fərqli list yaradın və listləri merge edin(zip metodu)

# list1 = ("Ar", "Gi", "Ba")
# list2 = ("mud", "las", "nan",)


# list3 = [a+b for a, b in zip(list1, list2)]

# print(list3)




# 4. Listin içində bir neçə list olsun, 3ci elementinin 2ci indeksinə dəyər əlavə edin

# Meyveler = [["alma", "armud", "nar"], ["qirmizi", "sari", "cehrayi"], ["kal", "deyib", "curuyub"]]

# Meyveler[2].insert(2, ("xarabdi") )

# print(Meyveler)



# 5. List yaradın , listin hər hansı dəyərinin indeksini tapın və həmin indeksə başqa dəyər əlavə edin

# cars = [["Bmw", "Mercedes", "Tesla"], ["Black", "Yellow", "Red"], ["Diesel", "Oil", "Electric"]]
# cars[2].insert(3,'Free for 1 Year')
# print(cars)

# 6. Verilmiş listin ədədi ortasını tapın

# numbers = (4,4,5,6,2,3,5,7,9)

# average = sum(numbers)/len(numbers)

# print("Average of list: ", round(average,2))


# 8. Təkrar elemetlərdən ibarət list yaradın, sonra bu listdən təkrarlanmayan list yaradın

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]


# res = []
# [res.append(x) for x in test_list if x not in res]

# print (" "
# 	+ str(res))

