# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PatentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    patents = scrapy.Field()
    sdate = scrapy.Field()
    edate = scrapy.Field()
    #inventor = scrappy.Field()
    #city = scrappy.Field()
    
    pass
