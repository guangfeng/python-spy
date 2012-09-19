#!/usr/bin/env python
# encoding: utf-8
"""
baidu.py

Created by Guang Feng on 2012-06-23.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os.path as path
#development load module
import os
if os.path.exists(os.path.join(os.path.dirname(sys.argv[0]), os.pardir, 'spy')):
    sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), os.pardir))
#development load end

from spy import *
import re

CURRENT_PATH = path.dirname(path.abspath(__file__))

class BaiduSpy(object):
    def generator_index(self):
        for i in xrange(1,3):
            yield self.parser_index,"http://www.baidu.com/s?wd=python&pn=10&usm=%d&rsv_page=1"%i
    
    def parser_index(self,page,url):
        re_item = re.compile(r'<a\s*onmousedown="*?".*?href="(.*?)"\s*target="_blank"\s*>.*?<em>.*?</em>(.*?)</a>',re.I|re.M|re.S)
        items = re_item.findall(page)
        for i in items:
            print i[0],'=>',i[1]
        
        download_file(url,'./cache/'+url.replace('/','_'))
        return None
            
B = BaiduSpy()
fetcher = Fetch(cache = 'cache')
spider = Rolling(fetcher,B.generator_index())
spider_runner = GSpider(spider, workers_count=3)
spider_runner.start()
        