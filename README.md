# Ticketing Software Web Scraping

There are many different types of ticketing software that have sprung up in the past decade. However, with this project, after coming across the website capterra.com, I wanted to focus on ticketing softwares that dealt with merchants who had to find a platform in order to sell tickets to their events.
These merchants pay the ticketing software company varying fees, such as a percentage of a ticket or a fixed deduction from each ticket sale. However, although these metrics can be used to try to deduce how a company should structure their business flow, I was more interested in the customer (merchants) reviews for each of the softwares.

My blog covers more about this project: [Scraping Ticketing Software Reviews](https://nycdatascience.com/blog/student-works/ticketing-software-reviews/)


## Scraping

In order to scrape the review websites of the ticketing software companies, I used Selenium as my driver. Initially, I was going to use a combination of the package Scrapy as well as Selenium but could not due to the dynamic loading of the review pages.
After going to the main site that showed a compilation of all the ticketing software companies, I first made the driver sort the page according to the most reviews. I then had to grab the URLs of each of the companies' review links and stored these links into a csv file. This first step was done in the urls.py file. One complication of this project was that Capterra did some A/B testing so I had to omit the companies that had a new website layout as well as those without 5 or more reviews.
Subsequently, I used the urls in the csv file in a new script called reviews.py and made a loop to make sure that the Selenium driver would visit each company's review page. From there, I located all the elements I wanted to scrape within each review cell such as the title, name, date, and much more. I then looped this for all of the review cells and managed to compile them all into a dictionary that finally outputted each of the values into a csv file, review_.csv.

## Data Cleaning

For data cleaning, I used a .ipynb file so that I could run the commands while testing the EDA and NLP side of my analysis. I used the pandas library to import the csv files into a dataframe and manipulated the column values with improperly formatted strings.

## Exploratory Data Analysis

I took a look into the various categories I could filter the companies by, including overall rating and paid status.

## Natural Language Processing

Using natural language processing, I wanted to analyze the sentiment of the reviews from the dataframe. What is interesting about this segment was that the reviews were split into various parts such as "Pros" and "Cons".

## Further Improvements

I would like to go deeper into the NLP side of this project. Once I have a better understanding of deep learning, I wish to utilize other more powerful engines of NLP to provide deeper insights into my data. Also, if there are any other sites that display reviews such as Capterra for ticketing companies, there could be other scripts implemented to scrape them in order to see different perspectives of various companies in this industry.
