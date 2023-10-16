import sqlite3 as db
from bs4 import BeautifulSoup
import requests

database = "database/jobs.db"

# TEST THIS LINK FOR EXAMPLE:
# https://duunitori.fi/tyopaikat/tyo/senior-java-developer-relocation-to-switzerland-scsom-14504783

def checkForOld(links: dict) -> list:
    toDelete = [] # Store the ID to be removed from Database
    for key, value in links.items():
        response = requests.get(value)
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            grid = soup.find_all('h2', class_='text--warning')
            if grid:
                toDelete.append(key)
                print("    yes")
        print("NO")
    print(toDelete)


def open_database(db_name):
    sqlConnection = None
    try:
        sqlConnection = db.connect(db_name)
        cursor = sqlConnection.cursor()
        cursor.execute("""
            SELECT link, id FROM jobs;
            """)
        rows = cursor.fetchall()
        linksToTest = {} # Collect ID and link
        for row in rows:
            link_val, id_val = row
            linksToTest[id_val] = link_val
        cursor.close()
        #for key, value in linksToTest.items():
        #    print(key, value)

        toDelete = checkForOld(linksToTest)

    except db.Error as error:
        print("Error while connecting to SQLite database: ", error)
        return

    finally:
        if sqlConnection:
            sqlConnection.close()
            print("Success and done")
        return

open_database(database)
