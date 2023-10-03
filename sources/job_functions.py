import requests
from job import Job
from bs4 import BeautifulSoup

def categorize_job(filename: str, job: Job):
    response = requests.get(job.url)
    if response.status_code == 200:
        with open(filename, "r") as file:
            terms = file.read().split()
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        description = soup.find('div', class_='gtm-apply-clicks description description--jobentry')
        # The following check eliminates the possible Demo page which would cause an error
        # as description would return None.
        if description:
            result = []
            div_text = description.get_text()
            job.description = div_text
            for word in terms:
                if word.lower() in div_text.lower():
                    if word not in result:
                        result.append(word.lower())
            for item in result:
                job.category += item + " "

def save_job(data, url):
    date = data.find('span', class_='job-box__job-posted').text
    if date[-1] == "." or date[-1] == "3":
        pass
    else:
        return None
    job_title = data.h3.text
    job_id = data.a['data-id']
    job_link = url + data.a['href']
    job_description = None
    job_category = ""
    job_level = ""
    new_job = Job(job_title,
        job_id,
        job_link,
        job_description,
        job_category,
        job_level)
    return new_job