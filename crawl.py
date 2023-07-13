
import requests
import re
import json
import os


span_tags = bs.findAll('span', style="font-size: 18px;letter-spacing: 2px;")
<div class="rich_media_content js_underline_content
                       autoTypeSetting24psection
            "
            id="js_content"
# 提取并处理中文内容
chinese_text = ""
for span_tag in span_tags:
    # 获取<span>标签中的文本内容
    text = span_tag.get_text(strip=True)
    # 利用正则表达式提取中文内容和中文标点符号
    chinese_text += ''.join(re.findall(r'[\u4e00-\u9fff，。！？]+', text)) + '\n'

print(chinese_text)


headers = {
    'Host': 'mp.weixin.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63060012)',
    'Cookie': 'wxuin=2408215323; lang=zh_CN; pass_ticket=TsrY5cXMvTN01ghVFxFxT9k4jdPONJBt8mdl0ta20qxjUHNsnkkWLjib4gXCXSQM; devicetype=android-29; version=2800153f; wap_sid2=CJvmqfwIEooBeV9IQVVCUVAzdVBlWEo5NTlySFpON1Ffek5zTE9qRi1jdWZjVFMyOFYyM0FyVE9RSTRNZ3VuUXFTcU94Q3lKY1VyQlJ2RkEtTWFyRWFLeHhJUTRrWmp0N0VDZ05zOFV4d0kzZ1p5cXBIbTVBbEZGRWJteEt4Q0oxSjY4ZHFhODlaZnMyY1NBQUF+MOXS6ZIGOA1AlU4=',
}
# ::text
for page in range(0, 3):
    url = f'https://链接不让发.com/mp/profile_ext?action=getmsg&__biz=MzU0MzU4OTY2NQ==&f=json&offset={page * 10}&count=10&is_ok=1&scene=&uin=777&key=777&pass_ticket=&wxtoken=&appmsg_token=1161_7%252BO7mVaQbImKSRrYWqKBnNggweX4WNZaqjadeg~~&x5=0&f=json'
    json_data = requests.get(url=url, headers=headers).json()
    general_msg_list = json_data['general_msg_list']
    general_msg_list = json.loads(general_msg_list)['list']
    # print(general_msg_list)
    title_list = []
    content_url_list = []
    for general_msg in general_msg_list:
        title = general_msg['app_msg_ext_info']['title']
        content_url = general_msg['app_msg_ext_info']['content_url']
        multi_app_msg_item_list = general_msg['app_msg_ext_info']['multi_app_msg_item_list']
        title_list.append(title)
        content_url_list.append(content_url)
        for multi_app_msg_item in multi_app_msg_item_list:
            title_list.append(multi_app_msg_item['title'])
            content_url_list.append(multi_app_msg_item['content_url'])
    # print(title_list)
    # print(content_url_list)
    zip_data = zip(title_list, content_url_list)
    for detail_title, detail_url in zip_data:
        if not os.path.exists('img/' + detail_title):
            os.mkdir('img/' + detail_title)
        # 1. 发送请求
        response = requests.get(url=detail_url, headers=headers)
        # 2. 获取数据
        html_data = response.text
        # 3. 解析数据
        # 正则匹配数据 第一个参数 需要匹配的规则
        # 第一个参数 在哪个字符串里面匹配
        img_list = re.findall('data-src="(https://mmbiz\.qpic\.cn/.*?)"', html_data)
        print(detail_title)
        # print(img_list)
        for img in img_list:
            if not 'gif' in img:
                img_data = requests.get(img).content
                img_name = img.split('/')[-2]
                print(img_name)
                with open(f'img/{detail_title}/{img_name}.jpeg', mode='wb') as f:
                    f.write(img_data)