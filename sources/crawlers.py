
import requests
from utility_functions import *
from bs4 import BeautifulSoup
from classes import Job
from url_gen import url_gen
import sys

def duunitori_crawler():
    base_url = 'https://duunitori.fi'
    search_url = 'https://duunitori.fi/tyopaikat?filter_work_type=full_time&haku='
    url = url_gen("../files/titles", search_url)
    index = 2
    page_found = True
    page_number = 1
    job_list = []

    while page_found:
        if page_number == 1:
            response = requests.get(url)
            if response.status_code == 503:
                raise ConnectionError("Under maintenance")
        else:
            url = url + "&sivu=" + str(index)
            response = requests.get(url)
            index += 1
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            job_grid = soup.find_all('div', class_='grid grid--middle job-box job-box--lg')
            for div in job_grid:
                job = save_job(div, base_url)
                if job:
                    categorize_job("../files/languages", job)
                    if job.category != "empty" and job.description != None:
                        job_list.append(job)
        else:
            if response.status_code == 503:
                raise ConnectionError("Under maintenance")
            if response.status_code == 404:
                page_found = False

        # Should be commented out in production as there's no GUI in VM.
        sys.stdout.flush()
        sys.stdout.write("\rNumber of pages processed: %d" % page_number)

        response = None
        page_number += 1

    # Should be commented out in production as there's no GUI in VM
    print("\nTotal pages processed: ", page_number)
    database_inserts(job_list)