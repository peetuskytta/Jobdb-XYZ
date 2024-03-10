import sqlite3 as db
from classes import Job
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

def save_job(data, url: str, id: str):
    if id == "duuni":
        return jobs_duunitori(data, url)
    elif id == "jobly":
        return jobs_jobly(data)

def jobs_jobly(data) -> Job:
    job_title = data.get('title')
    job_link = data.get('href')
    job_descr = None
    job_category = ""
    job_lvl = ""
    new_job = Job(job_title, job_link, job_descr, job_category, job_lvl)
    return new_job

def jobs_duunitori(data, url) -> Job:
    date = data.find('span', class_='job-box__job-posted').text
    if date[-1] == "." or date[-1] == "3":
        pass
    else:
        return None
    job_title = data.h3.text
    job_link = url + data.a['href']
    job_descr = None
    job_category = ""
    job_lvl = ""
    new_job = Job(job_title, job_link, job_descr, job_category, job_lvl)
    return new_job

def database_inserts(jobs_list: list):
    if testAndActConnection("../database/jobs.db", jobs_list) == True:
        pass
    else:
        job_dicts = [job.__dict__ for job in jobs_list]
        with open("../database/jobs_list.json", 'w') as file:
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
                id INTEGER PRIMARY KEY,
                title TEXT,
                link TEXT,
                descr TEXT,
                category TEXT,
                lvl TEXT,
                date DATE
            )
        """)

        # Fetch existing links from the database
        cursor.execute("SELECT link FROM jobs")
        existing_links = {row[0] for row in cursor.fetchall()}

        for job in jobs_list:
            # Check if the job link is already in the database
            if job.url not in existing_links:
                query = "INSERT INTO jobs (title, link, descr, category, lvl, date) VALUES (?, ?, ?, ?, ?, ?)"
                values = (job.title, job.url, job.descr, job.category, job.lvl, datetime.now().date())
                cursor.execute(query, values)
                sqlConnection.commit()
                existing_links.add(job.url)  # Add the new link to the set of existing links
        sqlConnection.commit()

    except db.Error as error:
        print("Error while connecting to SQLite database: ", error)
        return False

    finally:
        if sqlConnection:
            # close the connection to the database
            sqlConnection.close()
            # print("Closing successful.")
            return True
        else:
            return False

def dntori(soup, job):
    description = soup.find('div', class_='gtm-apply-clicks description description--jobentry')
    # decsription needs to be checked for "sample job posts"
    if description:
        job.descr = description.get_text()
        return description.get_text()
    return None

def jobly(soup, job):
    description = soup.find('div', class_='field field--name-body field--type-text-with-summary field--label-hidden')
    job.descr = description.text
    return description.text

def categorize_job(filename: str, job: Job, id: str):
    response = requests.get(job.url)
    if response.status_code == 200:
        with open(filename, "r") as file:
            terms = file.read().split('\n')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        if id == "duuni":
            description = dntori(soup, job)
        elif id == "jobly":
            description = jobly(soup, job)
        if description:
            result = []
            for word in terms:
                if word in description:
                    if word.lower() not in result:
                        result.append(word.lower())
            for item in result:
                job.category += item + " "
            job.category.strip()

def open_database(db_name: str):
    try:
        sqlConnection = db.connect(db_name)
    except db.Error as error:
        print("Error while opening SQLite database: ", error)
        return None
    finally:
        if sqlConnection:
            return sqlConnection
        return None

def identify_lvl():
    db_conn = open_database("../database/jobs.db")
    cursor = db_conn.cursor()
    cursor.execute("SELECT id, title, descr FROM jobs")
    # Fetch the id, title, description
    records = cursor.fetchall()

    for record in records:
        record_id, title, description = record
        lvl = ""

        # Determine the value for lvl
        if description and title:
            if "senior" in title.lower() or "senior" in description.lower() or "kokenut" in description.lower():
                lvl = "senior"
            elif "junior" in title.lower() or "junior" in description.lower() or "trainee" in description.lower() or "harjoittelija" in description.lower():
                lvl = "junior"
            else:
                lvl = "unknown"

        # Update the database with the new lvl value
        cursor.execute("UPDATE jobs SET lvl = ? WHERE id = ?", (lvl, record_id))

    # Commit changes and close the connection
    db_conn.commit()
    db_conn.close()