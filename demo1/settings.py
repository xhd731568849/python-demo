# -*- coding: UTF-8 -*-
BOT_NAME = 'python-demo'

SPIDER_MODULES = ['demo1.spiders']
NEWSPIDER_MODULE = 'demo1.spiders'

# 禁止cookies,防止被ban
COOKIES_ENABLED = False
COOKIES_ENABLES = False

# 设置Pipeline,此处实现数据写入文件
ITEM_PIPELINES = {
    'demo1.pipelines.TutorialPipeline': 300
}

# 设置爬虫爬取的最大深度
DEPTH_LIMIT = 100