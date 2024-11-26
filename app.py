from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/findcar')
def find_car():
    return render_template('Findcar.html')

@app.route('/purchasecar')
def purchase_car():
    return render_template('purchasecar.html')

@app.route('/findemployee2')
def find_employee():
    return render_template('findemployee2.html')

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'admin',  # Your MySQL password
    'database': 'bmw_dealership_db'
}

@app.route('/car_search', methods=['GET', 'POST'])
def car_search():
    # Get user inputs from the form
    model = request.args.get('model')
    car_year = request.args.get('car_year')
    manufacturing_country = request.args.get('manufacturing_country')
    msrp_min = request.args.get('msrp_min')
    msrp_max = request.args.get('msrp_max')

    # Base SQL query
    query = "SELECT * FROM car_type WHERE 1=1"
    params = []

    # Add conditions based on user input
    if model:
        query += " AND model LIKE %s"
        params.append(f"%{model}%")
    if car_year and car_year.isdigit():  # Validate numeric input
        query += " AND car_year = %s"
        params.append(car_year)
    if manufacturing_country:
        query += " AND manufacturing_country LIKE %s"
        params.append(f"%{manufacturing_country}%")
    if msrp_min and msrp_min.isdigit():  # Validate numeric input
        query += " AND msrp >= %s"
        params.append(msrp_min)
    if msrp_max and msrp_max.isdigit():  # Validate numeric input
        query += " AND msrp <= %s"
        params.append(msrp_max)

    try:
        # Database connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)  # Use parameterized query
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]

        # Handle empty results
        if rows:
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
        else:
            html_table = "<p>No results found.</p>"

        # Return rendered HTML
        return render_template_string("""
        <html>
        <body>
            <h2>Search Results</h2>
            {{ table|safe }}
            <br>
            <a href="/car_search">Back to Search</a>
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
