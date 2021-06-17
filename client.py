import argparse
from socket import *
import time
import pickle
import logging
import log.client_log_config

log.client_log_config.init_log()
logger = logging.getLogger('client_log_config')

def connect_server(addr='', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))
    msg = {
        "action": "authenticate",
        "time": time.time(),
        "user": {
            "account_name": "C0deMaver1ck",
            "password": "CorrectHorseBatterStaple"
        }
    }
    s.send(pickle.dumps(msg))
    data = s.recv(1024)
    print('Message from server ', pickle.loads(data), ', length ', len(data))
    s.close()

if __name__ == '__main__':
    logger.info('App started')
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', help='ip-адрес сервера', default='')
    parser.add_argument('port', help = 'tcp-порт на сервере', type=int, default=7777)
    args = parser.parse_args()
    connect_server(args.addr, args.port)
    logger.info('App ending')