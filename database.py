import sqlite3

conn = sqlite3.connect("products.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS saved (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score REAL
)
""")

def save_product(name, score):
    cursor.execute("INSERT INTO saved (name, score) VALUES (?, ?)", (name, score))
    conn.commit()

def get_saved():
    cursor.execute("SELECT name, score FROM saved ORDER BY score DESC")
    return cursor.fetchall()
