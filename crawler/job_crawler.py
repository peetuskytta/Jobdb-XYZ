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
duunitori_crawler()
jobly_crawler()
#hub_crawler()
#academicwork_crawler()
identify_lvl()
logging.info('Crawling DONE\n---------------------------------------------------')
clean_database() # cleans the "not wanted" items from the database
cleanOldFromDatabase() # clean the old links from the database
#
