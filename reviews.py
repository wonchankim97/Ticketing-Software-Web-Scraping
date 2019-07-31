from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
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
for url in urls[23:24]:
    # do not render images
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    chromeOptions.add_experimental_option("prefs", prefs) 
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # go on the specified url of the for loop
    driver.get(url)

    # try to click on the load more button after scrolling all the way down continously until you cannot
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        try:
            sleep(1.5)
            btn = driver.find_element_by_xpath('//a[@class="no-underline  show-more-reviews"]')
            btn.click()
            # ActionChains(driver).move_to_element(btn).click(btn).perform()
        except Exception as e:
            print('Click Error: ', e)
            break
    
    # categories found by following paths
    titles = driver.find_elements_by_xpath('//h3[@class="delta  weight-bold  half-margin-bottom"]/q')
    names = driver.find_elements_by_xpath('//div[@class="epsilon  weight-bold  inline-block"]')
    positions = driver.find_elements_by_xpath('//div[@class="opacity-threequarters"]')
    industries = driver.find_elements_by_xpath('//div[@class="italic  opacity-threequarters"]')
    usages = driver.find_elements_by_xpath('//div[@class="reviewer-details"]/div[5]')
    paid_statuses = driver.find_elements_by_xpath('//span[@class="help-tooltip text-left incentive"]')
        #.get_attribute('data-incentive-code') when looping through
    sources = driver.find_elements_by_xpath('//div[@class="reviewer-details"]/div[7]')

    # overalls = driver.find_elements_by_xpath('//span[@class="overall-rating"]/span')



    for source in sources:
        print(source.text)
    print(len(names))
    
    # make a dictionary that will eventually be outputted
    reviews_dict = {}

    # csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
    # writer = csv.writer(csv_file)

    # writer.writerow(['title', 'text', 'username', 'date_published', 'rating'])

    # wait_button = WebDriverWait(driver, 5)
    # next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="product-114949"]/div/div[2]/div/div[1]/div/div/a[1]')))

    driver.quit()