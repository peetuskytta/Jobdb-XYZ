import sqlite3 as db
from bs4 import BeautifulSoup
import requests

database = "../database/jobs.db"

# TEST THIS LINK FOR EXAMPLE:
# https://duunitori.fi/tyopaikat/tyo/senior-java-developer-relocation-to-switzerland-scsom-14504783

def checkForOld(links: dict) -> list:
    toDelete = [] # Store the ID to be removed from Database
    for key, value in links.items():
        #print(key)  # Print the key (ID) for debugging
        if value == "ERROR":
            toDelete.append(key)
        else:
            response = requests.get(value)
            if response.status_code == 200:
                html = response.content
                soup = BeautifulSoup(html, 'html.parser')
                grid = soup.find_all('h2', class_='text--warning')
                if grid:
                    toDelete.append(key)
    return toDelete

def clean_database():
    sqlConnection = None
    try:
        sqlConnection = db.connect("../database/jobs.db")
        cursor = sqlConnection.cursor()
        cursor.execute("""
            SELECT link, id, title, category FROM jobs;
            """)
        rows = cursor.fetchall()
        linksToTest = {}
        errorCases = ["c-kort", "hoitaj", "esperi", "sairaanhoidon", "myyjiä", "myyjä", "lukkoseppä", "fashion", "sosiaali", "inside sales", "attorney", "legal", "marketing", "ecommerce manager", "sähkösuunnittelija", "projektipäälli", "luottoriskianalyytikko", "supervisor/commissioning", "talent acquisition", "doctoral research", "treasury"]
        for row in rows:
            link_val, id_val, title, category = row
            if row[2].lower() in errorCases:
                linksToTest[id_val] = "ERROR"
            if row[3] == "c on r ":
                linksToTest[id_val] = "ERROR"
            else:
                linksToTest[id_val] = link_val
        toDelete = checkForOld(linksToTest)
        for item in toDelete:
            cursor.execute("SELECT id FROM jobs WHERE id = ?", (item,))
            existing_id = cursor.fetchone()
            if existing_id:
                cursor.execute("DELETE FROM jobs WHERE id = ?", (item,))
        cursor.execute("DELETE FROM jobs WHERE title LIKE '%C-%'")
        sqlConnection.commit()
        cursor.close()

    except db.Error as error:
        print("Error while connecting to SQLite database while cleaning: ", error)
        return

    finally:
        if sqlConnection:
            sqlConnection.close()
        return