import scrapy
from scrapy_splash import SplashRequest
import time
class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['www.quotes.toscrape.com/js']

    script = '''
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(1))
        splash:set_viewport_full()
        return splash:html()
    end
            '''
    def start_requests(self):
        yield SplashRequest(url="http://quotes.toscrape.com/js", callback=self.parse, endpoint="execute", args = {
            'lua_source': self.script
        })     
    def parse(self, response):
        for quotes in response.xpath('//div[@class="quote"]'):
           
            yield{
                'quotes': quotes.xpath('.//span[@class="text"]/text()').get(),
                'author': quotes.xpath('.//span/small/text()').get()
            }
            
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            absolute_url = f"http://quotes.toscrape.com{next_page}"
            yield{
                SplashRequest(url=absolute_url, callback=self.parse, endpoint="execute", args = {
            'lua_source': self.script
            })     
            }
