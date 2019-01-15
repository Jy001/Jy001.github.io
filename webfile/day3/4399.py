import requests
import re
from pyquery import PyQuery

#访问网站,获取网站数据,解码
html = requests.get('http://news.4399.com/gonglue/lscs/kptj/').content.decode("gb2312")

#调用pyquery
doc = PyQuery(html)

#获取li
items = doc('#dq_list>li').items()

for i in items:
    #print(i)
    #获取图片的url
    img_url = i.find('img').attr('lz_src')

    #获取图片的名称
    name = i.find('.kp-name').text()
    #print("url：" + img_url)
    #print("图片name：" + name)

    #下载图片
    url_content = requests.get(img_url).content #下载

    #写入文件
    file = open( 'E:\pycharm\项目\\4399_炉石_爬虫\\4399图片' + '\\' + name + '.jpg','wb')
    file.write(url_content)
    file.close()

print("下载完成")
























