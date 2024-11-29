from flask import Flask, redirect, request, render_template, render_template_string, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Your MySQL password
    'database': 'my_database'
}

@app.route('/search')
def search():
    model = request.args.get('model')
    car_year = request.args.get('car_year')
    manufacturing_country = request.args.get(' manufacturing_country')
    msrp_min = request.args.get('msrp_min')
    msrp_max = request.args.get('msrp_max')

    query = "SELECT * FROM car_type WHERE 1=1"
    if model:
        query += f" AND model LIKE '%{model}%'"
    if car_year:
        query += f" AND car_year = {car_year}"
    if manufacturing_country:
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
     return render_template_string("""
     <html>
     <body>
        {{ table|safe }}
      </body>
      </html>
      """, table=html_table)

       except mysql.connector.Error as err:
           return f"Error: {err}"

           if __name__ == '__main__':
               app.run(debug=True)






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

if __name__ == '__main__':
    app.run(debug=True)
