import mysql.connector

def test_connection():
    try:
        conn = mysql.connector.connect(
            host='BMW_Database',
            user='root',
            password='password',
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
