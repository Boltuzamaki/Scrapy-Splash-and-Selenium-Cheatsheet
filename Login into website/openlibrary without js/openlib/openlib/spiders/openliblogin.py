import scrapy
from scrapy import FormRequest

class OpenlibloginSpider(scrapy.Spider):
    name = 'openliblogin'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response):
        
        yield FormRequest.from_response(
                response,
                formid = 'register',
                
                formdata = {
                    "username": "divyanshuboltuzamaki23@gmail.com",
                    "password": "Naruto23@#$",
                    "redirect": "/",
                    "debug_token": "",
                    "login" : "Log In"
                },
                callback = self.after_login
            )
    def after_login(self, response):
        print("Logged in ....")
