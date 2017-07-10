#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
from lxml import etree

def get_urls(url, time):
    source_code = requests.get(url, timeout = time).text
    selector = etree.HTML(source_code)
    urls = selector.xpath('/html/body/div[6]/div[1]/div[1]/ul/li/div[2]/a/@href')
    return urls

def get_total_page(url, time):
    source_code = requests.get(url, timeout = time).text
    total_page = re.search(r'/<b>(\d+)</b>', source_code).group(1)
    return total_page

def get_picture_url(url, time):
    source_code = requests.get(url, timeout = time).text
    selector = etree.HTML(source_code)
    picture_url = selector.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/img/@src')
    return picture_url

def download_picture(url, time):
    picture = requests.get(url, timeout = time).content
    filename = re.sub(r'.*/', '', url)
    open('pic/' + filename, 'wb').write(picture)

if __name__ == '__main__':
    url = 'http://www.nzchinese.com/tupian/renti/'
    time = 60
    urls = get_urls(url, time)
    count = 1
    for each_url in urls:
        total_page = get_total_page(each_url, time)
        all_page_url = [each_url]
        for i in range(2, int(total_page) + 1):
            new_page_url = re.sub(r'(\d+)(.html$)', '\1' + str(i) + '\2', each_url, time)
            all_page_url.append(new_page_url)
        for each_page_url in all_page_url:
            picture_url = get_picture_url(each_page_url, time)
            for each_picture_url in picture_url:
                download_picture(each_picture_url, time)
                print('Downloading picture ' + str(count) + '...')
                count += 1
