'''
Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    a) клиент отправляет запрос серверу;
    b) сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента:
    - сформировать presence-сообщение;
    - отправить сообщение серверу;
    - получить ответ сервера;
    - разобрать сообщение сервера;
    - параметры командной строки скрипта client.py <addr> [<port>]:
        - addr — ip-адрес сервера;
        - port — tcp-порт на сервере, по умолчанию 7777.
Функции сервера:
    - принимает сообщение клиента;
    - формирует ответ клиенту;
    - отправляет ответ клиенту;
    - имеет параметры командной строки:
        - -p <port> — TCP-порт для работы (по умолчанию использует 7777);
        - -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

'''
import argparse
from socket import *
import time
import pickle

def run_server(addr='', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, port))
    s.listen(5)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    while True:
        client, ip_addr = s.accept()
        data = client.recv(1024)
        response = {
            "response": 200,
            "alert": time.time()
        }
        client.send(pickle.dumps(response))
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', help='IP-адрес для прослушивания', default='')
    parser.add_argument('port', help = 'TCP-порт для работы', type=int, default=7777)
    args = parser.parse_args()
    run_server(args.addr, args.port)

