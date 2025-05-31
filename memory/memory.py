import sqlite3
import json
from datetime import datetime

conn = sqlite3.connect("memory_logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    format TEXT,
    intent TEXT,
    timestamp TEXT,
    sender TEXT,
    result TEXT
)
""")
conn.commit()

def log_to_memory(source, fmt, intent, sender, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO memory (source, format, intent, timestamp, sender, result)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (source, fmt, intent, timestamp, sender, json.dumps(result)))
    conn.commit()
    
def fetch_logs(limit=10):
    cursor.execute("""
        SELECT id, source, format, intent, timestamp, sender, result
        FROM memory ORDER BY timestamp DESC LIMIT ?
    """, (limit,))
    return cursor.fetchall()
