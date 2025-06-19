import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "transactions.db"

def get_db_connection():
    print("🔍 Using DB Path:", DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # ✅ Enables dict-style access like row["status"]
    return conn
