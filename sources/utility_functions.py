##
#	Contains useful functions for the project.
##

import sqlite3 as db
from classes import Job
from bs4 import BeautifulSoup

def save_job(data, url):
    # OLD WAY
    	#job_title = data.find('h3', class_='job-box__title').text.strip()
    	#a_ref = data.find('a')
    	#job_id = a_ref.get('data-id')
    	#job_link = url + a_ref.get('href')
    #
    # NEW WAY
    job_title = data.h3.text
    job_id = data.a['data-id']
    job_link = url + data.a['href']
    new_job = Job(job_title, job_id, job_link)
    return new_job

def db_actions(jobs_list):
    if testAndActConnection("database/jobs.db", jobs_list) == True:
        print("Closing successful. Done.")
    else:
        return

def testAndActConnection(db_name, jobs_list):
    try:
        print("Connection to database was successful. Initiating the data insertion...")
        sqlConnection = db.connect(db_name)
        cursor = sqlConnection.cursor()
        # The table users will store the email and user_id. Later we can relate user_id with multiple
        # job_ids to identify what the user has received already
        #cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, email VARCHAR(255))")
        cursor.execute("CREATE TABLE IF NOT EXISTS jobs (id INT PRIMARY KEY, title TEXT, link TEXT)")

        cursor.execute("SELECT id FROM jobs")
        rows = cursor.fetchall()  # fetches all the job_id rows to be checked for existing ones
        compareIds = [row[0] for row in rows]

        for job in jobs_list:
            if job.id in compareIds:
                continue
            query = "INSERT INTO jobs (id, title, link) VALUES (?, ?, ?)"
            values = (job.id, job.title, job.url)
            cursor.execute(query, values)
            compareIds.append(job.id)
        sqlConnection.commit()  # saves the data

    except db.Error as error:
        print("Error while connecting to SQLite database", error)
        return False

    finally:
        if sqlConnection:
            sqlConnection.close()  # closes the connection to the database
            return True
        else:
            return False
