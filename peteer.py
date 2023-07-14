import asyncio,os,time
import pyppeteer
from pyppeteer import launch
from pyppeteer_stealth import stealth
#from pyhtml2pdf import converter
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
artist=r'D:\crawl\weixin_crawl\arti.cache.list'
with open(artist,'r',encoding='utf-8') as f:
    artist_list=f.readlines()
save_path=r'D:\crawl\weixin_crawl\output\new'

async def main():
    i = 0
    for url in artist_list:
        start = time.time()
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
                        }, 300); 
                        });
                }''')
        title =  await page.title()
        output = os.path.join(save_path, title) + ".pdf"
        #content = await page.evaluate('document.body.textContent', force_expr=True)
        intab = r'[|]'
        final = re.sub(intab, "_", output)
        final = ''.join([i.strip(' ') for i in final])
        pdf_file = await page.pdf({"path": final,"format": 'A4'})
        content = await page.content()
        end = time.time()
        total = (end - start)/1000
        #print(f"time: {total} 秒")
        title = await page.title()
        print(f"write {final}\n")
        await browser.close()

#url=r'http://mp.weixin.qq.com/s?__biz=MzIxMDcyMTYzOA==&mid=2247514403&idx=2&sn=b64796d592fe524a3496e2f21cb08892&chksm=9762b72aa0153e3cc12b50c839beaccebcb81bc5c9889989e1d6034d6b51c0abccdfb3673027#rd'
asyncio.get_event_loop().run_until_complete(main())
