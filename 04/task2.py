# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import random

# Программа создаёт два многочлена, записывает их в два файла, а потом считывает и складывает их.
# Программа выведет string многочлена, который является суммой двух других.

def validate(k: int): #проверка на число введённых степеней. минимум 1, потому что k(0)*x + n = 0, не должно получится
    if k >= 1:
        return True
    else:
        return print('В уровнении нет переменных!')

def create_list(k):  #функция создаёт список из k+1 элементов со случайными значенями от -100 до 100
    my_list = []
    min_value = -100
    max_value = 101
    for i in range(k+1):
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

def splited(inc_str: str) -> list: # список из строки
    temp_list = inc_str.replace(' ', '').replace('=0','')\
        .replace('+', ' ').replace('-', ' -').split()
    return temp_list

def create_dict(inc_list: list) -> dict:   #функция создаёт словарь из списка, с ключами - степенями, и значенями - множители переменной
    temp_dict = {}
    for item in inc_list:
        key = 0
        if 'x' in item:
            if '**' in item:
                key = int(item.split('**')[1])
                temp_dict[key] = int(item.split('*x')[0])
            else:
                temp_dict[1] = int(item.split('*x')[0])
        else:
            temp_dict[0] = int(item)
    return temp_dict

def total_dict(inc_dict1: dict, inc_dict2: dict) -> dict: # складываем int значения двух словарей
    keys = set()
    temp_dict = {}
    for i in inc_dict1:
        keys.add(i)
    for i in inc_dict2:
        keys.add(i)
    for i in keys:
        temp_dict[i] = inc_dict1.get(i, 0) + inc_dict2.get(i, 0)
    return temp_dict

# функция создаёт список из словаря. На случай, если какой-то степени в многочлене нету, создаётся элемент с 0
def create_list_from_dict(inc_dict: dict) -> list:      
    index = 0
    keys = 0
    temp_list = []
    while True:
        if keys == len(inc_dict):
            break
        elif inc_dict.get(index) != None:
            temp_list.append(inc_dict[index])
            index += 1
            keys += 1
        else:
            temp_list.append(0)
            index += 1
    return temp_list

print()
k = int(input('Задайте максимальную степень первого многочлена: ')) #вводим максимальную степень многочлена
if validate(k):
    my_list = (create_list(k))  #создаем рандомный список из "степень + 1" элементов в диапозоне от -100 до 100
    print(f'Наш случайный список №1\n{my_list}') 
    polynominal = create_polynomial(my_list)    #собираем многочлен из списка
    print(f'Так выглядит многочлен в файле\n{polynominal}\n')
    path1 = 'file1.txt'  #записываем сюда
    data = open(path1, 'w')
    data.write(f'{polynominal}\n')
    data.close()

#делаем тоже самое со вторым многочленом
k = int(input('Задайте максимальную степень второго многочлена: '))
if validate(k):
    my_list = (create_list(k))
    print(f'Наш случайный список №2\n{my_list}') 
    polynominal = create_polynomial(my_list)
    print(f'Так выглядит многочлен в файле\n{polynominal}\n')
    path2 = 'file2.txt'
    data = open(path2, 'w')
    data.write(f'{polynominal}')
    data.close()

# подгружаем многочлены из файлов в строковые переменные и формируем словари

data = open(path1, 'r')
poly_str1 = data.read()
data.close()
poly_str1 = poly_str1.strip()
my_list_poly = (splited(poly_str1))
print('Читаем первый файл и сплитуем')
print(my_list_poly)
my_dict1 = create_dict(my_list_poly)
print('Получается вот такой словарь')
print(my_dict1)

data = open(path2, 'r')
poly_str2 = data.read()
data.close()
poly_str2 = poly_str2.strip()
my_list_poly = (splited(poly_str2))
print('\nЧитаем второй файл и сплитуем')
print(my_list_poly)
my_dict2 = create_dict(my_list_poly)
print('Получается вот такой словарь')
print(my_dict2)

my_dict3 = total_dict(my_dict1, my_dict2)
print('\nСкладываем значение словарей')
print(my_dict3)
new_list = create_list_from_dict(my_dict3)
print('Список со значениями будущего многочлена')
print(new_list)
new_str = create_polynomial(new_list)
print('\nРезультат работы программы, Грац.')
print()

    
