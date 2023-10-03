##
#       Project name: Crawler
#       Description: a crawler/scraper to search specific job titles from Duunitori.fi
#       Authors: Asukava & Pskytta, Hive Helsinki students
##

import requests, sys
from database_actions import database_inserts
from job_functions import *
from bs4 import BeautifulSoup
from url_gen import url_gen

index = 2
base_url = 'https://duunitori.fi'
seach_url = url_gen("files/titles")
page_found = True
page_number = 1
job_list = []

#target = "Duunitori suosittelee"

while page_found:
    if page_number == 1:
        response = requests.get(seach_url)
        if response.status_code == 503:
            raise ConnectionError("Under maintenance")
    else:
        url = seach_url + "&sivu=" + str(index)
        response = requests.get(url)
        index += 1
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        job_grid = soup.find_all('div', class_='grid grid--middle job-box job-box--lg')
        for div in job_grid:
            job = save_job(div, base_url)
            if job:
                categorize_job("files/languages", job)
                if job.category != "empty" and job.description != None:
                    job_list.append(job)
    else:
        if response.status_code == 503:
            raise ConnectionError("Under maintenance")
        if response.status_code == 404:
            page_found = False
    sys.stdout.flush()
    sys.stdout.write("\rNumber of pages processed: %d" % page_number)
    response = None
    page_number += 1

print("\nTotal pages processed: ", page_number - 1)
database_inserts(job_list)