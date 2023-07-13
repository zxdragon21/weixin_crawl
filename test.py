# -*- coding: utf-8 -*-
from selenium import webdriver
import time,glob2,pdfkit
#import wkhtmltopdf
from bs4 import BeautifulSoup
import requests
import re
import shutil
import os
import json
import argparse
import parsel
from pathlib import Path

class Session:
    token = ''
    cookies = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

class Urls:
    index = 'https://mp.weixin.qq.com'
    editor = 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&share=1&lang=zh_CN&token={token}'
    query_biz = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?action=search_biz&token={token}&lang=zh_CN&f=json&ajax=1&random={random}&query={query}&begin={begin}&count={count}'
    query_arti = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token={token}&lang=zh_CN&f=json&%E2%80%A65&action=list_ex&begin={begin}&count={count}&query={query}&fakeid={fakeid}&type=9'

headers = {
'Host': 'mp.weixin.qq.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090551) XWEB/6945',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh',
}
options = {
            'page-size': 'Letter',
            'encoding': "utf-8",
            #'disable-javascript': True,
            'no-images': True,
            #'disable-external-links': True,
            #'enable-local-file-access': True,
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ]
        }
path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
file=r'D:\crawl\wxhub\output\陀乐寺\2023年正月禅修班开示三十二如何决定临终时往生善道还是堕恶道呢？\index.html'
url=r'http://mp.weixin.qq.com/s?__biz=MzIxMDcyMTYzOA==&mid=2247514403&idx=2&sn=b64796d592fe524a3496e2f21cb08892&chksm=9762b72aa0153e3cc12b50c839beaccebcb81bc5c9889989e1d6034d6b51c0abccdfb3673027#rd'
path=r'D:\crawl\wxhub\output\陀乐寺\**\index.html'
file_list=(glob2.glob(path))
save_dir=r'D:\crawl\wxhub\output\save'
response = requests.get(url=url, headers=headers, verify=False)
pdfkit.from_url(url,'./out.pdf',configuration=config,options=options)
import pdb
#pdb.set_trace()
i=0
for file in file_list:
    with open(file,'r',encoding='utf-8') as f:
        temp=f.read()
        bs = BeautifulSoup(temp, 'lxml')
        div_tag = bs.find('div', class_='rich_media_content')
        # 输出<div>标签的内容
        if div_tag:
            content = div_tag.get_text()
        else:
            print("未找到匹配的<div>标签")
        script_tags = bs.findAll('script', type="text/javascript")
        for script_tag in script_tags:
            # 提取<script>标签的文本内容
            script_content = script_tag.string
            # 使用正则表达式提取 var title 的值
            match = re.search(r"var\s+msg_title\s+=\s+'([^']+)'.html\(false\);", script_content)
            if match:
                title = match.group(1)
                print(title)
        print(content)
        output = os.path.join(save_dir,str(i))+".pdf"
        import pdb
        #pdb.set_trace()
        i+=1
        pdfkit.from_file(file,output,configuration=config,options=options)
        #pdfkit.from_url(url,output,configuration=config,options=options)

#selector = parsel.Selector(tex)
#print("css",selector.css('#sg_tj'))
