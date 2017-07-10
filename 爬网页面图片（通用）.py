import urllib.request
import random
import re
import os

def getHtml(url):
    #使用代理服务器
    #proxyList = ['220.194.213.52:8080', '61.176.215.34:8080', '61.160.190.34:8888','114.55.244.155:8080','1.28.246.144:8080','218.60.55.3:8080']
    #proxyOpen = urllib.request.ProxyHandler({'http': random.choice(proxyList)})
    #opener = urllib.request.build_opener(proxyOpen)
    #opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')]
    #urllib.request.install_opener(opener)
    #response = urllib.request.urlopen(url)
    #使用代理服务器结束
    
    #正常访问
    req = urllib.request.Request(url)
    req.add_header('http', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
    response = urllib.request.urlopen(req)
    #end
    
    html = response.read()
    return html

def setImg(url, code, t):
    html = getHtml(url).decode(code)
    a = re.findall(r'\<img.{0,200}\.'+ t, html)

    for i in a:
        imgurl = re.search(r'\/\/.{0,200}\.'+ t, i).group()
        filename = imgurl.split('/')[-1]
        urllib.request.urlretrieve("http:%s" % imgurl, filename)
        print(imgurl)

def getImg(url, folder, code, t):
    if os.path.exists(folder):#检查目录是否存在
        for root, dirs, files in os.walk(folder):#遍历目录下的文件
            for name in files:
                os.remove(folder + '/' + name)#删除文件
        try:
            os.removedirs(folder)#删除目录
        except Exception:
            print('removedirs err')#删除目录失败打印
    os.makedirs(folder, 511)#创建目录
    os.chdir(folder)#进入目录
    setImg(url, code, t)

#getImg('https://www.suning.com/', 'suning', 'utf-8', 'jpg')
#getImg('http://bj.58.com/', '58', 'utf-8', 'png')
#getImg('https://www.jd.com/', 'jd', 'utf-8', 'gif')
#getImg('https://www.taobao.com/', 'taobao', 'utf-8', 'jpg')
getImg('http://www.icloud365.cn/', 'icloud365', 'gb2312', 'jpg')

