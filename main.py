"""
1 Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.

2 Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину
соответствующих переменных.

3 Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

4 Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode).

5 Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в
строковый тип на кириллице.

6 Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и
вывести его содержимое.
"""


def task_1(list_word):
    for word in list_word:
        print(f'{word} is {type(word)}')

def task_2(list_word):
    for word in list_word:
        print(f'{word} is {type(word)} length = {len(word)}')

def task_3(list_word):
    for word in list_word:
        try:
            byte = word.encode('utf-8')
            print(byte)
        except:
            print(f'{word} can`t be bytes')

def task_4(list_word):
    for word in list_word:
        enc_word = word.encode('utf-8')
        dec_word = enc_word.decode('utf-8')
        print(f'{enc_word} is {dec_word}')


if __name__ == '__main__':

    words = ['разработка', 'сокет', 'декоратор']
    task_1(words)

    uni_word = ['%u0440%u0430%u0437%u0440%u0430%u0431%u043E%u0442%u043A%u0430', '%u0441%u043E%u043A%u0435%u0442',
                '%u0434%u0435%u043A%u043E%u0440%u0430%u0442%u043E%u0440']
    task_1(uni_word)

    words_2 = [bytes('class', encoding = 'utf-8'), bytes('function', encoding = 'utf-8'), bytes('method', encoding = 'utf-8')]
    task_2(words_2)

    words_3 = ['attribute', 'класс', 'функция', 'type']
    task_3(words_3)

    words_4 = ['разработка', 'администрирование', 'protocol', 'standard']
    task_4(words_4)

    my_file = open('test_file.txt', 'w+')
    my_file.write(f'сетевое программирование\nсокет\nдекоратор')
    my_file.close()
