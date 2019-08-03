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
writer = csv.DictWriter(csv_file, 
                        fieldnames = ['title', 'name', 'position', 'industry', 'usage', 'paid_status', 'source', 'date','total', 'ease', 'feature', 'support', 'value', 'recommend', 'comments', 'pros',
                            'cons', 'overall', 'recommendations to other buyers'])

writer.writeheader()

# function to differentiate the different review parts and mutate the review dict being passed
def check_element(dict, driver):
    try:
        key = re.search('.+?(?=:)', driver.find_element_by_xpath('./b').text).group(0).lower()
        dict[key] = driver.text
    except:
        pass
    try:
        key = re.search('.+?(?=:)', driver.find_element_by_xpath('./strong').text).group(0).lower()
        dict[key] = driver.text
    except:
        pass


# loop through each url and scrape,
for url in urls[0:1]:
    # do not render images
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    chromeOptions.add_experimental_option("prefs", prefs) 
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # go on the specified url of the for loop
    driver.get(url)
    # csv_file = open('reviews.csv', 'w', encoding='utf-8', newline='')
    # writer = csv.writer(csv_file)

    # writer.writerow(['title', 'text', 'username', 'date_published', 'rating'])

    # try to click on the load more button after scrolling all the way down continously until you cannot
    # while True:
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #     try:
    #         # wait_button = WebDriverWait(driver, 10)
    #         # btn = wait_button.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="no-underline  show-more-reviews"]')))
    #         # btn.click()
    #         sleep(1.5)
    #         btn = driver.find_element_by_xpath('//a[@class="no-underline  show-more-reviews"]')
    #         btn.click()
    #     except Exception as e:
    #         print('Click Error: ', e)
    #         break
    
    reviews = driver.find_elements_by_xpath('//div[@class="cell-review"]')
    for review in reviews[0:2]:
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

        total = review.find_element_by_xpath('.//span[@class="overall-rating"]/span').text
        # # these next four are annoying because some people do not do them and the class tags are same
        # # jk, i just didn't look hard enough for the path whoohooo
        ease = review.find_element_by_xpath('.//span[@class="reviews-stars  rating-ease-of-use"]/span[@class="milli  rating-decimal"]/span[1]').text
        feature = review.find_element_by_xpath('.//span[@class="reviews-stars  rating-features"]/span[@class="milli  rating-decimal"]/span[1]').text
        try:
            support = review.find_element_by_xpath('.//span[@class="reviews-stars  rating-customer-service"]/span[@class="milli  rating-decimal"]/span[1]').text
        except:
            pass
        value = review.find_element_by_xpath('.//div[@class="cell  three-twelfths  reviews-col columns4 lap-three-twelfths  palm-one-half"]/span[@class="reviews-stars  rating-value"]/span[@class="milli  rating-decimal"]/span[1]').text
        recommend = review.find_element_by_xpath('.//img[@class="gauge-svg-image"]').get_attribute('alt')

        # make a dictionary that will eventually be outputted
        review_dict = {}

        review_dict['title'] = title
        review_dict['name'] = name
        review_dict['position'] = position
        review_dict['industry'] = industry
        review_dict['usage'] = usage
        review_dict['paid_status'] = paid_status
        review_dict['source'] = source
        review_dict['date'] = date
        review_dict['total'] = total
        review_dict['ease'] = ease
        review_dict['feature'] = feature
        review_dict['support'] = support
        review_dict['value'] = value
        review_dict['recommend'] = recommend

        # the reviews themselves
        review_elements = review.find_elements_by_xpath('.//div[@class="review-comments  color-text"]/p')
        # for loop to iterate through the p tags and put them in correct element
        for element in review_elements:
            # element_category = element.find_element_by_xpath('./b').text
            check_element(review_dict, element)
            # use regex to check the bold, then based off that key, input in the text to the value

        writer.writerow(review_dict)

    driver.quit()