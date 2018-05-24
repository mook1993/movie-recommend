# -*- coding: utf-8 -*-

__author__='movie'

import scrapy
from naver_movie.items import NaverMovieItem

class codeSpider(scrapy.Spider):
    name="codeCrawler"
    item = NaverMovieItem()  # items.py 에서 정의한 객체 가져옴
    #start_urls=[]
    #사이트 여러 곳 에서 가져오고자 할 때
    def start_requests(self):
        for i in range(1, 1000, 1):
                yield scrapy.Request("https://movie.naver.com/movie/point/af/list.nhn?&page=%d" % i, self.parse_naver)  #정의한 파서 메서드를 인자로...

    def parse_naver(self,reponse):
        for sel in reponse.xpath('//tbody/tr'):
            item=self.item
            #dateTmp=datetime.strptime(sel.xpath('td[@class="num"]/text()').extract()[-1], "%YY.%mm.%dd")
            item['source'] = '네이버'
            item['title'] = sel.xpath('td[@class="title"]/a/text()').extract()[0]
            item['desc']=sel.xpath('td[@class="title"]/text()').extract()[2]
            item['url'] = 'https://movie.naver.com/movie/point/af/list.nhn' + sel.xpath('td[@class="title"]/a/@href').extract()[0]

            # 사이트 마다 표기하는 날짜 형식이 다름, 따라서 dateTmp가 어떤 타입인지 모르기 때문에, str타입으로 한번 더 바꿔줌
            #item['date'] =dateTmp.strftime("%Y-%m-%d")
            item['date']=sel.xpath('td[@class="num"]/text()').extract()[-1]
            item['stars'] = int(sel.xpath('td[@class="point"]/text()').extract()[0])

            print '*' * 50
            print item['title']

            yield item