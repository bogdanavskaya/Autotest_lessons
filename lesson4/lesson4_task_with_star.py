# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    str_num = str(num)
    length = len(str_num)

    lst_new_num_without_3 = []
    for j in range(10 ** (length - 1), 10 ** length):
        if j % 3 == 0:
            lst_new_num_without_3.append(str(j))

    lst_new_num_with_1_diff = []
    for k in range(len(lst_new_num_without_3)):
        count = 0
        for h in range(0, length):
            if str_num[h] == lst_new_num_without_3[k][h]:
                count += 1
        if count == (length - 1):
            lst_new_num_with_1_diff.append(lst_new_num_without_3[k])

    lst_new_num_with_1_diff_int = []
    for i in range(len(lst_new_num_with_1_diff)):
        lst_new_num_with_1_diff_int.append(int(lst_new_num_with_1_diff[i]))
    new_num = max(lst_new_num_with_1_diff_int)
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')