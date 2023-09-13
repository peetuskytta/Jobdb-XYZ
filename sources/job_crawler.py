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
job_list = [] # creates an empty list

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
            #print(div.find_all('div'))
            new_job = save_job(div, base_url)
            job_list.append(new_job)
    else:
        if response.status_code == 404:
            #print(f"Page {page_number}: not found")
            page_found = False
    sys.stdout.flush()
    sys.stdout.write("\rNumber of pages processed: %d" % page_number)
    response = None
    page_number += 1

# Connect to a database usig SQLite and add the list of jobs to database table
print("\nTotal pages processed: ", page_number)
db_actions(job_list)
#for Job in job_list:
#	print(Job)
## we can print job_list here or use redirection in shell when running the
## script to redirect the output to a file.
