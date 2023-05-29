##
#	Project name: Crawler
#	Description: a crawler/scraper to search specific job titles from Duunitori.fi
#	Authors: Asukava & Pskytta, Hive Helsinki Alumni
##

import requests
from bs4 import BeautifulSoup
from utility_functions import save_job
from classes import Job
from url_gen import url_gen

index = 2
base_url = 'https://duunitori.fi'
seach_url = url_gen("titles")
page_found = True
page_number = 1
job_list = [] # creates an empty list

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
            job_list.append(new_job)
    else:
        if response.status_code == 404:
            print(f"Page {page_number}: not found")
            page_found = False
    response = None
    page_number += 1

## we can print job_list here or use redirection in shell when running the
## script to redirect the output to a file.
