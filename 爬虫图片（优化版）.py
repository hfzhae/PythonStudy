import urllib.request
import random
import re
import os

def getProxyIP(url):
    html = getHtml(url).decode('gb2312')
    #print(html)
    a = re.findall(r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])', html)
    for i in a:
        print(i)

def getHtml(url):
    #使用代理服务器
    #proxyList = ['220.194.213.52:8080', '61.176.215.34:8080', '61.160.190.34:8888','114.55.244.155:8080','1.28.246.144:8080','218.60.55.3:8080']
    #proxyOpen = urllib.request.ProxyHandler({'http': random.choice(proxyList)})
    #opener = urllib.request.build_opener(proxyOpen)
    #opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')]
    #urllib.request.install_opener(opener)
    #response = urllib.request.urlopen(url)
    #使用代理服务器结束 test
    
    #正常访问
    req = urllib.request.Request(url)
    req.add_header('http', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
    response = urllib.request.urlopen(req)
    #end
    
    html = response.read()
    return html


def getPage(url):
    html = getHtml(url).decode('utf-8')
    a = re.findall(r'current-comment-page\"\>\[(\d+)\]', html)
    return a[0]

def setImg(url):
    html = getHtml(url).decode('utf-8')
    a = re.findall(r'\<img.+src="([^"]+\.jpg)', html)
    
    for i in a:
        if re.search(r'http:', i):
            imgurl = i
        else:
            imgurl = "http:" + i
        print(imgurl)
        #imgurl = re.search(r'\/\/.{0,500}\.jpg', i).group()
        filename = imgurl.split('/')[-1]
        urllib.request.urlretrieve(imgurl, filename)

def getImg(url, page):
    if os.path.exists('images'):#检查目录是否存在
        for root, dirs, files in os.walk('images'):#遍历目录下的文件
            for name in files:
                os.remove('images/' + name)#删除文件
        try:
            os.removedirs('images')#删除目录
        except Exception:
            print('removedirs err')#删除目录失败打印
        
    os.makedirs('images', 511)#创建目录
    os.chdir('images')#进入目录
    
    n = int(getPage(url))#获取当前页面的页编码

    while page > 0:
        openurl = url + '/page-' + str(n) + '#comments'
        setImg(openurl)
        n -= 1
        page -= 1

getProxyIP('http://www.66ip.cn/')
#getImg('http://jandan.net/ooxx', 1)#调用主函数
