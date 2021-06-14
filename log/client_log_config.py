import logging

def init_log():
    logging.basicConfig(
        filename="client_log_config",
        format="%(asctime)-10s %(levelname)s %(module)s %(message)s",
        level=logging.INFO
    )

if __name__ == '__main__':
    init_log()