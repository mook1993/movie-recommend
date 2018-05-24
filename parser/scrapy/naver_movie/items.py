# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NaverMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code=scrapy.Field()
    source=scrapy.Field()
    title = scrapy.Field()
    stars=scrapy.Field()
    desc=scrapy.Field()
    reviewDate= scrapy.Field()
    nickName=scrapy.Field()
    sympathy=scrapy.Field()
    notSympathy = scrapy.Field()
    pass


class NaverMovieInfoItem(scrapy.Item):
    code=scrapy.Field()
    title=scrapy.Field()
    jenre=scrapy.Field()
    country=scrapy.Field()
    runningTime=scrapy.Field()
    openDate=scrapy.Field()
    director=scrapy.Field()
    actors=scrapy.Field()
    viewingClass=scrapy.Field()
    audienceStar=scrapy.Field()
    criticStar=scrapy.Field()
    NetizenStar=scrapy.Field()
    audienceStarParticipantNum=scrapy.Field()
    NetizenStarParticipantNum = scrapy.Field()
    pass