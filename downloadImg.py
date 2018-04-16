
# -*- coding:utf-8 -*-

import re
import requests


def download_img():
    url = 'https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs14&word=%E5%BE%AE%E4%BF%A1%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&oriquery=%E8%A1%A8%E6%83%85%E5%8C%85&ofr=%E8%A1%A8%E6%83%85%E5%8C%85&sensitive=0'
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 0
    for each in pic_url:
        print each
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print '【错误】当前图片无法下载'
            continue
        string = 'pictures' + str(i) + '.jpg'
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

if __name__ == '__main__':
    download_img()