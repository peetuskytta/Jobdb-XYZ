##
#	Contains useful functions for the project.
#
#	Aleksi, you can add new functions here.
#	When you need the function use the import utility
#	in the file you want to use the function.
##

from classes import Job
from bs4 import BeautifulSoup


def save_job(data, url):
    # the text.strip will remove any leading or trailing whitespaces
    job_title = data.find('h3', class_='job-box__title').text.strip()
    a_ref = data.find('a')
    job_id = a_ref.get('data-id')
    job_link = url + a_ref.get('href')
    new_job = Job(job_title, job_id, job_link)
    return new_job
