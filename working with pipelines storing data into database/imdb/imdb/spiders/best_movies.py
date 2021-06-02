import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import re

class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url="https://www.imdb.com/chart/top", headers={
            "User-Agent" : self.user_agent
        },
        meta={'donwload_timeout': 10})

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//table/tbody/tr/td[2]/a'), callback='parse_item', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request, response):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        time.sleep(1) # load time sleep
        title = response.xpath('//div[@class="title_bar_wrapper"]/div[@class="titleBar"]/div[@class="title_wrapper"]/h1/text()').get()
        year = response.xpath('//span[@id="titleYear"]/a/text()').get()
        duration = response.xpath('//div[@class="subtext"]/time/text()').get()
        genre = response.xpath('//div[@class="subtext"]/a[1]/text()').get()
        rating = response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        #title = re.sub(r"\xa0", '', title)
        duration = re.sub(r"[\n\t\s]*", "", str(duration))


        yield{
            "title": title,
            "year": year,
            "duration": duration,
            "genre": genre,
            "rating":rating
        }
        time.sleep(0.3) # load time sleep 
