# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв"

all_txt = input("Введите исходный текст:\n")
print(f"Исходный текст: {all_txt}")
find_txt = "абв"
lst = [i for i in all_txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')