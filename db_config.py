import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname='feedbackdb',
        user='postgres',
        password='ravi811@',  # Replace with your actual password
        host='localhost',
        port='5432'
    )
    return conn
 
