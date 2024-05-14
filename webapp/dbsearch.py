import sqlite3 as db
from datetime import datetime
import logging

def open_database(db_name: str):
    try:
        sqlConnection = db.connect(db_name)
    except db.Error as error:
        logging.error('Error: ', error)
        return None
    finally:
        if sqlConnection:
            return sqlConnection
        return None

def search_database(sql_connection, words: list) -> list:
    cursor = sql_connection.cursor()
    cursor.execute("SELECT title, category, link, lvl, date FROM jobs")
    # Fetch all the titles, category, link, and lvl (lvl to be used later
    # in frontend to select junior or senior)
    titles = cursor.fetchall()
    jobs = []
    for item in titles:
        categories = item[1].split(' ')
        for keyword in words:
            if keyword.lower() in categories:
                jobs.append({"name": item[0], "link": item[2], "lvl": item[3], "date": item[4]})
                break
        if keyword.lower() == "c":
            jobs.append({"name": item[0], "link": item[2], "lvl": item[3], "date": item[4]})

    # Close the cursor and return the results
    cursor.close()
    sql_connection.close()
    return jobs

def api_jobs(sql_connection) -> list:
    # get title, link, lvl FROM jobs WHERE date = today
    jobs = []
    cursor = sql_connection.cursor()
    today_date = datetime.now().date()
    cursor.execute("SELECT title, link, lvl, date FROM jobs WHERE date = ?", (today_date,))
    records_with_today_date = cursor.fetchall()
    for item in records_with_today_date:
        jobs.append({"title": item[0], "link": item[1], "lvl": item[2], "date": item[3]})
    # Close the cursor and return the results
    cursor.close()
    sql_connection.close()
    return jobs


def api_jobs_jr(sql_connection) -> list:
    # get title, link, lvl FROM jobs WHERE lvl = 'junior'
    jobs = []
    cursor = sql_connection.cursor()
    cursor.execute("SELECT title, link, lvl, date FROM jobs WHERE lvl = 'junior'")
    records = cursor.fetchall()
    for item in records:
        jobs.append({"title": item[0], "link": item[1], "lvl": item[2], "date": item[3]})
    # Close the cursor and return the results
    cursor.close()
    sql_connection.close()
    return jobs

def api_jobs_sr(sql_connection) -> list:
    # get title, link, lvl FROM jobs WHERE lvl = 'senior'
    jobs = []
    cursor = sql_connection.cursor()
    cursor.execute("SELECT title, link, lvl, date FROM jobs WHERE lvl = 'senior'")
    records = cursor.fetchall()
    for item in records:
        jobs.append({"title": item[0], "link": item[1], "lvl": item[2], "date": item[3]})
    # Close the cursor and return the results
    cursor.close()
    sql_connection.close()
    return jobs
