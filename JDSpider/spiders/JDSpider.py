#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__author__ = 'Kandy.Ye'
__mtime__ = '2017/4/12'
"""

import logging
import json
import requests
import MySQLdb
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from JDSpider.items import *
from twisted.enterprise import adbapi

key_word = ['book', 'e', 'channel', 'mvd', 'list']
Base_url = 'https://list.jd.com'
price_url = 'https://p.3.cn/prices/mgets?skuIds=J_'
comment_url = 'https://club.jd.com/comment/productPageComments.action?productId=%s&score=0&sortType=5&page=%s&pageSize=10'
favourable_url = 'https://cd.jd.com/promotion/v2?skuId=%s&area=1_72_2799_0&shopId=%s&venderId=%s&cat=%s'


class JDSpider(Spider):
    name = "JDSpider"
    allowed_domains = ["jd.com"]
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="test", charset="utf8")
    cursor = conn.cursor()
    # start_urls = [
    #     'https://www.jd.com/allSort.aspx'
    # ]
    sql="SELECT product_id from product_item WHERE original_price=0.0000 OR really_price=0.0000 limit 0,200000"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    logging.getLogger("requests").setLevel(logging.ERROR)  # 将requests的日志级别设成WARNING

    def start_requests(self):
        for url in self.result:
            target_url=price_url+str(url[0])
            yield Request(url=target_url, callback=self.parse_product_price)

    def parse_product_price(self, response):
        """获取商品价格"""
        productsItem = ProductsItem()
        try:
            price_json = eval(response.text.strip()[1:-1])
        except Exception as e:
            print(e)
        try:
            productsItem['reallyPrice'] = price_json['p']
        except Exception as e:
            productsItem['reallyPrice'] = 0
        try:
            productsItem['originalPrice'] = price_json['m']
        except Exception as e:
            productsItem['originalPrice'] = 0

        productsItem['_id'] =price_json['id'][2:]
        yield productsItem

