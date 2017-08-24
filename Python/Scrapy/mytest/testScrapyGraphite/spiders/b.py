# !usr/bin/python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from scrapy import Spider
from testScrapyGraphite.items import MytestItem
# from bs4 import BeautifulSoup


class TestB(Spider):
    name = "mytest_b"
    start_urls = [
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89",
        "http://chejiahao.autohome.com.cn/Authors/RankList?termType=3&termId=0%EF%BC%88%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6%EF%BC%89"]

    def parse(self, response):
        # content = response.body
        # soup = BeautifulSoup(content, "html.parser")
        # for li in soup.find("ul", class_="data-list").find_all("li", class_="data-order"):
        #     print li.find("div", class_="data-name").find("span").text

        # print [i.extract() for i in
        # response.selector.xpath('//ul[@class="data-list"]/li[@class="data-order"]/div[@class="data-name"]/a/span/text()')][0:10]
        for i in response.selector.xpath('//ul[@class="data-list"]/li[@class="data-order"]')[0:10]:
            # co = i.xpath('div[@class="data-name"]/a/span/text()').extract()
            ob = MytestItem()
            ob["my_item"] = i.xpath('div[@class="data-name"]/a/@href').extract()[0]
            yield ob

            # i.xpath('div[@class="data-name"]/a/@href').extract(),
            # i.xpath('div[@class="data-effect"]/text()').extract()]
