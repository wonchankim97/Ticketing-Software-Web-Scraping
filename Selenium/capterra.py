from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver = webdriver.Chrome()

driver.get("https://www.capterra.com/ticketing-software/?utf8=%E2%9C%93&users%5B6%5D=64&commit=Apply+Filters&sort_options=Most+Reviews")


driver.quit()