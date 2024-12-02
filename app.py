from flask import Flask, request, render_template, render_template_string, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
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

@app.route('/Findcustomer')
def find_customer():
    return render_template('findcustomer.html')

@app.route('/stock')
def stock():
    return render_template('Stock.html')

#when employee searches through new and used inventories
@app.route('/search_inventory', methods=['POST'])
def search_inventory():
    # Get form data
    inventory_type = request.form.get('inventory_type')  # 'new_inventory' or 'used_inventory'
    model = request.form.get('model')
    year = request.form.get('year')
    manufacturing_country = request.form.get('manufacturing_country')
    msrp_min = request.form.get('msrp_min')
    msrp_max = request.form.get('msrp_max')

    # Construct base query with JOIN
    if inventory_type == "new_inventory":
        query = f"""
            SELECT 
                car_type.model,
                inv.vin,
                car_type.car_year,
                car_type.manufacturing_country, 
                car_type.msrp 
            FROM {inventory_type} inv
            JOIN car_type ON inv.type_id = car_type.type_id
            WHERE 1=1
        """
    if inventory_type == "used_inventory":
        query = "SELECT * FROM used_inventory WHERE 1=1"

    params = []

    # Add filters dynamically
    if model:
        query += " AND car_type.model = %s"
        params.append(model)
    if year:
        query += " AND inv.year = %s"
        params.append(year)
    if manufacturing_country:
        query += " AND car_type.manufacturing_country = %s"
        params.append(manufacturing_country)
    if msrp_min:
        query += " AND car_type.msrp >= %s"
        params.append(msrp_min)
    if msrp_max:
        query += " AND car_type.msrp <= %s"
        params.append(msrp_max)

    # Connect to the MySQL database
    results = []
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    if inventory_type == "new_inventory":
        # Generate an HTML table from the results
        table_html = """
        <table border="1" style="width:100%; border-collapse:collapse;">
            <thead>
                <tr>
                    <th>Model</th>
                    <th>Vin</th>
                    <th>Year</th>
                    <th>Manufacturing Country</th>
                    <th>MSRP</th
                </tr>
            </thead>
            <tbody>
        """
        for row in results:
            table_html += "<tr>"
            for cell in row:
                table_html += f"<td>{cell}</td>"
            table_html += "</tr>"
        table_html += """
            </tbody>
        </table>
        """

        # Render the table on a basic HTML page
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Inventory Search Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }}
                table {{
                    margin-top: 20px;
                    width: 100%;
                    border: 1px solid #ccc;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Inventory Search Results</h1>
            {table_html}
        </body>
        </html>
        """
    if inventory_type == "used_inventory":
        # Generate an HTML table from the results
        table_html = """
        <table border="1" style="width:100%; border-collapse:collapse;">
            <thead>
                <tr>
                    <th>Vin</th>
                    <th>Brand</th>
                    <th>Model</th>
                    <th>Year</th>
                    <th>Color</th>
                    <th>Mileage</th>
                    <th>Condition</th>
                    <th>Warranty Status</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
        """
        for row in results:
            table_html += "<tr>"
            for cell in row:
                table_html += f"<td>{cell}</td>"
            table_html += "</tr>"
        table_html += """
            </tbody>
        </table>
        """

        # Render the table on a basic HTML page
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Inventory Search Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }}
                table {{
                    margin-top: 20px;
                    width: 100%;
                    border: 1px solid #ccc;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Inventory Search Results</h1>
            {table_html}
        </body>
        </html>
        """
        
    return render_template_string(html_template)

@app.route('/findservice')
def find_service():
    return render_template('findservice.html')

#when employee searches through new and used inventories
@app.route('/findservice', methods=['POST'])
def search_service():
    # Get form data
    service_id = request.form.get('service_id')
    email = request.form.get('customer_email')
    date = request.form.get('date')
    license = request.form.get('license')
    service_type = request.form.get('service_type')
    employee_id = request.form.get('employee_id')

    if service_id:
        query = f"""SELECT service_id, customer_email, CONCAT(car_type.car_year, ' ', car_type.model), license_plate_number, color, service_type, appointment_date, CONCAT(employee.first_name, ' ', employee.last_name) 
        FROM service 
        JOIN car_type ON service.type_id = car_type.type_id JOIN employee ON employee.employee_id = service.employee_id 
        WHERE 1 = 1"""

        params = []

        query += " AND service_id = %s"
        params.append(service_id)

    else: 
        query = f"""
            SELECT service_id, customer_email, CONCAT(car_type.car_year, ' ', car_type.model), license_plate_number, color, service_type, appointment_date, CONCAT(employee.first_name, ' ', employee.last_name) 
            FROM service 
            JOIN car_type ON service.type_id = car_type.type_id JOIN employee ON employee.employee_id = service.employee_id
            WHERE 1 = 1
        """
        params = []

        # Add filters dynamically
        if email:
            query += " AND customer_email = %s"
            params.append(email)
        if date:
            query += " AND appointment_date = %s"
            params.append(date)
        if license:
            query += " AND license_plate_number = %s"
            params.append(license)
        if service_type:
            query += " AND service_type = %s"
            params.append(service_type)
        if employee_id:
            query += " AND employee_id = %s"
            params.append(employee_id)

    # Connect to the MySQL database
    results = []
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


    # Generate an HTML table from the results
    table_html = """
    <table border="1" style="width:100%; border-collapse:collapse;">
        <thead>
            <tr>
                <th>Service ID</th>
                <th>Customer Email</th>
                <th>Model</th>
                <th>License</th>
                <th>Color</th>
                <th>Service Type</th>
                <th>Appointment Date</th>
                <th>Employee</th>
            </tr>
        </thead>
        <tbody>
    """
    for row in results:
        table_html += "<tr>"
        for cell in row:
            table_html += f"<td>{cell}</td>"
        table_html += "</tr>"
    table_html += """
        </tbody>
    </table>
    """

    # Render the table on a basic HTML page
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inventory Search Results</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            table {{
                margin-top: 20px;
                width: 100%;
                border: 1px solid #ccc;
                border-collapse: collapse;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Inventory Search Results</h1>
        {table_html}
    </body>
    </html>
    """
    
    return render_template_string(html_template)

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
            <style>
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 1em;
                font-family: Arial, sans-serif;
                min-width: 400px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }}
            table thead tr {{
                background-color: #009879;
                color: #ffffff;
                text-align: left;
            }}
                table th, table td {{
                padding: 12px 15px;
                border: 1px solid #dddddd;
            }}
            table tbody tr {{
                border-bottom: 1px solid #dddddd;
            }}
            table tbody tr:nth-of-type(even) {{
                background-color: #f3f3f3;
            }}
            table tbody tr:last-of-type {{
                border-bottom: 2px solid #009879;
            }}
            </style>
            <table>
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


@app.route('/purchase', methods=['POST'])
def purchase():
    model = request.form.get('model')
    car_color = request.form.get('color')
    customer_email = request.form.get('customer_email')
    employee_id = request.form.get('employee_id')
    sale_date = request.form.get('sale_date')

    if not (model and car_color and customer_email and employee_id and sale_date):
        return "Missing data", 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query_car = """
            SELECT new_inventory.vin, car_type.msrp
            FROM car_type
            JOIN new_inventory ON car_type.type_id = new_inventory.type_id
            WHERE car_type.model = %s AND new_inventory.color = %s
        """
        cursor.execute(query_car, (model, car_color))
        car = cursor.fetchone()

        if car is not None:
            vin = car[0]
            sale_price = car[1]

            cursor.execute("SELECT MAX(CAST(SUBSTRING(sale_id, 2) AS UNSIGNED)) FROM sale")
            max_id = cursor.fetchone()[0]
            if max_id is None:
                sale_id = "S1"
            else:
                sale_id = f"S{max_id + 1}"
            
            query_add_sale = """
                INSERT INTO sale (sale_id, customer_email, vin, sale_date, sale_price, employee_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query_add_sale, (customer_email, vin, sale_date, sale_price, employee_id))

            query_remove_car = "DELETE FROM new_inventory WHERE vin = %s"
            cursor.execute(query_remove_car, (vin,))

            conn.commit()
            return f"Purchase successful! Sale ID: {sale_id}"

        else:
            return "Car not found", 404

    except mysql.connector.Error as err:
        return f"Error: {err}", 500

    finally:
        cursor.close()
        conn.close()

@app.route('/get_customer', methods=['GET', 'POST'])
def get_customer():
    # Get user input from the form
    search_entry = request.form.get('query')

    # Base SQL query
    query = " SELECT CONCAT(first_name, ' ', last_name) AS Name, customer.customer_email AS Email, cust_contact.phone_number AS Phone, cust_contact.address AS Address FROM customer JOIN cust_contact ON customer.customer_email = cust_contact.customer_email"
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
            <style>
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 1em;
                font-family: Arial, sans-serif;
                min-width: 400px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }}
            table thead tr {{
                background-color: #009879;
                color: #ffffff;
                text-align: left;
            }}
                table th, table td {{
                padding: 12px 15px;
                border: 1px solid #dddddd;
            }}
            table tbody tr {{
                border-bottom: 1px solid #dddddd;
            }}
            table tbody tr:nth-of-type(even) {{
                background-color: #f3f3f3;
            }}
            table tbody tr:last-of-type {{
                border-bottom: 2px solid #009879;
            }}
            </style>
            <table>
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
            <h2>Customer Contact Results</h2>
            {{ table|safe }}
            <br>
            <a href="{{ url_for('find_customer') }}">Back to Search</a>
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
            <style>
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 1em;
                font-family: Arial, sans-serif;
                min-width: 400px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }}
            table thead tr {{
                background-color: #009879;
                color: #ffffff;
                text-align: left;
            }}
                table th, table td {{
                padding: 12px 15px;
                border: 1px solid #dddddd;
            }}
            table tbody tr {{
                border-bottom: 1px solid #dddddd;
            }}
            table tbody tr:nth-of-type(even) {{
                background-color: #f3f3f3;
            }}
            table tbody tr:last-of-type {{
                border-bottom: 2px solid #009879;
            }}
            </style>
            <table>
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


@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input from the form
        username = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('user-type')
        # Validate input
        if not username or not password or not user_type:
            return render_template('Login.html', error="Please fill all fields.")
        try:
            # Database connection
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            # Determine query based on user type
            if user_type == 'Customer':
                query = "SELECT * FROM customer JOIN cust_contact ON customer.customer_email = cust_contact.customer_email WHERE customer.customer_email = %s AND cust_contact.password = %s"
            else:
                query = "SELECT * FROM employee JOIN emp_info ON employee.email = emp_info.email WHERE employee.email = %s AND emp_info.password = %s"
            # Execute query
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            if result:
                # Redirect based on user type
                if user_type == 'Customer':
                    return redirect(url_for('home1'))
                elif user_type == 'Employee':
                    return redirect(url_for('home2'))
            else:
                return render_template('Login.html', error="Incorrect username or password.")
        finally:
            cursor.close()
            conn.close()



# Only one app.run() needed, here at the bottom.
if __name__ == '__main__':
    app.run(debug=True)
