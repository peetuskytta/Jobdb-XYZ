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

def search_database(sql_connection, words: list):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT title, category, link, lvl FROM jobs")
    # Fetch all the titles, category and link
    titles = cursor.fetchall()
    jobs = []
    for item in titles:
        categories = item[1].split(' ')
        for keyword in words:
            if keyword.lower() in categories:
                jobs.append({"name": item[0], "link": item[2], "lvl": item[3]})
                break
    # Close the cursor and return the results
    cursor.close()
    sql_connection.close()
    return jobs

