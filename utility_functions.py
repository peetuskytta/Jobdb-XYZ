##
#	Contains useful functions for the project.
##

import sqlite3 as db
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

def db_actions(jobs_list):
    if testAndActConnection("database/test.db", jobs_list) == True:
        print("Closing successful. Done.")
    else:
        return

def testAndActConnection(db_name, jobs_list):
    try:
        print("Connection to database was succesful. Initiating the data insertion...")
        sqlConnection = db.connect(db_name)
        cursor = sqlConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, job_id INTEGER, title TEXT, link TEXT)")

        for job in jobs_list:
            query = "INSERT INTO jobs (job_id, title, link) VALUES (?, ?, ?)"
            values = (job.id, job.title, job.url)
            cursor.execute(query, values)
        sqlConnection.commit() # saves the data

    except db.Error as error :
        print("Error while connecting to SQLite database", error)
        return False

    finally:
        if sqlConnection:
            sqlConnection.close() # closes the connection to the database
            return True
        else:
            return False
