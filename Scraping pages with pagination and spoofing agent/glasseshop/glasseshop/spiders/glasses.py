import scrapy
import re

class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for glass in response.xpath('//div[@id="product-lists"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            glass_name = glass.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[@class="col-6 col-lg-6"]/div[@class="p-title"]/a/text()').get()
            glass_price =  glass.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div[@class="row no-gutters"]/div[@class="col-6 col-lg-6"]/div[@class="p-price"]/div[1]/span/text()').get()
            glass_link = glass.xpath('.//div[@class="product-img-outer"]/a[1]/@href').get()
            glass_image_link = glass.xpath('.//div[@class="product-img-outer"]/a[1]/img[1]/@data-src').get()
            glass_name = re.sub(r"[\n\t\s]*", "", glass_name)

            
            
            yield{
                "glass_link": glass_link,
                "glass_image_link": glass_image_link,
                "glass_name": glass_name,
                "glass_price": glass_price
            }
        
        next_page = response.xpath('//div[@class="row mt-5 mb-5 d-none d-lg-block"]/div/ul/li[6][@class="page-item"]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
