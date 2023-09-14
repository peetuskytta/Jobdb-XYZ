##
#	Contains useful functions for the project.
##

import sqlite3 as db
from classes import Job
from bs4 import BeautifulSoup
import requests

def save_job(data, url):
    job_title = data.h3.text
    job_id = data.a['data-id']
    job_link = url + data.a['href']
    job_description = None
    job_category = ""
    date = data.find('span', class_='job-box__job-posted').text
    if date[-1] == "." or date[-1] == "3":
        print(date)
    else:
        print(f" Wrong: {date}")
    new_job = Job(job_title, job_id, job_link, job_description, job_category)
    return new_job

def database_inserts(jobs_list: list):
    if testAndActConnection("database/jobs.db", jobs_list) == True:
        #later collect this to a log and redirect err messages to errlog in the Oracle Linux
        pass
    else:
        return

def testAndActConnection(db_name: str, jobs_list: list):
    try:
        print("Connection to database was successful. Initiating the data insertion...")
        sqlConnection = db.connect(db_name)
        cursor = sqlConnection.cursor()
        # The table users will store the email and user_id. Later we can relate user_id with multiple
        # job_ids to identify what the user has received already
        #cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, email VARCHAR(255))")
        cursor.execute("CREATE TABLE IF NOT EXISTS jobs (nro INT PRIMARY KEY, id INT, title TEXT, link TEXT, description TEXT, category TEXT)")

        cursor.execute("SELECT id FROM jobs")
        rows = cursor.fetchall()  # fetches all the id rows to be checked for existing ones
        compareIds = [row[0] for row in rows]

        for job in jobs_list:
            if job.id in compareIds:
                continue
            query = "INSERT INTO jobs (id, title, link, description, category) VALUES (?, ?, ?, ?, ?)"
            values = (job.id, job.title, job.url, job.description, job.category)
            cursor.execute(query, values)
            compareIds.append(job.id)
        sqlConnection.commit()  # saves the data

    except db.Error as error:
        print("Error while connecting to SQLite database", error)
        return False

    finally:
        if sqlConnection:
            # close the connection to the database
            sqlConnection.close()
            print("Closing successful.")
            return True
        else:
            return False

def categorize_job(filename: str, job: Job):
    response = requests.get(job.url)
    if response.status_code == 200:
        with open(filename, "r") as file:
            terms = file.read().split()
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        description = soup.find('div', class_='gtm-apply-clicks description description--jobentry')
        # The following check eliminates the possible Demo page which would cause an error
        # as description would return None.
        if description:
            result = []
            div_text = description.get_text()
            job.description = div_text
            for word in terms:
                if word.lower() in div_text.lower():
                    if word not in result:
                        result.append(word)
            for item in result:
                job.category += item + " "
