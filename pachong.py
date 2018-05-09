from urllib.request import*
import re
##爬取图片的地址
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1525766087121_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%9E%97%E5%BF%97%E7%8E%B2'
html = urlopen(url)
obj = html.read().decode()
urls = re.findall(r'"objURL":"(.*?)"',obj)
index = 0
for url in urls:
    try:
        print('downloading...%d'%index)
        urlretrieve(url,'pic'+str(index)+'.jpg')
        index += 1
    except Exception:
        print('download error...%d'%index)
    else:
        print('download complete...')
