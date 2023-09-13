
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
        else:
            return None

def search_database(sql_connection, words: list):
    cursor = sql_connection.cursor()
    query = "SELECT title, link FROM jobs"
    cursor.execute(query)
    # Fetch all the titles
    titles = cursor.fetchall()
    # Close the cursor and return the results
    cursor.close()
    return titles

