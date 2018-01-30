# -*- coding: utf-8 -*-
# 爬取春节图片并且保存本地
import os
from bs4 import BeautifulSoup
import urllib.request
import sys
from pypinyin import pinyin, lazy_pinyin


def getFileName(page, name, suffix='jpg'):
    dir = os.path.dirname(os.path.realpath(__file__)) + os.sep + str(page)
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir + os.sep + name + '.' + suffix


def spider(searchStr):
    # 第一页
    page = 0
    while page < 10:
        page += 1
        url = 'http://588ku.com/sucai/0-default-0-0-{}-{}'.format(searchStr, page)
        print(url)

        try:
            r = urllib.request.urlopen(url)
        except BaseException as e:
            print('请求出错', e)
            continue

        if r.status != 200:
            print('request fail')
            continue

        soup = BeautifulSoup(r.read(), 'html.parser')

        r.close()
        for img in soup.select('.img-show img'):
            urllib.request.urlretrieve(img.attrs['data-original'], getFileName(searchStr+str(page), img.attrs['alt']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        search = sys.argv[1]
        print(search)
    else:
        search = '春节'
    search = lazy_pinyin(search)
    search = ''.join(search)
    spider(search)
