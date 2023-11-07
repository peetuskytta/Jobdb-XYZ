import sqlite3 as db
from bs4 import BeautifulSoup
import requests

# TEST THIS LINK FOR EXAMPLE:
# https://duunitori.fi/tyopaikat/tyo/senior-java-developer-relocation-to-switzerland-scsom-14504783


### This function will load delete_pattern file content from files folder to search_patterns
### variable (list) which is used to delete specific patterns not wanted in the database.
def clean_database():
    sqlConnection = None
    print("Starting database cleaning based on patterns")
    try:
        sqlConnection = db.connect("../database/jobs.db")
        cursor = sqlConnection.cursor()

        # open and split content of the file
        with open("files/delete_pattern", 'r') as file:
            search_patterns = file.read().splitlines()

        # loop the patterns and execute sql DELETE
        for pattern in search_patterns:
            sql = f"DELETE FROM jobs WHERE title LIKE '{pattern}'"
            cursor.execute(sql)
            sqlConnection.commit()

        sqlConnection.commit()
        cursor.close()

    except db.Error as error:
        print("Error connecting to SQLite database while cleaning: ", error)
        return

    finally:
        if sqlConnection:
            sqlConnection.close()
        return

# if you want to run this separately remove the comment on the next line and run the script with command: 'python3 clean_database.py'
clean_database()

### Make a separate cleaner for out of date job postings.
### Tricky to make work for multiple different job sites.
### Consider deleting any posting that has been in database for more than a month.