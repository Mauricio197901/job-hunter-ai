import sqlite3
from pathlib import Path

DB_PATH = Path("data/jobhunter.db")
DB_PATH.parent.mkdir(exist_ok=True)


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT,
                location TEXT,
                salary TEXT,
                url TEXT UNIQUE,
                source TEXT,
                description TEXT,
                score REAL DEFAULT 0,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save_job(self, job):
        try:
            self.cursor.execute("""
                INSERT INTO jobs
                (title, company, location, salary, url, source, description, score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                job.title,
                job.company,
                job.location,
                job.salary,
                job.url,
                job.source,
                job.description,
                job.score
            ))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def total_jobs(self):
        self.cursor.execute("SELECT COUNT(*) AS total FROM jobs")
        return self.cursor.fetchone()["total"]


db = Database()