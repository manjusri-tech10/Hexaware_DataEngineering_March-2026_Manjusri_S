-- Create Database
CREATE DATABASE order_insights;
USE order_insights;

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    region VARCHAR(50)
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100),
    order_date DATETIME,
    expected_delivery DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Delivery Status Table
CREATE TABLE delivery_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    status VARCHAR(50),
    actual_delivery DATE,
    remarks TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- INSERT (Create)
INSERT INTO customers (name, email, phone, region) VALUES
('Alice Johnson', 'alice@email.com', '9876543210', 'North'),
('Bob Smith', 'bob@email.com', '9123456780', 'South'),
('Carol White', 'carol@email.com', '9988776655', 'East');

INSERT INTO orders (customer_id, product_name, order_date, expected_delivery) VALUES
(1, 'Laptop', '2024-01-01', '2024-01-07'),
(2, 'Phone', '2024-01-03', '2024-01-09'),
(3, 'Tablet', '2024-01-05', '2024-01-11');

INSERT INTO delivery_status (order_id, status, actual_delivery, remarks) VALUES
(1, 'Delayed', '2024-01-12', 'Weather issue'),
(2, 'Delivered', '2024-01-09', 'On time'),
(3, 'Delayed', '2024-01-15', 'Logistics problem');

-- READ
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM delivery_status;

-- UPDATE
UPDATE delivery_status SET status = 'Delivered', actual_delivery = '2024-01-14' WHERE order_id = 1;

-- DELETE
DELETE FROM delivery_status WHERE order_id = 3;

DELETE FROM orders WHERE order_id = 3;
-- Stored Procedure: Fetch all delayed deliveries for a customer
DELIMITER $$
CREATE PROCEDURE GetDelayedDeliveries(IN cust_id INT)
BEGIN
    SELECT c.name, o.order_id, o.product_name, o.expected_delivery,
           d.actual_delivery, d.status, d.remarks
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN delivery_status d ON o.order_id = d.order_id
    WHERE c.customer_id = cust_id AND d.status = 'Delayed';
END $$
DELIMITER ;

-- Call Stored Procedure
CALL GetDelayedDeliveries(1);