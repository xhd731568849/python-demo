# -*- coding: UTF-8 -*-
from scrapy import cmdline

# https://www.cnblogs.com/liruihua/p/5957393.html ....demo网址

if __name__=="__main__":
    cmdline.execute("scrapy crawl demo1".split())