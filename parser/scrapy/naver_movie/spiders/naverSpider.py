# -*- coding: utf-8 -*-

__author__='movie'

import scrapy
from naver_movie.items import NaverMovieItem
from datetime import datetime
from operator import eq

class naverSpider(scrapy.Spider):
    name="naverReviewCrawler"

    #사이트 여러 곳 에서 가져오고자 할 때
    def start_requests(self):
        for year in range(2016,2017,1):
            yield scrapy.Request("https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=%d&page=%d" % (year, 1), self.parse_code, meta={'year': year, 'page': 1})
            # for page in range(1,2,1): #디렉터리 페이지 순회
            #     yield scrapy.Request("https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=%d&page=%d" %(year,page), self.parse_code,meta={'year':year,'page':page})

    #paging!!!
    def parse_code(self,reponse):
        year=reponse.meta['year']
        page=reponse.meta['page']

        #영화가아닌것들은pass
        for sel in reponse.xpath('//ul[@class="directory_list"]/li'):
            code=int(sel.xpath('a/@href').extract()[0].split("=")[-1])
            flag=1
            for jenreSel in sel.xpath('ul[@class="detail"]/li/a/text()'):
                jenStr=jenreSel.extract()
                if eq(jenStr,u'웹드라마') or eq(jenStr,u'TV시리즈') or eq(jenStr,u'뮤비직디오'):
                    print '-'*50
                    print 'filter: ['+str(code)+'] --->'+str(year)+'년 '+str(page)+'페이지'
                    print jenreSel.extract()
                    print '-'*50
                    flag=-1
                    break

            if flag==-1:
                continue

            print '디렉터리: ['+str(code)+'] --->'+str(year)+'년 '+str(page)+'페이지'

            yield scrapy.Request("https://movie.naver.com/movie/bi/mi/point.nhn?code=%d" % code, self.parse_movieName, meta={'code': code})

        for sel in reponse.xpath('//td[@class="next"]'):
            print 'check!!'
            yield scrapy.Request("https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=%d&page=%d" % (year, page+1), self.parse_code, meta={'year': year, 'page': page+1})


    def parse_movieName(self,reponse):
        url="https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=%d&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%d"
        code=reponse.meta['code']
        title= reponse.xpath('//div[@class="mv_info_area"]/div[@class="mv_info"]/h3/a/text()').extract()[0]
        yield scrapy.Request(url % (code, 1), self.parse_shortReview, meta={'code': code, 'title': title, 'page': 1})  # A페이지에서 추출한 데이터 B페이지로 넘김


    #!!!페이징기법!!!
    def parse_shortReview(self,reponse):
        for sel in reponse.xpath('//div[@class="score_result"]/ul/li'):
            url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=%d&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%d"
            page = reponse.meta['page']
            code = reponse.meta['code']
            title = reponse.meta['title']

            # print '!'*100
            # print '['+title+']'+'['+str(code)+']'+'['+str(page)+']'

            infoSel=sel.xpath('div[@class="score_reple"]/dl/dt/em')   #!!!엘리먼트를 순서말고는 구분할 방법이 없는 경우 이런 식으로 해결
            sympSel=sel.xpath('div[@class="btn_area"]/strong')

            item = NaverMovieItem()  # items.py 에서 정의한 객체 가져옴
            item['source'] = '네이버'
            item['code']=code
            item['title'] = title
            item['stars']=int(sel.xpath('div[@class="star_score"]/em/text()').extract()[0])
            item['desc'] = sel.xpath('div[@class="score_reple"]/p/text()').extract()[0]

            item['nickName'] = infoSel[0].xpath('a/span/text()').extract()[0]
            reviewDate_Str = infoSel[1].xpath('text()').extract()[0] + ":00"
            item['reviewDate']=datetime.strptime(reviewDate_Str,"%Y.%m.%d %H:%M:%S")
            item['sympathy']=int(sympSel[0].xpath('span/text()').extract()[0])
            item['notSympathy']=int(sympSel[1].xpath('span/text()').extract()[0])

            # print '-'*100
            #print reponse.url
            # print item['code']
            # print item['title']
            # print item['reviewDate']
            # print item['sympathy']
            # print item['notSympathy']
            # print item['desc']
            # print item['nickName']

            yield item

        # 다음 페이지가 있을 경우 다음 페이지 요청
        for sel in reponse.xpath('//div[@class="paging"]/div/a[@class="pg_next"]'):
            yield scrapy.Request(url % (code, page+1), self.parse_shortReview, meta={'code': code, 'title': title, 'page': page+1})


