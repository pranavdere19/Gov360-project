# db_handler.py
import sqlite3

def init_db():
    conn = sqlite3.connect("policies.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        policy_id INTEGER,
        text TEXT,
        sentiment TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    conn.commit()
    conn.close()

def insert_policy(title, content):
    conn = sqlite3.connect("policies.db")
    c = conn.cursor()
    c.execute("INSERT INTO policies (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def get_policies():
    conn = sqlite3.connect("policies.db")
    c = conn.cursor()
    c.execute("SELECT id, title FROM policies")
    data = c.fetchall()
    conn.close()
    return data