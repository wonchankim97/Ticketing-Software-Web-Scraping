from selenium import webdriver
# from selenium.webdriver.common.by import By
import re
import csv

chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

# driver = webdriver.Chrome()

driver.get("https://www.capterra.com/ticketing-software/")

sort_button = driver.find_element_by_xpath('//*[@id="sort_options_select"]/option[3]')#.get_attribute()
sort_button.click()

csv_file = open('urls.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# writer.writerow(['title', 'text', 'username', 'date_published', 'rating'])

# wait_button = WebDriverWait(driver, 5)
# next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="product-114949"]/div/div[2]/div/div[1]/div/div/a[1]')))

companies = driver.find_elements_by_xpath('//div[@class="card  listing"]')
for company in companies:
    name = company.find_element_by_xpath('.//h2[@class="listing-name"]/a').text
    number = company.find_element_by_xpath('.//*/a[@class="reviews-count milli"]').text
    number = re.search('\d+', number).group(0)
    if((name != 'Eventzilla') & (name != 'TicketSpice') & (number != '0')):
        links = company.find_element_by_xpath('.//*/a[@class="reviews-count milli"]').get_attribute('href')
        writer.writerow([links])

driver.quit()