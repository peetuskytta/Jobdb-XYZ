import requests
from bs4 import BeautifulSoup

file = open("testfile.txt", "r")
print(file.readlines())
print()
file.seek(0)
print(file.read())
