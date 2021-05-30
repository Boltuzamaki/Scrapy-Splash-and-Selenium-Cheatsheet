### Installing selenium

```
pip install selenium
```

Now install webdriver for chrome from
[here](https://selenium-python.readthedocs.io/installation.html)

- Now put the driver same in the projecct folder

## Install scrapy-selenium
```
pip install scrapy-selenium
```

- Now create a new scrapy project and add the following to settings.py
  
```
from shutil import which

SELENIUM_DRIVER_NAME = 'chrone'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # '--headless' if using chrome 
```

```
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
```