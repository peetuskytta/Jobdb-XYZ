import sqlite3 as db
from bs4 import BeautifulSoup
import requests


linksToTest = {} # Collect ID and link
toDelete = [] # Store the ID to be removed from Database

