import requests
from utility_functions import *
from bs4 import BeautifulSoup
from url_gen import url_gen
#import sys

def duunitori_crawler():
    base_url = 'https://duunitori.fi'
    search_url = 'https://duunitori.fi/tyopaikat?filter_work_type=full_time&haku='
    url_done = url_gen("files/duunitori", search_url)
    index = 2
    page_found = True
    page_number = 1
    duunitori_jobs = []

    while page_found:
        if page_number == 1:
            response = requests.get(url_done)
            if response.status_code == 503:
                raise ConnectionError("Under maintenance")
        else:
            url = url_done + "&sivu=" + str(index)
            response = requests.get(url)
            index += 1
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            job_grid = soup.find_all('div', class_='grid grid--middle job-box job-box--lg')
            for div in job_grid:
                job = save_job(div, base_url, "duuni")
                if job:
                    categorize_job("files/languages", job, "duuni")
                    duunitori_jobs.append(job)
        else:
            if response.status_code == 503:
                raise ConnectionError("Under maintenance")
            if response.status_code == 404:
                page_found = False

        # Should be commented out in production as there's no GUI in VM.
        #sys.stdout.flush()
        #sys.stdout.write("\rNumber of pages processed: %d" % page_number)

        response = None
        page_number += 1

    # Should be commented out in production as there's no GUI in VM
    #print("\nDuunitori: total pages processed: ", page_number)
    database_inserts(duunitori_jobs)


### Crawler to find the job postings in Jobly.fi website. ###
def jobly_crawler():
    baseurl = "https://www.jobly.fi/tyopaikat?search="
    pageIndex = 0
    jobly_jobs = []

    with open("files/jobly", "r") as file:
        searchTerms = file.read().split('\n')
    for word in searchTerms:
        try:
            searchurl = baseurl + word + "&page=" + str(pageIndex)
            response = requests.get(searchurl)
            if response.status_code == 200:
                html = response.content
                soup = BeautifulSoup(html, 'html.parser')
                job_grid = soup.find_all('a', class_='recruiter-job-link')
                for div in job_grid:
                    job = save_job(div, None, "jobly")
                    if job:
                        categorize_job("files/languages", job, "jobly")
                        jobly_jobs.append(job)
        except:
            raise ConnectionError()
        finally:
            None
            #print(f"jobly: ({word}) done!")
    database_inserts(jobly_jobs)