##
#	Project name: Crawler
#	Description: a crawler/scraper to search specific job titles from Duunitori.fi
#	Authors: Asukava & Pskytta, Hive Helsinki students
##

import requests
from utility_functions import *
from bs4 import BeautifulSoup
from classes import Job
from url_gen import url_gen
import sys

index = 2
base_url = 'https://duunitori.fi'
seach_url = url_gen("files/titles")
page_found = True
page_number = 1
job_list = []

target = "Duunitori suosittelee"

while page_found:
    if page_number == 1:
        response = requests.get(seach_url)
    else:
        url = seach_url + "&sivu=" + str(index)
        response = requests.get(url)
        index += 1
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        job_grid = soup.find_all('div', class_='grid grid--middle job-box job-box--lg')
        for div in job_grid:
            new_job = save_job(div, base_url)
            categorize_job("files/languages", new_job)
            if new_job.category != "empty" and new_job.description != None:
                job_list.append(new_job)
    else:
        if response.status_code == 404:
            page_found = False
    sys.stdout.flush()
    sys.stdout.write("\rNumber of pages processed: %d" % page_number)
    response = None
    page_number += 1

print("\nTotal pages processed: ", page_number)
database_inserts(job_list)
