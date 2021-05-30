### Install and setting up scrapy-splash

```
pip install scrapy-splash
```

Then open settings.py of scrapy project and add

```
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
```
```
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
```
```
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
```