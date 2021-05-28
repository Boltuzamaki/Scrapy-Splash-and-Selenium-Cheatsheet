import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            #absolute_url =f"https://www.worldometers.info/{link}" #Way 1
            #absolute_url =  response.urljoin(link)  #Way 2
            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link, callback=self.parse_country, meta={"country_name":name})

# Meta help to sync the extracted data between more than one parsing methods 
    def parse_country(self, response):
        country_name = response.request.meta["country_name"]
        rows = response.xpath('//div[@class="table-responsive"]/table[@class="table table-striped table-bordered table-hover table-condensed table-list"][1]/tbody/tr')
        for r in rows:
            year = r.xpath(".//td[1]/text()").get()
            population = r.xpath(".//td[2]/strong/text()").get()

            yield{
                "country_name": country_name,
                "year":year,
                "population": population
            }

