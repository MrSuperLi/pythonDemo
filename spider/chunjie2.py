# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import urllib.request


def getFileName(page, name, suffix='jpg'):
    dir = os.path.dirname(__file__) + os.sep + str(page)
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir + os.sep + name + '.' + suffix


def spider():
    # 第一页
    page = 0
    while page < 1:
        page += 1
        url = 'http://588ku.com/sucai/0-default-0-0-chunjie-{}'.format(page)
        print(url)
        r = urllib.request.urlopen(url)

        if r.status != 200:
            print('request fail')
            continue

        soup = BeautifulSoup(r.read(), 'html.parser')

        r.close()
        for img in soup.select('.img-show img'):
            urllib.request.urlretrieve(img.attrs['data-original'], getFileName(page, img.attrs['alt']))


if __name__ == '__main__':
    spider()
