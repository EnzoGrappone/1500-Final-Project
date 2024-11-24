CREATE DATABASE
BMW_dealership_DB;
USE BMW_dealership_DB;
CREATE TABLE car_type (
	model VARCHAR(15),
    car_year YEAR,
    manufacturing_country VARCHAR(25),
	msrp INT,
    PRIMARY KEY (model, car_year)
);

CREATE TABLE new_inventory (
	vin CHAR(17),
    model VARCHAR(15),
    color VARCHAR(15),
    PRIMARY KEY (vin),
    FOREIGN KEY (model) REFERENCES car_type(model)
);

CREATE TABLE used_inventory (
	vin CHAR(17),
    brand VARCHAR(15),
    model VARCHAR(15),
    car_year YEAR,
    color VARCHAR(15),
    mileage INT,
    car_condition VARCHAR(15),
    warranty_status VARCHAR(15),
    price INT,
    PRIMARY KEY (vin)
);

CREATE TABLE customer (
	customer_email VARCHAR(256),
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    PRIMARY KEY (customer_email)
);

CREATE TABLE cust_contact (
	customer_email VARCHAR(256),
    phone_number CHAR(11),
    address VARCHAR (256),
    DOB DATE,
    PRIMARY KEY (customer_email),
    FOREIGN KEY (customer_email) REFERENCES customer(customer_email)
		ON DELETE CASCADE
);

CREATE TABLE department (
	department_id INT,
    department_name VARCHAR(15),
    department_size INT,
    PRIMARY KEY (department_id)
);

CREATE TABLE emp_info (
	email VARCHAR(256),
    phone_number CHAR(11),
    address VARCHAR(256),
    DOB DATE,
    salary INT,
    PRIMARY KEY (email)
);

CREATE TABLE employee (
	employee_id INT,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    department_id INT,
    email VARCHAR(256),
    PRIMARY KEY (employee_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
		ON DELETE SET NULL,
    FOREIGN KEY (email) REFERENCES emp_info(email)
		ON DELETE CASCADE
);

CREATE TABLE service (
	service_id INT,
    customer_email VARCHAR(256),
    model VARCHAR(15),
    liscense_plate_number VARCHAR(10),
    color VARCHAR(15),
    service_type VARCHAR(25),
    appointment_date DATE,
    employee_id INT,
    FOREIGN KEY (customer_email) REFERENCES customer(customer_email)
		ON DELETE SET NULL,
    FOREIGN KEY (model) REFERENCES car_type(model),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
		ON DELETE SET NULL,
    PRIMARY KEY (service_id)
);

CREATE TABLE sale (
	sale_id INT,
    customer_email VARCHAR(256),
    vin CHAR(17),
    sale_date DATE,
    sale_price INT,
    employee_id INT,
    FOREIGN KEY (customer_email) REFERENCES customer(customer_email)
		ON DELETE SET NULL,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
		ON DELETE SET NULL,
    PRIMARY KEY (sale_id)
);