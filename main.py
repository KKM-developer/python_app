'''
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().

2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое
число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
'''

import csv
import glob
import os
import json
import yaml

def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    os_prod = u'Изготовитель ОС'
    os_name = u'Название ОС'
    os_code = u'Код продукта'
    os_type = u'Тип системы'

    for filename in glob.glob('*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            for line in f:
                if os_prod in line:
                    os_prod_list.append(line.split(': ')[1].strip())
                if os_name in line:
                    os_name_list.append(line.split(': ')[1].strip())
                if os_code in line:
                    os_code_list.append(line.split(': ')[1].strip())
                if os_type in line:
                    os_type_list.append(line.split(': ')[1].strip())
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(len(os_prod_list)):
        info_list = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(info_list)
    return main_data


def write_to_csv():
    with open('kp_data_write.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in get_data():
            f_n_writer.writerow(row)

def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_n, indent=4)

def yaml_write(dict_list, int_numb, uni_dict):
    data_to_yaml = {'first': dict_list, 'second': int_numb, 'third': uni_dict}
    with open('file.yaml', 'w') as f_n:
        yaml.dump(data_to_yaml, f_n, default_flow_style=True, allow_unicode=True)


if __name__ == '__main__':
    write_to_csv()
    write_order_to_json('apple', 5, 15, 'Kirill', '01-06-2021')

    list_for_yaml = ['cat', 'dog', 'cow']
    numb_for_yaml = 15
    uni_for_yaml = {
        'А' : 0x0410,
        'Б' : 0x0411,
        'В' : 0x0412,
        'Г' : 0x0413,
        'Д' : 0x0414,
        'Е' : 0x0415,
    }
    yaml_write(list_for_yaml, numb_for_yaml, uni_for_yaml)

