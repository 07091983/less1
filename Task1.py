# # Задача 2: Найдите сумму цифр трехзначного числа.
# # *Пример:*

# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0) |

a = input("Введите трехзначное число: ")
a = int(a)
 
b = a % 10
a = a // 10
c = a % 10
a = a // 10
 
print("Суммa равна:", a + c + b)

# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# # Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# # если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# # *Пример:*

# # 6 -> 1  4  1
# # 24 -> 4  16  4
# #     60 -> 10  40  10

s = input ('Введите количество готовых журавликов:')
s = int (s)

b = int((s/3)*2)
a = int((b/2)/2)
c= int(a)

print (a, b, c)

# # Задача 6: Вы пользуетесь общественным транспортом? 
# # Вероятно, вы расплачивались за проезд и получали билет с номером. 
# # Счастливым билетом называют такой билет с шестизначным номером, 
# # где сумма первых трех цифр равна сумме последних трех. 
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# # Вам требуется написать программу, которая проверяет счастливость билета.

# # *Пример:*

# # 385916 -> yes
# # 123456 -> no

n = input ('Введите номер счастливого билета:')
a = int (n[0]) + int (n[1]) + int (n[2])
b = int (n[3]) + int (n[4]) + int (n[5])

if a == b:
    print ('Ваш билет счастливый))):')
else:
    print ('Ваш билет не счастливый(((:')

# Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int (input('Вводим размер шоколадки - n:'))
m = int (input('Вводим размер шоколадки - m:'))
k = int (input('Вводим количество долек:'))

if k < m * n and (k % m == 0 or k % n == 0):
    print ('Да)))')
else: print ('Нет(((')