import sqlite3
import os

os.makedirs("data", exist_ok=True)


class Database:

    def __init__(self):

        self.conn = sqlite3.connect("data/jobhunter.db")

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                title TEXT,

                company TEXT,

                location TEXT,

                salary TEXT,

                url TEXT UNIQUE,

                source TEXT,

                score REAL,

                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
        """)

        self.conn.commit()

    def save_job(self, job):

        try:

            self.cursor.execute("""

            INSERT INTO jobs(title,company,location,salary,url,source,score)

            VALUES(?,?,?,?,?,?,?)

            """, (

                job.title,

                job.company,

                job.location,

                job.salary,

                job.url,

                job.source,

                job.score

            ))

            self.conn.commit()

            return True

        except sqlite3.IntegrityError:

            return False


db = Database()