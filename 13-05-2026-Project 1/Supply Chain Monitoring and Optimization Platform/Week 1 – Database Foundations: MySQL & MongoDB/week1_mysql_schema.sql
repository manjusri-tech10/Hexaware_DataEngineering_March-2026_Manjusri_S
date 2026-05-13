-- 1. Database Creation
CREATE DATABASE supply_chain;
USE supply_chain;

-- 2. Create Tables
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    phone VARCHAR(20),
    location VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT NOT NULL,
    order_date DATE,
    delivery_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (product_id) REFERENCES inventory(product_id)
);

-- 3. Insert Sample Data

INSERT INTO suppliers (supplier_name, contact_email, phone, location)
VALUES
('ABC Supplies', 'abc@gmail.com', '9876543210', 'Chennai'),
('Global Traders', 'global@gmail.com', '9876501234', 'Bangalore'),
('Fast Logistics', 'fast@gmail.com', '9988776655', 'Mumbai');

INSERT INTO inventory (product_name, stock_quantity, reorder_level, supplier_id)
VALUES
('Laptop', 50, 20, 1),
('Mouse', 100, 30, 2),
('Keyboard', 25, 15, 2),
('Monitor', 10, 12, 3);

INSERT INTO orders (product_id, quantity, order_date, delivery_date, status)
VALUES
(1, 5, '2026-05-01', '2026-05-05', 'Delivered'),
(2, 10, '2026-05-03', '2026-05-10', 'Delayed'),
(3, 7, '2026-05-04', '2026-05-08', 'Delivered'),
(4, 2, '2026-05-06', '2026-05-15', 'Pending');

-- 4. CRUD Operations
INSERT INTO suppliers (supplier_name, contact_email, phone, location)
VALUES ('Tech World', 'tech@gmail.com', '9999999999', 'Hyderabad');

-- View all suppliers
SELECT * FROM suppliers;
-- View all inventory
SELECT * FROM inventory;
-- View all orders
SELECT * FROM orders;

-- Update
-- Update stock quantity
UPDATE inventory
SET stock_quantity = 80
WHERE product_id = 1;

-- Delete
-- Delete an order

DELETE FROM orders
WHERE order_id = 4;

-- 5. Stored Procedure (Auto Reorder Check)

-- Checks products below reorder level

DELIMITER //

CREATE PROCEDURE check_reorder()
BEGIN
    SELECT product_id,
           product_name,
           stock_quantity,
           reorder_level
    FROM inventory
    WHERE stock_quantity < reorder_level;
END //

DELIMITER ;
CALL check_reorder();

-- 6. Trigger (Auto Reduce Stock After Order)
DELIMITER //

CREATE TRIGGER reduce_stock
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE inventory
    SET stock_quantity = stock_quantity - NEW.quantity
    WHERE product_id = NEW.product_id;
END //

DELIMITER ;

-- 7. Join Query
-- Orders with supplier details

SELECT o.order_id,
       i.product_name,
       s.supplier_name,
       o.quantity,
       o.status
FROM orders o
JOIN inventory i ON o.product_id = i.product_id
JOIN suppliers s ON i.supplier_id = s.supplier_id;
