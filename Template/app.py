from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'admin',  # Your MySQL password
    'database': 'bmw_dealership_db'
}

#customer car searching method

@app.route('/car_search')
def car_search():
    # Get user inputs
    model = request.args.get('model')
    car_year = request.args.get('car_year')
    manufacturing_country = request.args.get('manufacturing_country')
    msrp_min = request.args.get('msrp_min')
    msrp_max = request.args.get('msrp_max')

    query = "SELECT * FROM car_type WHERE 1=1"
    params = []

    if model:
        query += " AND model LIKE %s"
        params.append(f"%{model}%")
    if car_year:
        if car_year.isdigit():  # Validate numeric input
            query += " AND car_year = %s"
            params.append(car_year)
    if manufacturing_country:
        query += " AND manufacturing_country LIKE %s"
        params.append(f"%{manufacturing_country}%")
    if msrp_min:
        if msrp_min.isdigit():  # Validate numeric input
            query += " AND msrp >= %s"
            params.append(msrp_min)
    if msrp_max:
        if msrp_max.isdigit():  # Validate numeric input
            query += " AND msrp <= %s"
            params.append(msrp_max)

    try:
        # Database connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)  # Use parameterized query
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]

        # Build HTML table
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

        # Return rendered HTML
        return render_template_string("""
        <html>
        <body>
            {{ table|safe }}
        </body>
        </html>
        """, table=html_table)

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)


def send_purchase():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM users"  # Replace with your query that sends purchase data to the purchase table

    cursor.close()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
