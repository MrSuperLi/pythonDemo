# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request


def spider():
    page = 0
    f = open('douban.txt', 'bw')
    while page < 10:
        url = 'https://movie.douban.com/top250?start='+str(page*25)
        page += 1
        print(url)
        response = urllib.request.urlopen(url)

        if response.status != 200:
            print('request fail')
            continue
        soup = BeautifulSoup(response.read(), 'html.parser')
        pageInfo = ''
        for movie in soup.select('.grid_view .info'):
            try:
                info = {}
                info['url'] = movie.select('a')[0].attrs['href']
                if 0 in movie.select('.bd .quote span'):
                    info['quote'] = movie.select('.bd .quote span')[0].get_text()
                else:
                    info['quote'] = ''
                info['star'] = movie.select('.bd .star .rating_num')[0].get_text()
                info['desc'] = movie.select('.bd p')[0].get_text(',', strip=True)
                info['title'] = movie.select('.hd a')[0].get_text(',', strip=True)
                pageInfo += ("名称：{title}  评分:{star}  引言：{quote}  链接：{url}  详情：{desc}\n\n".format(**info))
            except:
                print(info)
                continue
        f.write(pageInfo.encode('utf-8', 'ignore'))
    f.close()


if __name__ == '__main__':
    spider()
