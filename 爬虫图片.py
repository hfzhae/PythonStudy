import urllib.request
import re
import random #随机数对象
import chardet

n = 131
ipList = ['144.76.32.78:8080', '113.245.184.227:8081', '218.60.55.78:8080', '58.221.38.70:8080', '61.176.215.34:8080']

while (n > 130):
    url = 'http://jandan.net/ooxx/page-%s' % n

    proxy_support = urllib.request.ProxyHandler({'http':random.choice(ipList)}) #定义使用代理的协议和地址
    opener = urllib.request.build_opener(proxy_support)

    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')]

    urllib.request.install_opener(opener) #安装代理访问opener

    #req = urllib.request.Request(url)
    #req.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')]

    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    regx = r'src="(.*?.jpg)"'
    pat = re.compile(regx)
    
    #encode_type = chardet.detect(html)#转码
    #html = html.decode(encode_type['encoding'])#转码回填

    imgpath = re.findall(pat, html)
    if len(imgpath) > 0:
        imgpath.pop(len(imgpath)-1)
    
    for url in imgpath:
        filename = url.split('/')
        #print(filename[len(filename)-1])
        urllib.request.urlretrieve('http:%s' % url, 'images\%s' % filename[len(filename)-1])
        print('http:%s' % url)

    n -= 1
