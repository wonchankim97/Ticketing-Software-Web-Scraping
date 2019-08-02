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

csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

writer.writerow(['title', 'name', 'position', 'industry', 'usage', 'paid_status', 'source', 'date',
                'overall', 'ease', 'feature', 'support', 'value', 'recommend', 'comment', 'pros',
                'cons'])

# loop through each url and scrape,
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
            wait_button = WebDriverWait(driver, 10)
            btn = wait_button.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="no-underline  show-more-reviews"]')))
            btn.click()
            # sleep(1.5)
            # btn = driver.find_element_by_xpath('//a[@class="no-underline  show-more-reviews"]')
            # btn.click()
        except Exception as e:
            print('Click Error: ', e)
            break
    
    reviews = driver.find_elements_by_xpath('//div[@class="cell-review"]')
    for review in reviews:
        # categories found by following paths
        title = review.find_element_by_xpath('.//h3[@class="delta  weight-bold  half-margin-bottom"]/q').text
        name = review.find_element_by_xpath('.//div[@class="epsilon  weight-bold  inline-block"]').text
        position = review.find_element_by_xpath('.//div[@class="opacity-threequarters"]').text
        industry = review.find_element_by_xpath('.//div[@class="italic  opacity-threequarters"]').text
        usage = review.find_element_by_xpath('.//div[@class="reviewer-details"]/div[5]').text
        paid_status = review.find_element_by_xpath('.//span[@class="help-tooltip text-left incentive"]').get_attribute('data-incentive-code')
            #.get_attribute('data-incentive-code') when looping through
        source = review.find_element_by_xpath('.//div[@class="reviewer-details"]/div[7]').text
        date = review.find_element_by_xpath('.//div[@class="quarter-margin-bottom  micro  color-gray  weight-normal  text-right  palm-text-left"]').text

        overall = review.find_element_by_xpath('.//span[@class="overall-rating"]/span').text
        # these next four are annoying because some people do not do them and the class tags are same
        # jk, i just didn't look hard enough for the path whoohooo
        ease = review.find_element_by_xpath('.//span[@class="reviews-stars  rating-ease-of-use"]/span[@class="milli  rating-decimal"]/span[1]').text
        feature = review.find_element_by_xpath('.//span[@class="reviews-stars  rating-features"]/span[@class="milli  rating-decimal"]/span[1]').text
        support = review.find_element_by_xpath('.//span[@class="reviews-stars  rating-customer-service"]/span[@class="milli  rating-decimal"]/span[1]').text
        value = review.find_element_by_xpath('.//div[@class="cell  three-twelfths  reviews-col columns4 lap-three-twelfths  palm-one-half"]/span[@class="reviews-stars  rating-value"]/span[@class="milli  rating-decimal"]/span[1]').text
        recommendation = review.find_element_by_xpath('.//img[@class="gauge-svg-image"]').get_attribute('alt')
    
    # the reviews themselves
    # for loop to iterate through the p tags and put them in correct element
    test = driver.find_element_by_xpath('//div[@class="review-comments  color-text"]/p[1]')
    re.search('//b'.text, 'Comments: ?')
    if test.find_element_by_xpath('./b') == 'Comments:' or test.find_element_by_xpath('./b') == 'Comments: ':
        # use regex for the conditional above instead
        comment = test.text
    # comments = driver.find_elements_by_xpath('div[@class="review-comments  color-text"]/p[1]')
    # pros = driver.find_elements_by_xpath('div[@class="review-comments  color-text"]/p[2]')
    # cons = driver.find_elements_by_xpath('div[@class="review-comments  color-text"]/p[3]')


    # make a dictionary that will eventually be outputted
    # reviews_dict = {}

    # review_dict['title'] = title
    # review_dict['name'] = name
    # review_dict['position'] = position
    # review_dict['industry'] = industry
    # review_dict['usage'] = usage
    # review_dict['paid_status'] = paid_status
    # review_dict['source'] = source
    # review_dict['date'] = date
    # review_dict['overall'] = overall
    # review_dict['ease'] = ease
    # review_dict['feature'] = feature
    # review_dict['support'] = support
    # review_dict['value'] = value
    # review_dict['recommend'] = recommend
    # review_dict['comment'] = comment
    # review_dict['pros'] = pros
    # review_dict['cons'] = cons

    # writer.writerow(review_dict.values())

    # csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
    # writer = csv.writer(csv_file)

    # writer.writerow(['title', 'text', 'username', 'date_published', 'rating'])

    # wait_button = WebDriverWait(driver, 5)
    # next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="product-114949"]/div/div[2]/div/div[1]/div/div/a[1]')))

    driver.quit()