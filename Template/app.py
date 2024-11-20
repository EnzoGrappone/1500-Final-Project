from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Your MySQL password
    'database': 'my_database'
}

@app.route('/fetch-table')
def fetch_table():
    # Query the database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT * FROM users"  # Replace with your query
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]  # Get column names
        cursor.close()
        conn.close()
        
        # Render data as an HTML table
        html_table = """
        <table border="1">
            <thead>
                <tr>{}</tr>
            </thead>
            <tbody>
                {}
            </tbody>
        </table>
        """.format(
            "".join(f"<th>{col}</th>" for col in headers),
            "".join(
                "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
                for row in rows
            )
        )
        return html_table

    except mysql.connector.Error as err:
        return f"Error: {err}"
    
def send_purchase():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM users"  # Replace with your query that sends purchase data to the purchase table

    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
