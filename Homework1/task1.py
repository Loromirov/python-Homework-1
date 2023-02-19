# # Задача 2: Найдите сумму цифр трехзначного числа.

# # *Пример:*

# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите трехзначное число: "))
sum = 0 
remNum = num
while num > 0:
     remNum = num % 10
     sum += remNum
     num = num // 10
print(sum, remNum, num)
