import sqlite3 as db
import json

def database_inserts(jobs_list: list):
    if testAndActConnection("database/jobs.db", jobs_list) == True:
        pass
    else:
        job_dicts = [job.__dict__ for job in jobs_list]
        with open("database/job_list.json", 'w') as file:
            json.dump(job_dicts, file, indent=2)
        return

def testAndActConnection(db_name: str, jobs_list: list):
    sqlConnection = None
    try:
        print("Connection to database was successful. Initiating the data insertion...")
        sqlConnection = db.connect(db_name)
        cursor = sqlConnection.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                nro INTEGER PRIMARY KEY,
                id INTEGER,
                title TEXT,
                link TEXT,
                description TEXT,
                category TEXT,
                level TEXT
            )
        """)
        cursor.execute("SELECT id FROM jobs")
        rows = cursor.fetchall()  # fetches all the id rows to be checked for existing ones
        compareIds = [row[0] for row in rows]

        for job in jobs_list:
            if job.id in compareIds:
                continue
            else:
                query = "INSERT INTO jobs (id, title, link, description, category, level) VALUES (?, ?, ?, ?, ?, ?)"
                values = (job.id, job.title, job.url, job.description, job.category, job.level)
                cursor.execute(query, values)
                compareIds.append(job.id)
                sqlConnection.commit()

        sqlConnection.commit()

    except db.Error as error:
        print("Error while connecting to SQLite database: ", error)
        return False

    finally:
        if sqlConnection:
            # close the connection to the database
            sqlConnection.close()
            print("Closing successful.")
            return True
        else:
            return False