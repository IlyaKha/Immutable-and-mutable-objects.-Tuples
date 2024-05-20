# 2 Задание
immutable_var = (5, "строка", True, 2.15)
print(immutable_var)
# 3 Задание
# immutable_var[0] = 20 Ошибка! Кортежи неизменяемы
# Обьяснение Кортежи (tuples) в Python неизменяемы,  это означает, что после создания кортежа мы не можем изменять элементы.
# Задание 4
mutable_list = [10, "десять", 2.15, False]
print(mutable_list)
mutable_list[1] = "девять"
mutable_list.append("новый элемент")
print("Измененный список :", mutable_list)
