import asyncio,os
import pyppeteer
from pyppeteer import launch
from pyppeteer_stealth import stealth
from pyhtml2pdf import converter
from bs4 import BeautifulSoup
import re, lxml
launch_kwargs = {
        # 控制是否为无头模式
        'headless': False,
        # chrome启动命令行参数
        "args": [
            # 浏览器代理 配合某些中间人代理使用
            #"--proxy-server=http://127.0.0.1:8008",
            "--start-maximized",
            "--no-sandbox",
            "--disable-infobars",
            "--log-level=3",
            # 设置UA
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        ],
       	"dumpio":True,
        "userDataDir": "./"
    }

artist=r'D:\crawl\wxhub\arti.cache.list'
with open(artist,'r',encoding='utf-8') as f:
    artist_list=f.readlines()
save_path=r'D:\crawl\wxhub\output\save'

async def main():
    i = 0
    for url in artist_list:
        import pdb
        #pdb.set_trace()
        browser = await pyppeteer.launch()
        page = await browser.newPage()
        await page.setViewport({'width': 1920, 'height': 1080})  # 调整页面的尺寸为 1920*1080
        await page.setJavaScriptEnabled(enabled=True)  # 允许 javascript 执行
        # 隐藏特征

        #await stealth(page)
        await page.goto(url,{
            'waitUntil': 'networkidle0',
            #'timeout': 1000
        })
        await page.waitFor(1000)
        await page.evaluate('window.scrollBy(0,document.body.scrollHeight)')
        #content = await page.evaluate('document.body.textContent', force_expr=True)
        pdf_file = await page.pdf({"format": 'A4'})
        content = await page.content()
        #title = page.title()

        bs = BeautifulSoup(content,'lxml')
        #print(bs)
        script_tags = bs.findAll('script', type="text/javascript")
        for script_tag in script_tags:
            # 提取<script>标签的文本内容
            script_content = script_tag.string
            # 使用正则表达式提取 var title 的值
            match = re.search(r"var\s+msg_title\s+=\s+'([^']+)'.html\(false\);", script_content)
            if match:
                title = match.group(1)
                print(title)
        import pdb
        #pdb.set_trace()
        output = os.path.join(save_path,str(i))+".pdf"
        i+=1
        with open(r"D:\crawl\wxhub\output\save\artilist.txt",'a',encoding='utf-8') as g:
            g.write(title)
            g.write("\n")
        with open(output,'wb') as f:
            f.write(pdf_file)
        #print(pdf_file)
        #converter.convert(pdf_file, './test2.pdf', compress=False, power=1, timeout=5)
        print(f"write {title} done!\n")
        await asyncio.sleep(1)
        await browser.close()

#url=r'http://mp.weixin.qq.com/s?__biz=MzIxMDcyMTYzOA==&mid=2247514403&idx=2&sn=b64796d592fe524a3496e2f21cb08892&chksm=9762b72aa0153e3cc12b50c839beaccebcb81bc5c9889989e1d6034d6b51c0abccdfb3673027#rd'
asyncio.get_event_loop().run_until_complete(main())
