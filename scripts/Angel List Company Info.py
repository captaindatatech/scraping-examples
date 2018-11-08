from urllib import request
from datetime import datetime
from bs4 import BeautifulSoup
import csv


# add the correct User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# the company page you're about to scrape
company_page = 'https://angel.co/uber'

# open the page
page_request = request.Request(company_page, headers=headers)
page = request.urlopen(page_request)

# parse the html using beautiful soup
html_content = BeautifulSoup(page, 'html.parser')

# we parse the title
title = html_content.find('h1')
title = title.text.strip()
print(title)

# we parse the description
description = html_content.find('h2', attrs={'class': 'js-startup_high_concept'})
description = description.text.strip()
print(description)

# we extract the website
website = html_content.find('a', attrs={'class': 'company_url'})
website = website['href'].strip()
print(website)

# open a csv with the append (a) parameter. We also save the date which is always a good indicator.
with open('angel.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([title, description, website, datetime.now()])

