## 启动爬虫
    $切换到项目根目录
    #仅仅将采集到的数据打印在终端上
    $ scrapy crawl toscrape-css
    #保存采集到的数据到一个文件上
    $ scrapy crawl toscrape-css -o quotes.json
--------------------------------------------------
#标注
原来写过一些爬虫，但一直不喜欢用框架，听过讲师的课后觉得真的应该学一下框架，这里
用的是scrpy爬虫框架,看着scrapy的文档写的这个爬虫，个人感觉python最强的还是爬虫，
希望可以弥补一些前端的不足:)
### 提取数据
这个爬虫采集了 http://quotes.toscrape.com 这个网站中的名人名言，输出格式如下
    {
        'author': 'author name',
        'text': '“autor's quoto”',
        'tags': ['life', 'thinking']
    }
### 选择器
选择器采用css()；爬虫文件toscrape-css
