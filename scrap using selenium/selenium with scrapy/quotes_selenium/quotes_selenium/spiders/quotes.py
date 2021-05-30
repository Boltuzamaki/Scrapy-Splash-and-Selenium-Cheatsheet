import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector

class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        yield SeleniumRequest(url="http://quotes.toscrape.com/js",
        wait_time=3, 
        screenshot=True,
        callback=self.parse
            )     

    def parse(self, response):
      # note if intial response is modiefied by like filling value to input automatic by selenium then we need to use the commented line
      #  driver = response.meta['driver']
      #  driver.save_screenshot('quote.png')
      #  html = driver.page_source
     #  response_obj = Selector(text=html)
        for quotes in response.xpath('//div[@class="quote"]'):
           
            yield{
                'quotes': quotes.xpath('.//span[@class="text"]/text()').get(),
                'author': quotes.xpath('.//span/small/text()').get()
            }
            
        next_page = response.xpath('//li[@class="next"]/a/@href').get()

        if next_page:
            
            absolute_url = f"http://quotes.toscrape.com{next_page}"
            print(absolute_url)
            yield SeleniumRequest(url=absolute_url,
                            wait_time=3, 
                            screenshot=True,
                            callback=self.parse
                )
            