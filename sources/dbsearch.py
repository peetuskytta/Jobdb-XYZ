
import sqlite3 as db

def open_database(db_name: str):
    try:
        sqlConnection = db.connect(db_name)
    except db.Error as error:
        print("Error while connecting to SQLite database", error)
        return None
    finally:
        if sqlConnection:
            return sqlConnection
        return None

def search_database(sql_connection, words: list):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT title, category, link FROM jobs")
    # Fetch all the titles
    titles = cursor.fetchall()
    jobs = []
    for item in titles:
        categories = item[1].split(' ')
        for keyword in words:
            if keyword in categories:
                jobs.append({item[0]:item[2]})
                break
    # Close the cursor and return the results
    cursor.close()
    return jobs

