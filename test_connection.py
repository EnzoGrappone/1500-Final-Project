import mysql.connector

def test_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin',
            database='bmw_dealership_db'
        )
        if conn.is_connected():
            print("Connection successful!")
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        print("Connected to database:", cursor.fetchone()[0])
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn:
            conn.close()

test_connection()
