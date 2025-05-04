from db_config import get_db_connection

def insert_feedback(username, message):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback_wall (username, message) VALUES (%s, %s)", (username, message))
    conn.commit()
    cur.close()
    conn.close()

def get_all_feedback():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, message, timestamp FROM feedback_wall ORDER BY timestamp DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
 
