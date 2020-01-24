import time
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import requests



def get_html(url):
    # begin = time.time()
    r = requests.get(url)
    # print(time.time() - begin)
    # print(r.content)

urls = [
    'http://google.com',
    'http://yandex.ru',
    'http://mail.ru'
] * 10


if __name__ == '__main__':
    processPool = ProcessPool(4)
    begin = time.time()
    # processPool.map(get_html, urls)
    print(time.time() - begin)
    threadPool = ThreadPool(4)
    begin = time.time()
    threadPool.map(get_html, urls)
    print(time.time() - begin)