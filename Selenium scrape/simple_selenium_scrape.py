from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

# For spoofing the request 
opts = Options()
opts.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

driver = webdriver.Chrome(chrome_options=opts)

# Initializing the Driver
chrome_path = r"C:\Users\chand\Desktop\adverto\Scrape\gov\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get("https://myanimelist.net/")

# Click interation of login
login_button = driver.find_element_by_xpath('//a[@id="malLogin"]')
login_button.click()

login_username = driver.find_element_by_xpath('//input[@id="loginUserName"]')
login_username.send_keys("xxxxxxxx")

password = driver.find_element_by_xpath('//input[@id="login-password"]')
password.send_keys("xxxxxxxx")


button = driver.find_element_by_xpath('//input[@value="Login"]')
button.click()

input_query = driver.find_element_by_xpath('//input[@value="Login"]')
input_query.click()


# Taking care of hard coded wait time by try except

while True:
    try:
        time.sleep(2)
        myElem = driver.find_element_by_xpath('//input[@id="topSearchText"]')
        myElem.send_keys("top anime")
        # For drop down selectors 
        # sel = Select(driver.find_element_by_xpath("//select[@id='topSearchValue']"))
        # sel.select_by_visible_text("Manga")
        break 
    except:
        continue

button_submit = driver.find_element_by_xpath('//input[@id="topSearchButon"]')
button_submit.click()

time.sleep(3)

get_divs = driver.find_elements_by_xpath('//article/div[@class="list di-t w100"]')

# Get the elements 
for g in get_divs:
    print(g.text)