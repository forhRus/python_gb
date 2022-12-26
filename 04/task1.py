# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def validate(k: int): #проверка на количество переменных, хотя бы 1
    if k >= 1:
        return True
    else:
        return print('В уровнении нет переменных!')

def create_list(n):  #функция создаёт список из n+1 элементов со случайными значениями от -100 до 100
    my_list = []
    min_value = -100
    max_value = 101
    for i in range(n+1):
        my_list.append(random.randint(min_value, max_value))
    return my_list

def create_polynomial(inc_list: list): #из списка делаем строку с многочленом
    str_polynomial = ''
    for k in range(len(inc_list)-1, -1, -1):
        if k == 0:
            if len(inc_list) - 1 == 1 and inc_list[1] == 0:
                print('В уровнении нет переменных!')
                continue
            elif inc_list[k] != 0:
                if inc_list[k] == 1:
                    str_polynomial += f'{str(inc_list[k])}'
                elif inc_list[k] > 0:
                    str_polynomial += f' + {str(inc_list[k])}'
                else:
                    str_polynomial += f' - {str(inc_list[k])[1:]}'
            else:
                continue
        elif k == 1:
            if len(inc_list) > 2:
                if inc_list[k] != 0:
                    if inc_list[k] == 1:
                        str_polynomial += f' + x'
                    elif inc_list[k] > 0:
                        str_polynomial += f' + {str(inc_list[k])}*x'
                    else:
                        str_polynomial += f' - {str(inc_list[k])[1:]}*x'
                else:
                    continue
            else:
                if inc_list[k] != 0:
                    if inc_list[k] == 1:
                        str_polynomial += f'x'
                    elif inc_list[k] > 0:
                        str_polynomial += f'{str(inc_list[k])}*x'
                    else:
                        str_polynomial += f'-{str(inc_list[k])[1:]}*x'
                else:
                    continue
        elif k == len(inc_list) - 1:
            if inc_list[k] != 0:        #проверка нужна для того, чтобы печатать отрицательные значения первого члена
                if inc_list[k] == 1:
                    str_polynomial += f'x**{k}'
                else:
                    str_polynomial += f'{str(inc_list[k])}*x**{k}'  
            else:
                continue
        elif k > 1:              #отрицательные значения прибавляем в строку без минуса, но в само стринговое выражение символ добавляем
            if inc_list[k] != 0:
                if inc_list[k] == 1:
                    str_polynomial += f' + x**{k}'
                elif inc_list[k] > 0:
                    str_polynomial += f' + {str(inc_list[k])}*x**{k}'
                else:
                    str_polynomial += f' - {str(inc_list[k])[1:]}*x**{k}'
            else:
                continue
    str_polynomial = str_polynomial + ' = 0'
    return str_polynomial


k = int(input('Задайте максимальную степень многочлена: ')) #вводим максимальную степень многочлена
if validate(k):
    my_list = (create_list(k))  #создаем рандомный список из "степень + 1" элементов в диапозоне от -100 до 100
    print(my_list) 
    polynominal = create_polynomial(my_list)    #собираем многочлен из списка
    print(polynominal)
    path1 = 'file1.txt'  #записываем сюда
    data = open(path1, 'w')
    data.write(f'{polynominal}\n')
    data.close()

    





