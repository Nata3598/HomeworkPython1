#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input('Введите число от 1 до 7: '))
if num == 6 or num == 7:
   print(f'{num} -> Да')
elif num > 7 or num < 1:
     print('Ввели не верное число')
elif num < 6 and num > 0:
     print(f'{num} -> Нет')
