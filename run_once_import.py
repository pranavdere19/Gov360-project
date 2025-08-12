import json
import sqlite3

# Load policies from policies.json
with open("data/policies.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create new database
conn = sqlite3.connect("policies.db")
c = conn.cursor()

# Create table
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

# Insert each policy into the table
for p in data:
    c.execute('''
        INSERT INTO policies (title, year, sector, summary, details, url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (p["title"], p["year"], p["sector"], p["summary"], p["details"], p["url"]))

conn.commit()
conn.close()

print("✅ Database created and policies imported successfully.")