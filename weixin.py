"""
采集微信公众号
Python学习交流q群：708525271
VIP课程咨询添加微信：Python1018
"""
import requests, lxml
import json
import re
from bs4 import BeautifulSoup

headers = {
    'Host': 'mp.weixin.qq.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090016)',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': '*/*',
    'Cookie': 'wxuin=2408215323; lang=zh_CN; devicetype=android-29; version=28002037; pass_ticket=f85UL5Wi11mqpsvuWgLUECYkDoL2apJ045mJw9lzhCjUteAxd4jM8PtaJCM0nBXrQEGU9D7ulLGrXpSummoA==; wap_sid2=CJvmqfwIEooBeV9IR29XUTB2eERtakNSbzVvSkhaRHdMak9UMS1MRmg4TGlaMjhjbTkwcks1Q2E2bWZ1cndhUmdITUZUZ0pwU2VJcU51ZWRDLWpZbml2VkF5WkhaU0NNaDQyQ1RDVS1GZ05mellFR0R5UVY2X215bXZhUUV0NVlJMVRPbXFfZGQ1ZnVvMFNBQUF+MPz0/50GOA1AlU4=',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=Mzg3Nzc2OTQzOA==&uin=MjQwODIxNTMyMw%3D%3D&key=2ed1dc903dceac3d9a380beec8d46a84995a555d7c7eb7b793a3cc4c0d32bc588e1b6df9da9fa1a258cb0db4251dd36eda6029ad4831c4d57f6033928bb9c64c12b8e759cf0649f65e4ef30753ff3092a2a4146a008df311c110d0b6f867ab173792368baa9aaf28a514230946431480cc6b171071a9f9a1cd52f7c07a751925&devicetype=Windows+10+x64&version=63090016&lang=zh_CN&a8scene=7&session_us=gh_676b5a39fe6e&acctmode=0&pass_ticket=f85UL5Wi11%2BmqpsvuW%2BgLUECYkDoL2apJ045mJw9lzhCjUteAxd4jM8PtaJCM0nBXrQEGU9D7ulLGrXpSummoA%3D%3D&wx_header=1&fontgear=2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
index = 0
file=r'D:\crawl\wxhub\output\陀乐寺\2023年正月禅修班开示三十二如何决定临终时往生善道还是堕恶道呢？\index.html'
for page in range(1, 5):
    url = r'https://mp.weixin.qq.com/mp/relatedarticle?action=getlist&article_url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FwZvFaFNhOHzbK0KecTp3IA&__biz=MzU5MjgwMDMwNQ==&mid=2247531038&idx=1&has_related_article_info=0&is_pay=0&is_from_recommand=0&scene=0&subscene=0&is_open_comment=undefined&uin=&key=&pass_ticket=&wxtoken=777&devicetype=&clientversion=&__biz=MzU5MjgwMDMwNQ%3D%3D&appmsg_token=&x5=0&f=json'

    response = requests.get(url=url, headers=headers, verify=False)
    import pdb
    bs = BeautifulSoup(response.text, "lxml")
    pdb.set_trace()
    #general_msg = bs['general_msg_list']
    div_tag = bs.find('div', class_='rich_media_content')
    if div_tag:
        content = div_tag.get_text()
        print(content)
    else:
        print("未找到匹配的<div>标签")
      # for general in a['list']:
      #   content_url = general['app_msg_ext_info']['content_url']
      #   html_data = requests.get(url=content_url, headers=headers, verify=False).text
      #   img_list = re.findall('<img class=".*?data-src="(.*?)"', html_data)
      #   print(img_list)
      #   for img in img_list:
      #       img_data = requests.get(url=img, verify=False).content
      #       open(f'img/{index}.jpg', mode='wb').write(img_data)
      #       index += 1