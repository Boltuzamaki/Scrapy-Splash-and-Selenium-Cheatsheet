from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chrome_option = Options()
chrome_option.add_argument("--headless")

chrome_path = which("chromedriver.exe")
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_option)
#driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://duckduckgo.com")

search_form = driver.find_element_by_xpath('//input[@id="search_form_input_homepage"]')
search_form.send_keys("My user agent")


#search_btn = driver.find_element_by_xpath('//input[@id="search_button_homepage"]')
#search_btn.click()

search_form.send_keys(Keys.ENTER)
driver.close()