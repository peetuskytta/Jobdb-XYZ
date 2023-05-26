import requests
from bs4 import BeautifulSoup


##'https://duunitori.fi/tyopaikat?filter_work_type=full_time&haku=system%20specialist%3Bdeveloper%3BLinux-kehitt%C3%A4j%C3%A4%3Bohjelmoija'


def url_gen():
    base = 'https://duunitori.fi/tyopaikat?filter_work_type=full_time&haku='
    file = open("job_titles", "r")
##  print(file.readlines())
##  file.seek(0)
##  print(file.read())
##  file.seek(0)
    string = "".join(file)
    for symbol in "ö":
        string = string.replace(symbol, "%C3%B6")
    for symbol in "ä":
        string = string.replace(symbol, "%C3%A4")
    for symbol in " ":
        string = string.replace(symbol, "%20")
    for symbol in "\n":
        string = string.replace(symbol, "%3B")
    ret = base + string[:-3]
    return ret
