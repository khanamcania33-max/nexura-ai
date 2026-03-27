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
    try:
        cursor.execute("INSERT OR IGNORE INTO saved VALUES (?, ?, ?)", (pid, name, score))
        conn.commit()
    except:
        pass

def unsave_product(pid):
    try:
        cursor.execute("DELETE FROM saved WHERE id=?", (pid,))
        conn.commit()
    except:
        pass

def get_saved_ids():
    try:
        cursor.execute("SELECT id FROM saved")
        return [x[0] for x in cursor.fetchall()]
    except:
        return []
