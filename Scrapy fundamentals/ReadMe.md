### Some commands for scrapy
```
scrapy bench
```
Used to perform benchmark for scrapping 
```
scrapy fetch https://google.com
```
Fetch a url using Scrapy downloader 

## Start a project 
```
scrapy startproject worldometerspopulation
```
## Create a genspider 
Go to worldometerspopulation population and start genspider 

```
scrapy genspider countries https://www.worldometers.info/world-population/population-by-country
```

# Scrapy Shell
Run 
```
scrapy shell
```

Inside shell
```
fetch("https://www.worldometers.info/world-population/population-by-country/")
```
Note - If we can't find robots.txt after fetching (ie. robots.txt get return 404) that means we can scrap

## Return the HTML markup of te website


```
r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")

fetch(r)

response.body # Return the HTML markup of the website
```

## View the scraped response 
```
view(response)
```

Note - Scrapy see website without Javascript so we should always check our website which we want to scrap without javascript 

### Some ways to extract a specific div/classes 
```
title = response.xpath("//h1")
title

#Output
[<Selector xpath='//h1' data='<h1>Countries in the world by populat...'>]

title = response.xpath("//h1/text()")
title
title.get()
```

### Basic scrapping in worldometerspopulation project