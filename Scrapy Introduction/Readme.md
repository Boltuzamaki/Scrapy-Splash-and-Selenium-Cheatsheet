# Basic components of Scrapy
## All the components of scrapy 
<img src="https://github.com/Boltuzamaki/Scrapy-Splash-and-Selenium-Cheatsheet/blob/master/images/2.png"  width="600" height="400" />

## Spiders
Spider is the component where we define what we want to extract from the webpage and there are different types of Spiders available in scrapy.
<img src="https://github.com/Boltuzamaki/Scrapy-Splash-and-Selenium-Cheatsheet/blob/master/images/3.png"  width="600" height="400" />

## Pipelines
Pipeline component is related to data we extract like cleaning , storing the data 

<img src="https://github.com/Boltuzamaki/Scrapy-Splash-and-Selenium-Cheatsheet/blob/master/images/4.png"  width="600" height="400" />

## Middleware 
Middleware component is related to everything we need to do with request we sent and response we get from website 
<img src="https://github.com/Boltuzamaki/Scrapy-Splash-and-Selenium-Cheatsheet/blob/master/images/5.png"  width="600" height="400" />

## Engine and Schedular

Engines are responsible for co-ordinating between all the components and Schedular helps to preserve the order of operations 

## What to scrap and what not is controlled by robots.txt 
<img src="https://github.com/Boltuzamaki/Scrapy-Splash-and-Selenium-Cheatsheet/blob/master/images/1.png"  width="600" height="400" />


# Install Scrapy 
```
conda install -c conda-forge scrapy
```
and dependencies 

```
pip install protego
```