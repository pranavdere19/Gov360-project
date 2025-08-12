import sqlite3

DB_NAME = "policies.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS policies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year INTEGER,
            sector TEXT,
            summary TEXT,
            details TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_policy(policy):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO policies (title, year, sector, summary, details, url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        policy['title'],
        policy['year'],
        policy['sector'],
        policy['summary'],
        policy['details'],
        policy['url']
    ))
    conn.commit()
    conn.close()

def get_all_policies():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM policies")
    rows = c.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "title": row[1],
            "year": row[2],
            "sector": row[3],
            "summary": row[4],
            "details": row[5],
            "url": row[6],
        }
        for row in rows
    ]