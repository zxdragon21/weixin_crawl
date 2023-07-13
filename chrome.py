import pdfkit, time, pprint,json,os
from selenium import webdriver
from pyhtml2pdf import converter
#import PDFDoc
#from weasyprint import HTML
def set_cookies(driver, cookies):
    Session.cookies = {}
    for item in cookies:
        driver.add_cookie(item)
        Session.cookies[item['name']]=item['value']
class Session:
    token = ''
    cookies = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

options_chrome = webdriver.ChromeOptions()
# 以最高权限运行
options_chrome.add_argument('--no-sandbox')
# 浏览器不提供可视化页面，linux下如果系统不支持可视化不加这条会启动失败
options_chrome.add_argument('--headless')
# executable_path为chromedriver的位置
driver = webdriver.Chrome(executable_path=r'D:\crawl\wxhub\chromedriver.exe', chrome_options=options_chrome)
# 浏览器全屏
path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
driver.fullscreen_window()
file=r'D:\crawl\wxhub\output\陀乐寺\大爱无疆八万四千法门，藏传佛教如何学习的？\index.html'
url=r'http://mp.weixin.qq.com/s?__biz=MzIxMDcyMTYzOA==&mid=2247514357&idx=1&sn=f8fb563543cf70e7aabd680f30512d1b&chksm=9762b6fca0153feab78d73bde243ce4a16deeb3c3b08d1d63a19658bea59810ccace8818c3e1#rd'
driver.get(url)
cookies = json.load(open('cookies.json', 'rb')) if os.path.isfile('cookies.json') else []
set_cookies(driver, cookies)
driver.get(url)
time.sleep(5)
source_text = driver.page_source
converter.convert(url, './test2.pdf', compress=False,power=1,timeout=10)
#webdriver.execute_script('window.location="'+url+'";')
#converter.convert(url, './test3.pdf', compress=False,power=1,timeout=10)
# sleep 1秒
# html_content = driver.find_element('By.CLASS_NAME', "rich_media").text
# # html1 = HTML(string = html_content)
# # html1.write_pdf('test.pdf')
# import pdb
# #pdb.set_trace()
# options_pdf = {
#     'page-size': 'Letter',
#     'encoding': "UTF-8"
# }
# result = pdfkit.from_string(source_text, "./0.pdf", configuration=config,options=options_pdf)
# pdb.set_trace()
driver.quit()