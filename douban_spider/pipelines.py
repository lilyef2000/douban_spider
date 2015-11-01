# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')



class DoubanSpiderPipeline(object):
    def  __init__(self):
        self.file=codecs.open('douban_movie2.json',mode='wb',encoding='utf-8')
    def process_item(self, item, spider):

#        for i in item['movie_name']:
#            print "~~~~~~~~~~~~~~~~~~~\n"
#            print i
#            print "~~~~~~~~~~~~~~~~~~~~\n"

        line='the list:'+'\n'
        for i in range(len(item['quote'])):#quote movie_name
            #movie_name={"movie_name":item['movie_name'][i]}
            movie_name={'movie_name':str(item['movie_name'][i]).replace(' ','')}
            star={"star":item['star'][i]}
            #quote={"quote":item['quote'][i]}
            quote={'quote':str(item['quote'][i]).replace(' ','')}
            line=line+json.dumps(movie_name,ensure_ascii=False)
            line=line+json.dumps(star,ensure_ascii=False)
            line=line+json.dumps(quote,ensure_ascii=False)+"\n"



        self.file.write(line)
        
    def close_spider(self,spider):
        self.file.close()
