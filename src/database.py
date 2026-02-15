import sqlite3
from datetime import datetime 


DB_path = "date/jobs.db"

def get_connection():
  return sqlite3.connect(DB_PATH)
  
def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT,
        normalized_title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        date_posted TEXT,
        source TEXT,
        url TEXT,
        legitimacy_score INTEGER,
        similar_in_6_months INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_job(job):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO jobs (
        job_title, normalized_title, company, location,
        description, date_posted, source, url,
        legitimacy_score, similar_in_6_months
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        job["job_title"],
        job["normalized_title"],
        job["company"],
        job["location"],
        job["description"],
        job["date_posted"],
        job["source"],
        job["url"],
        job["legitimacy_score"],
        job["similar_in_6_months"]
    ))

    conn.commit()
    conn.close()

def check_similar_job(company, normalized_title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM jobs
    WHERE company = ?
    AND normalized_title = ?
    AND date(date_posted) >= date('now', '-180 day')
    """, (company, normalized_title))

    count = cursor.fetchone()[0]
    conn.close()

    return count
