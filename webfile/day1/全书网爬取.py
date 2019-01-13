import re
import requests


#定义一个函数：获取分类里的小说
def get_novel_list():
    response = requests.get('http://www.quanshuwang.com/list/4_1.html')
    response.encodeing = 'gbk'
    html = response.text
    #正则匹配
    reg = r'<a target="_blank" href="(.*?)" class="l mr10">'
    return re.findall(reg,html)

#获取小说的首页
def get_home_list(url):
    response = requests.get(url)
    response.encoding = 'GBK'
    html = response.text
    #正则
    reg = r'<a href="(.*?)" class="reader" title="(.*?)">开始阅读</a>'
    #print(re.findall(reg,html))
    return re.findall(reg,html)

#获取小说的目录
def get_catalogue_list(url):
    response = requests.get(url)
    response.encoding = 'GBK'
    html = response.text
    # 正则
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    #print(re.findall(reg,html))
    return re.findall(reg,html)

#获取小说的内容
def get_content(content):
    response = requests.get(content)
    response.encoding = 'GBK'
    html = response.text
    # 正则
    reg = r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6\(\);</script>'
    return re.findall(reg,html,re.S)


for i in get_novel_list():
    for j in get_home_list(i):
       for get_url,get_user in get_catalogue_list(j[0]):
           #print(k[0])
           for l in get_content(get_url):
                print(l)
                f = open(get_user + '.html','w')
                f.write(l)
                f.close()

    break

