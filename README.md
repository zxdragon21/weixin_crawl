## 公众号文章抓取工具
爬取微信公众号所有历史文章，参考了现有项目，爬取历史文章url。然后通过playwright，pyppeteer渲染网页，将html转成pdf格式下载。

### 1.抓取公众号历史文章url
```
(py3) isyuu:wxhub isyuu$ python wxhub.py -h
usage: wxhub.py [-h] -biz BIZ [-chrome CHROME] [-arti ARTI] [-method METHOD]
                [-sleep SLEEP] [-pipe PIPE] [-pl PAGE_LIMIT]

公众号文章全搞定

optional arguments:
  -h, --help      show this help message and exit
  -biz BIZ        必填:公众号名字
  -chrome CHROME  可选:web chrome 路径, 默认使用脚本同级目录下的chromedriver
  -arti ARTI      可选:文章名字, 默认处理全部文章
  -method METHOD  可选, 处理方法: all_images, baidu_pan_links, whole_page
  -sleep SLEEP    翻页休眠时间, 默认为1即 1秒每页.
  -pipe PIPE      在method指定为pipe时, 该参数指定pipe处理流程. 例如:"pipe_example,
                  pipe_example1, pipe_example2, pipe_example3"
  -pl PAGE_LIMIT  指定最大翻页次数, 每次同一个公众号, 翻页太多次会被ban, 0:不翻页 只处理todo.list, 默认<0:无限制
                  >0:翻页次数

```

###2.抓取文章内容并转存为pdf
```
peteer.py
采用pyppeteer异步执行模式，page.evaluate将文章所有页面加载，当网页及所有资源加载后，将网页转成pdf保存到本地。
```