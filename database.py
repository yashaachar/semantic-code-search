import sqlite3

def init_db():
    conn = sqlite3.connect("snippets.db", check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY,
            filename TEXT,
            code TEXT,
            language TEXT
        )
    """)
    conn.commit()
    return conn

def insert_snippet(conn, filename, code, language):
    conn.execute("INSERT INTO snippets (filename, code, language) VALUES (?,?,?)",
                 (filename, code, language))
    conn.commit()

def get_snippet(conn, id):
    return conn.execute("SELECT * FROM snippets WHERE id=?", (id,)).fetchone()