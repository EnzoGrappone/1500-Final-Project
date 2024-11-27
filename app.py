from flask import Flask, request, render_template, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/home1')
def home1():
    return render_template('index.html')

@app.route('/findcar')
def find_car():
    return render_template('Findcar.html')

@app.route('/purchasecar')
def purchase_car():
    return render_template('purchasecar.html')

@app.route('/findemployee1')
def find_employee1():
    return render_template('findemployee.html')

@app.route('/findemployee2')
def find_employee2():
    return render_template('findemployee2.html')

@app.route('/stock')
def stock():
    return render_template('Stock.html')

@app.route('/findcustomer')
def find_customer():
    return render_template('findcustomer.html')

@app.route('/findservice')
def find_service():
    return render_template('findservice.html')

@app.route('/home2')
def home2():
    return render_template('index2.html')

@app.route('/findsale')
def find_sale():
    return render_template('findsale.html')

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',  # Your MySQL username
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
            <a href="{{ url_for('find_car') }}">Back to Search</a>
        </body>
        </html>
        """, table=html_table)

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        conn.close()

@app.route('/employee_contact', methods=['GET', 'POST'])
def employee_contact():
    # Get the search term (either first name or last name)
    search_term = request.args.get('search_term')

    # Base SQL query to search employees by first or last name
    query = "SELECT first_name, last_name, email FROM emp_info WHERE 1=1"
    params = []

    # Add conditions to the query based on the search term
    if search_term:
        query += " AND (first_name LIKE %s OR last_name LIKE %s)"
        params.append(f"%{search_term}%")
        params.append(f"%{search_term}%")

    try:
        # Database connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)  # Execute the parameterized query
        rows = cursor.fetchall()
        headers = ['First Name', 'Last Name', 'Email']

        # If results are found, build HTML table
        if rows:
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
            html_table = "<p>No employees found.</p>"

        # Return rendered HTML with the employee search results
        return render_template_string("""
        <html>
        <body>
            <h2>Employee Search Results</h2>
            {{ table|safe }}
            <br>
            <a href="{{ url_for('find_employee') }}">Back to Search</a>
        </body>
        </html>
        """, table=html_table)

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        conn.close()

# Only one app.run() needed, here at the bottom.
if __name__ == '__main__':
    app.run(debug=True)
