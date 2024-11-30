from flask import Flask, request, render_template, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/login')
def login():
    return render_template('Login.html')

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

@app.route('/find_sale')
def find_sale():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sale")
    sales = cursor.fetchall()  # Fetch all rows from the sale table
    conn.close()

    return render_template('findsale.html', sales=sales)

@app.route('/sale_search', methods=['POST'])
def sale_search():
    sale_id = request.form.get('sale_id')
    customer_email = request.form.get('customer_email')
    sale_date = request.form.get('sale_date')
    employee_id = request.form.get('employee_id')

    # Build the query
    query = "SELECT * FROM sale WHERE 1=1"
    params = []

    if sale_id:
        query += " AND sale_id = %s"
        params.append(sale_id)
    if customer_email:
        query += " AND customer_email = %s"
        params.append(customer_email)
    if sale_date:
        query += " AND sale_date = %s"
        params.append(sale_date)
    if employee_id:
        query += " AND employee_id = %s"
        params.append(employee_id)

    # Execute the query
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query, params)
    sales = cursor.fetchall()
    conn.close()

    # Render results in the HTML template
    return render_template('findsale.html', sales=sales)

    



# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',  # Your MySQL username
    'password': 'admin',  # Your MySQL password
    'database': 'bmw_dealership_db'
}

# retrieves a table of the cars that the user searched for
@app.route('/car_search', methods=['GET', 'POST'])
def car_search():
    model = request.values.get('model')
    car_year = request.values.get('car_year')
    manufacturing_country = request.values.get('manufacturing_country')
    msrp_min = request.values.get('msrp_min')
    msrp_max = request.values.get('msrp_max')

    query = "SELECT * FROM car_type WHERE 1=1"
    params = []

    if model:
        query += " AND model LIKE %s"
        params.append(f"%{model}%")
    if car_year and car_year.isdigit():
        query += " AND car_year = %s"
        params.append(car_year)
    if manufacturing_country:
        query += " AND manufacturing_country LIKE %s"
        params.append(f"%{manufacturing_country}%")
    if msrp_min and msrp_min.isdigit():
        query += " AND msrp >= %s"
        params.append(msrp_min)
    if msrp_max and msrp_max.isdigit():
        query += " AND msrp <= %s"
        params.append(msrp_max)

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]

        if rows:
            return render_template(
                'car_search_results.html',
                headers=headers,
                rows=rows
            )
        else:
            return render_template(
                'car_search_results.html',
                headers=None,
                rows=None,
                message="No cars match your search criteria."
            )

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        conn.close()

#when the customer clicks the button next to car_search results, they get a table of available cars from the new inventory
@app.route('/car_inventory', methods=['GET'])
def car_inventory():
    # Get the type_id from the query parameter
    type_id = request.args.get('type_id')

    if not type_id:
        return "No type_id provided", 400

    try:
        # Database connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to get car details from new_inventory joined with car_type
        query = """
        SELECT ni.*, ct.model, ct.manufacturing_country 
        FROM new_inventory ni
        JOIN car_type ct ON ni.type_id = ct.type_id 
        WHERE ct.type_id = %s
        """

        cursor.execute(query, (type_id,))
        rows = cursor.fetchall()

        if rows:
            # Build HTML table for displaying results
            html_table = """
            <table border="1">
                <thead>
                    <tr>
                        <th>Car ID</th>
                        <th>Vin</th>
                        <th>Color</th>
                        <th>Model</th>
                        <th>Manufacturing Country</th>
                    </tr>
                </thead>
                <tbody>
                    {}
                </tbody>
            </table>
            """.format(
                "".join(
                    "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
                    for row in rows
                )
            )
        else:
            html_table = "<p>No inventory found for this car model.</p>"

        # Return the table as part of the new page
        return render_template_string("""
        <html>
        <body>
            <h2>Available Cars</h2>
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
    # Get user input from the form
    search_entry = request.args.get('e_name')

    # Base SQL query
    query = " SELECT CONCAT(first_name, ' ', last_name) AS Name, employee.email AS Email, emp_info.phone_number AS Phone, department.department_name AS Department FROM employee JOIN emp_info ON emp_info.email = employee.email JOIN department ON employee.department_id = department.department_id"
    params = []

    # Add conditions based on user input
    if search_entry:
        query += " AND (first_name LIKE '" + search_entry + "' OR last_name LIKE '" + search_entry + "' OR CONCAT(first_name, ' ', last_name) LIKE '" + search_entry + "')"

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
            <h2>Employee Contact Results</h2>
            {{ table|safe }}
            <br>
            <a href="{{ url_for('find_employee2') }}">Back to Search</a>
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
