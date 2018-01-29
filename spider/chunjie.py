# -*- coding: utf-8 -*-

import urllib3
import io
import os
from bs4 import BeautifulSoup
import urllib.request


def save(http, page, name, url, suffix='jpg'):
    filename = getFileName(page, name, suffix)
    r = http.urlopen('GET', url, True, preload_content=False)
    b = io.BufferedReader(r, 1024)
    with open(filename, 'wb') as fd:
        while not b.closed:
            fd.write(b.read())
    r.close()


def getFileName(page, name, suffix='jpg'):
    dir = os.path.dirname(__file__) + os.sep + str(page)
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir + os.sep + name + '.' + suffix


def spider():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    http = urllib3.PoolManager()

    # 不显示报错
    urllib3.disable_warnings()

    # 第一页
    page = 0
    while page < 1:
        page += 1
        url = 'http://588ku.com/sucai/0-default-0-0-chunjie-{}'.format(page)
        r = http.request('GET', url, headers=header)
        print(url)
        if r.status != 200:
            print('request fail')
            continue

        soup = BeautifulSoup(r.data, 'html.parser')

        r.close()
        for img in soup.select('.img-show img'):
            # save(http, page, img.attrs['alt'], img.attrs['data-original'])
            urllib.request.urlretrieve(img.attrs['data-original'], getFileName(page, img.attrs['alt']))


if __name__ == '__main__':
    spider()
