import sqlite3 as db
from bs4 import BeautifulSoup
import requests
import logging
#from fuzzywuzzy import fuzz # Used for text similarity comparisons

# TEST THIS LINK FOR EXAMPLE:
# https://duunitori.fi/tyopaikat/tyo/senior-java-developer-relocation-to-switzerland-scsom-14504783

logging.basicConfig(filename='report.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

### This function will load delete_pattern file content from files folder to search_patterns
### variable (list) which is used to delete specific patterns not wanted in the database.
def clean_database():
    sqlConnection = None
    try:
        sqlConnection = db.connect("../database/jobs.db")
        cursor = sqlConnection.cursor()

        # open and split content of the file
        with open("files/delete_pattern", 'r') as file:
            search_patterns = file.read().splitlines()

        rowsAffected = 0
        # loop the patterns and execute sql DELETE
        for pattern in search_patterns:
            sql = f"DELETE FROM jobs WHERE title LIKE '{pattern}'"
            cursor.execute(sql)
            rowsAffected += cursor.rowcount
            sqlConnection.commit()

        sqlConnection.commit()
        cursor.close()

    except db.Error as error:
        logging.error('Error: ', error)
        return

    finally:
        if sqlConnection:
            logging.info('Total rows deleted: %s', rowsAffected)
            sqlConnection.close()
        return

#https://youtu.be/ooOELrGMn14?t=10
### Make a cleaner for duplicates compare titles and if they match compare descriptions and if 90% match remove. Use diff?

def shouldDeleteRow(link):
    #checks
    response =  requests.get(link)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        if "jobly" in link:
            if "Tämä työpaikkailmoitus ei ole enää voimassa" in soup.text:
                return True
        elif "duunitori" in link:
            if "Pahoittelut, haku tähän avoimeen" in soup.text:
                return True
    return False

def deleteRowsWithEmptyCategory(cursor):
    cursor.execute("SELECT id FROM jobs WHERE category IS NULL OR category = ''")
    logging.info('Deleting empty category rows')
    rows = cursor.fetchall()
    rowsAffected = 0
    for row in rows:
        row_id = row[0]
        cursor.execute("DELETE FROM jobs WHERE id=?", (row_id,))
        rowsAffected += cursor.rowcount
    return rowsAffected

def cleanOldFromDatabase():
    sqlConnection = None
    logging.info('Deleting old job postings')
    try:
        sqlConnection = db.connect("../database/jobs.db")
        cursor = sqlConnection.cursor()
        rowsAffected = deleteRowsWithEmptyCategory(cursor)
        cursor.execute(f"SELECT id, link FROM jobs")
        rows = cursor.fetchall()

        for row in rows:
            if shouldDeleteRow(row[1]):
                row_id = row[0]
                cursor.execute(f"DELETE FROM jobs WHERE id=?", (row_id,))
                rowsAffected += cursor.rowcount
                sqlConnection.commit()

        sqlConnection.commit()
        cursor.close()

    except db.Error as error:
        logging.error('Error: %s', error)
        return

    finally:
        if sqlConnection:
            logging.info('Total links deleted: %s', rowsAffected)
            sqlConnection.close()
        return


# if you want to run these separately remove the comments on the next lines and run the script with command: 'python3 clean_database.py'
#clean_database()
#cleanOldFromDatabase()
