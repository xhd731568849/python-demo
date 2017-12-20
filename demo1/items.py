# -*- coding: UTF-8 -*-
import scrapy
from scrapy.item import Item,Field

class TutorialItem(Item):
    title = Field()
    author = Field()
    releasedate = Field()
