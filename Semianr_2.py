# Задача про заражённые холодильники




# n = int(input("Введите кол-во холодильников"))
# list1 = []
# for i in range(n):
#     a = input("Введите серийный номера")
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)
# print(*list1) 

######################################################################################

# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

# N = int(input("Введите число - "))
# a = 0
# res = 1

# while a < N:
#     res = res*(-3)
#     a += 1
#     print(res)


                            # вариант решения 


# for i in range(5):

#  print((-3 )** i, end=" ")  # "end=" "" помогает вывесчти результат в список


##############################################################################################

#Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

a = " 123 234 543 123 123 123"
b = "123"
list = 0
for i in range(a):
    if b in a: 
        a = a[a.find(b)]
        list.append(i + 1)
print(*list)
