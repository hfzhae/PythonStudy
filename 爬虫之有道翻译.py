import urllib.request
import urllib.parse
import json


url = 'http://fanyi.baidu.com/v2transapi'

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'

data = {}
data['from'] = 'en'
data['to'] = 'zh' 
data['query'] = input('请输入英文：')
data['transtype'] = 'realtime'
data['simple_means_flag'] = '3'

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')

fyrps = json.loads(html)

print('翻译的结果是：%s' % (fyrps['trans_result']['data'][0]['dst']))




