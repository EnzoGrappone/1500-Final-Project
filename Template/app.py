from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Your MySQL password
    'database': 'my_database'
}

@app.route('/search') def search():
model = request.args.get('model')
car_year = request.args.get('car_year')
manufacturing_country = request.args.get(' manufacturing_country')
msrp_min = request.args.get('msrp_min')
msrp_max = request.args.get('msrp_max')
query = "SELECT * FROM car_type WHERE 1=1"
if model:
     query += f" AND model LIKE '%{model}%'"
if year:
     query += f" AND car_year = {car_year}"
if country:
    query += f" AND manufacturing_country LIKE '%{ manufacturing_country}%'"
if msrp_min:
     query += f" AND msrp >= {msrp_min}"
if msrp_max:
    query += f" AND msrp <= {msrp_max}"
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()

    html_table = """
    <table border="1">
    <thead>
    <tr>{}</tr>
    </thead> <tbody>
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
     return render_template_string("""
     <html>
      <body>
      {{ table|safe }}
      </body>
      </html>
      """, table=html_table)
       except mysql.connector.Error as err:
           return f"Error: {err}"
           if __name__ == '__main__': app.run(debug=True)






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
