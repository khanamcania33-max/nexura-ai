import sqlite3

conn = sqlite3.connect("products.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS saved (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score REAL
)
""")

def save_product(pid, name, score):
    cursor.execute("INSERT OR IGNORE INTO saved VALUES (?, ?, ?)", (pid, name, score))
    conn.commit()

def unsave_product(pid):
    cursor.execute("DELETE FROM saved WHERE id=?", (pid,))
    conn.commit()

def get_saved_ids():
    cursor.execute("SELECT id FROM saved")
    return [x[0] for x in cursor.fetchall()]

def get_saved():
    cursor.execute("SELECT name, score FROM saved ORDER BY score DESC")
    return cursor.fetchall()
