from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import csv
import re

# read in all the urls from the csv file
urls = []
with open('urls.csv', 'r') as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip('\n'), lines))
    for line in lines:
        urls.append(line)

# loop through each url and scrape
for url in urls[29]:
    # do not render images
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # go on the specified url of the for loop
    driver.get(url)

    # try to click on the load more button after scrolling all the way down continously until you cannot
    try:
        btn = driver.find_element_by_xpath('//a[@class="no-underline  show-more-reviews"]')
        ActionChains(driver).move_to_element(btn).perform()
    except Exception as e:
        print('Click Error: ', e)
    
    # names found by following this path
    names = driver.find_elements_by_xpath('//div[@class="epsilon  weight-bold  inline-block"]').text

    for name in names:
        print(name)
    
    # make a dictionary that will eventually be outputted
    reviews_dict = {}

    # csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
    # writer = csv.writer(csv_file)

    # writer.writerow(['title', 'text', 'username', 'date_published', 'rating'])

    # wait_button = WebDriverWait(driver, 5)
    # next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="product-114949"]/div/div[2]/div/div[1]/div/div/a[1]')))

    driver.quit()