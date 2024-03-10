import sqlite3 as db

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
    # get title, link, lvl FROM jobs
    jobs = []
    cursor = sql_connection.cursor()
    cursor.execute("SELECT title, link, lvl FROM jobs")
    titles = cursor.fetchall()
    for item in titles:
        jobs.append({"title": item[0], "link": item[1], "lvl": item[2]})
    # Close the cursor and return the results
    cursor.close()
    sql_connection.close()
    return jobs