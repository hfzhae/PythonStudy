import urllib.request
import re
import chardet

def get_content(url):
    try:
        html = urllib.request.urlopen(url)
        content = html.read()
        html.close()
        return content
    except Exception as e:  
        print(e)

def get_images(info):
    regx = r'src="(.*?.jpg)"'
    try:
        encode_type = chardet.detect(info)#转码
        info = info.decode(encode_type['encoding'])#转码回填
        pat = re.compile(regx)
        images_code = re.findall(pat, info)
        i = 0
        for image_url in images_code:
            print(image_url)
            filename = image_url.split('/')
            urllib.request.urlretrieve(image_url, '%s_%s.jpg' % (i, filename[len(filename)-1]))
            i += 1
    except Exception as e:  
        print(e)

info = get_content('http://www.ivsky.com/')
#info = get_content('http://tu.duowan.com/')
#info = get_content('http://www.cnbeta.com/')
get_images(info)
