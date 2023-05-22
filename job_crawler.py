import requests
from bs4 import BeautifulSoup

index = 2
baseurl = 'https://duunitori.fi/tyopaikat?filter_work_type=full_time&haku=system%20specialist%3Bdeveloper%3BLinux-kehitt%C3%A4j%C3%A4%3Bohjelmoija'
page_found = True
page_number = 1

while page_found:
    if page_number == 1:
        response = requests.get(baseurl)
    else:
        url = baseurl + "&sivu=" + str(index)
        response = requests.get(url)
        index += 1

    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        div_job = soup.find_all('h3', class_='job-box__title')
        for h3 in div_job:
            print(h3.text)
    else:
        if response.status_code == 404:
            print(f"Page {page_number}: not found")
            page_found = False

    response = None
    page_number += 1