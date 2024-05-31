# 1
print('Задание №1')

def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params()
# print_params(4, 2, 6, 7) ошибка, значений параметров больше чем задано в функции
print_params(2, 3, 4)
print_params(b = 25)
print_params(c=[1, 2, 3])

print(' ')
# 2
print('Задание №2 ')
values_list = [2, 'Element', False]
values_dict = {'a': 4, 'b': 5, 'c': 6}
print_params(*values_list)
print_params(**values_dict)

print(' ')
# 3
print('Задание №3')
values_list_2 = [14.46, 'Stroka']
print_params(*values_list_2, 42)