# -*- coding: utf-8 -*-

__author__='movie'

import scrapy
from naver_movie.items import NaverMovieInfoItem
from datetime import datetime
from operator import eq

class naverMovieInfoSpider(scrapy.Spider):
    name="naverMovieInfoCrawler"

    #사이트 여러 곳 에서 가져오고자 할 때
    def start_requests(self):
        for year in range(1990,2019,1):
            yield scrapy.Request("https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=%d&page=%d" % (year, 1), self.parse_code, meta={'year': year, 'page': 1})

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
                    flag=-1
                    break

            if flag==-1:
                continue

            yield scrapy.Request("https://movie.naver.com/movie/bi/mi/point.nhn?code=%d" % code, self.parse_movieInfo, meta={'code': code})

        for sel in reponse.xpath('//td[@class="next"]'):
            print 'check!!'
            yield scrapy.Request("https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open=%d&page=%d" % (year, page+1), self.parse_code, meta={'year': year, 'page': page+1})


    def parse_movieInfo(self,response):
        item=NaverMovieInfoItem()
        jenreStr=""
        actorStr=""
        overviewSel=response.xpath('//div[@class="mv_info_area"]/div[@class="mv_info"]/dl[@class="info_spec"]/dd/p/span')
        specSel=response.xpath('//div[@class="mv_info_area"]/div[@class="mv_info"]/dl[@class="info_spec"]/dd')
        scoreSel=response.xpath('//div[@class="mv_info_area"]/div[@class="mv_info"]/div[@class="main_score"]/div')

        for jenre in overviewSel[0].xpath('a/text()').extract():
            jenreStr+=jenre+"|"

        actorsel=specSel[2]
        for actor in actorsel.xpath('p/a/text()').extract():
            actorStr+=actor+"|"

        audiScoreSel=scoreSel[0].xpath('a[@id="actualPointPersentBasic"]/div/em/text()').extract()
        criticScoreSel=scoreSel[1].xpath('div/a/div/em/text()').extract()
        netizenScoreSel=response.xpath('//a[@id="pointNetizenPersentBasic"]/em/text()').extract()
        AudiscoreStr=""
        for token in audiScoreSel:
            AudiscoreStr+=token
        criticScoreStr=""
        for token in criticScoreSel:
            criticScoreStr+=token
        netizenScoreStr=""
        for token in netizenScoreSel:
            netizenScoreStr+=token

        openDateSel=overviewSel[3].xpath('a/text()')
        openDateStr=(openDateSel[0].extract()+openDateSel[1].extract())[1:] #year + month.day
        item['code'] = response.meta['code']
        item['title'] = response.xpath('//div[@class="mv_info_area"]/div[@class="mv_info"]/h3/a/text()').extract()[0]
        item['jenre']= jenreStr
        item['country']=overviewSel[1].xpath('a/text()').extract()[0]
        item['runningTime']=overviewSel[2].xpath('text()').extract()[0]
        item['openDate']=datetime.strptime(openDateStr,"%Y.%m.%d")
        item['director']=specSel[1].xpath('p/a/text()').extract()[0]
        item['actors']=actorStr
        item['viewingClass']=specSel[3].xpath('p/a/text()').extract()[0]
        item['audienceStar']= "N/A" if eq(AudiscoreStr,"") else float(AudiscoreStr)
        item['criticStar']="N/A" if eq(criticScoreStr,"") else float(criticScoreStr)
        item['NetizenStar'] = "N/A" if eq(netizenScoreStr, "") else float(netizenScoreStr)
        item['audienceStarParticipantNum']=int(response.xpath('//div[@id="actualPointCountBasic"]/em/text()').extract()[0])
        item['NetizenStarParticipantNum'] = int(response.xpath('//div[@id="pointNetizenCountBasic"]/em/text()').extract()[0])

        yield item


