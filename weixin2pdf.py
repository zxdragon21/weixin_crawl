"""
采集微信公众号
Python学习交流q群：708525271
VIP课程咨询添加微信：Python1018
"""
import requests, lxml
import json
import re
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio
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
url = r'http://mp.weixin.qq.com/s?__biz=MzIxMDcyMTYzOA==&mid=2247514340&idx=6&sn=3777dd2604eee179298932008e77c13e&chksm=9762b6eda0153ffbff1e39fbdd1aceae8f3e2285c17fa4b25d8fa6e5c9b7cf4aeda00e75b819#rd'
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True,
                                    args=['--start-maximized'],
                                    slow_mo=3000
                                    )
        context = await  browser.new_context(viewport={"width":1920,"height":1080})
        page = await context.new_page()
        await  page.goto(url,wait_until="networkidle")
        import pdb
        print(await page.title())
        await page.evaluate('''async () => {
                                    await new
                                Promise((resolve, reject) => {
                                    var
                                totalHeight = 0;
                                var
                                distance = 1000;
                                var
                                timer = setInterval(() => {
                                    var
                                scrollHeight = document.body.scrollHeight;
                                window.scrollBy(0, distance);
                                totalHeight += distance;

                                if (totalHeight >= scrollHeight){
                                clearInterval(timer);
                                resolve();
                                }
                                }, 500);
                                });
                        }''')
        #pages = await context.background_pages
        await page.screenshot(path=f'screenshot.png')
        pdb.set_trace()
        pdf_file = await page.pdf()
        with open("test.pdf",'wb') as f:
            f.write(pdf_file)

asyncio.run(main())

