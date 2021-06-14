'''
Для всех функций из урока 3 написать тесты с использованием unittest. Они должны быть оформлены в отдельных
скриптах с префиксом test_ в имени файла (например, test_uni.py).
'''
import unittest
import client
import server

class TestClient(unittest.TestCase):
    def setUp(self):
        self.c = client.connect_server('127.0.0.1', 7777)
        self.s = server.run_server('127.0.0.1', 7777)

    def tearDown(self):
        self.c.close()
        self.s.close()





if __name__ == '__main__':
    unittest.main()
