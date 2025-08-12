import sqlite3
import os

db_path = os.path.abspath("Policies.db")
print("📂 Using database file at:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS policies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
)
""")

# Only insert if table is empty
cursor.execute("SELECT COUNT(*) FROM policies")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("INSERT INTO policies (title, description) VALUES (?, ?)",
                   ("Digital India Policy", "Improving digital infrastructure and governance."))
    conn.commit()
    print("✅ Inserted 'Digital India Policy'")

# Fetch and show all records
cursor.execute("SELECT * FROM policies")
rows = cursor.fetchall()

if rows:
    print("\n📄 Existing Policies:")
    for row in rows:
        print(f"ID: {row[0]} | Title: {row[1]} | Description: {row[2]}")
else:
    print("⚠️ No policies found.")

conn.close()