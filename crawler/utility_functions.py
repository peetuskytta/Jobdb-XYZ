import sqlite3 as db
from classes import Job
from bs4 import BeautifulSoup
import requests
import json

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
    new_job = Job(job_title, job_id, job_link, job_description, job_category, job_level)
    return new_job

def database_inserts(jobs_list: list):
    if testAndActConnection("database/jobs.db", jobs_list) == True:
        #later collect this to a log and redirect err messages to errlog in the Oracle Linux
        pass
    else:
        job_dicts = [job.__dict__ for job in jobs_list]
        with open("database/job_list.json", 'w') as file:
            json.dump(job_dicts, file, indent=2)
        return

def testAndActConnection(db_name: str, jobs_list: list):
    sqlConnection = None
    try:
        sqlConnection = db.connect(db_name)
        print("Connection to database was successful. Initiating the data insertion...")
        cursor = sqlConnection.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                nro INTEGER PRIMARY KEY,
                id INTEGER,
                title TEXT,
                link TEXT,
                description TEXT,
                category TEXT,
                level TEXT
            )
        """)
        cursor.execute("SELECT id FROM jobs")
        rows = cursor.fetchall()  # fetches all the id rows to be checked for existing ones
        compareIds = [row[0] for row in rows]

        for job in jobs_list:
            if job.id in compareIds:
                continue
            else:
                query = "INSERT INTO jobs (id, title, link, description, category, level) VALUES (?, ?, ?, ?, ?, ?)"
                values = (job.id, job.title, job.url, job.description, job.category, job.level)
                cursor.execute(query, values)
                compareIds.append(job.id)
                sqlConnection.commit()

        sqlConnection.commit()

    except db.Error as error:
        print("Error while connecting to SQLite database: ", error)
        return False

    finally:
        if sqlConnection:
            # close the connection to the database
            sqlConnection.close()
            print("Closing successful.")
            return True
        else:
            return False
