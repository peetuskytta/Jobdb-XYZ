##
#       Project name: Crawler
#       Description: a crawler/scraper to search specific job titles from duunitori.fi and jobly.fi
#       Authors: Asukava & Pskytta, Hive Helsinki students
##

import logging
from crawlers import duunitori_crawler, jobly_crawler
from clean_database import clean_database, cleanOldFromDatabase
from utility_functions import identify_lvl


logging.basicConfig(filename='report.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Starting to crawl job sites')
duunitori_crawler()
jobly_crawler()
#hub_crawler()
#academicwork_crawler()
identify_lvl()
logging.info('Crawling DONE')
logging.info('Starting to clean the database')
clean_database() # cleans the "not wanted" items from the database
cleanOldFromDatabase() # clean the old links from the database
logging.info('Cleaning DONE\n---------------------------------------------------')
#
