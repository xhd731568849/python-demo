# -*- coding: UTF-8 -*-
import json
import codecs


class TutorialPipeline(object):
 def __init__(self):
     self.file = codecs.open('data.json', mode='wb', encoding='utf-8')#数据存储到data.json

 def process_item(self, item, spider):
     line = json.dumps(dict(item)) + "\n"
     self.file.write(line.decode("unicode_escape"))

     return item